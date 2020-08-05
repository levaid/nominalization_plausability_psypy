import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from itertools import product

from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

variations = list(product(['image', 'sentence'], ['plaus', 'implaus'], ['cum', '1', '2']))


for stimtype, plaus, lname in variations:

    main_df = pd.read_csv('../stats/cum_lists.csv')
    verb_by_index = defaultdict(dict)
    cat_change_by_word = {}

    with open('../id_by_verb.csv', encoding='utf-8') as f:
        for line in f:
            i_, verb, morph, nom = line.strip().split(',')
            verb_by_index[i_]['verb'] = nom
            verb_by_index[i_]['morph'] = morph
            verb_by_index[i_]['cat_change'] = morph.count('_')-1
            cat_change_by_word[verb] = morph.count('_')-1


    normal = [12, 10]
    smaller = [7, 5.5]

    # print(cat_change_by_word)

    if lname != 'cum':
        main_df = main_df.query(f"list_name == {lname}")
        fontsizes = normal
    else:
        fontsizes = smaller


    main_df['verb'] = [verb_by_index[str(i)]['verb'] for i in main_df['stimulus_id'].values]
    main_df['cat_change'] = [verb_by_index[str(i)]['cat_change'] for i in main_df['stimulus_id'].values]
    main_df['key_resp_rt'] = main_df['key_resp.rt']

    main_df['verb_word'] = main_df['verb']

    rt_summ = main_df.groupby(['stimulus_name', 'stimulus_id', 'stimulus_type', 'stimulus_plaus']).key_resp_rt.describe()
    answ_roles_summ = main_df.groupby(['stimulus_name', 'stimulus_id', 'stimulus_type', 'stimulus_plaus']).answer_role.value_counts()

    answ_roles_data = answ_roles_summ.unstack(fill_value=0).reset_index()
    answ_roles_data['verb'] = [verb_by_index[str(i)]['verb'] for i in answ_roles_data.stimulus_id.values]
    answ_roles_data['cat_change'] = [verb_by_index[str(i)]['cat_change'] for i in answ_roles_data.stimulus_id.values]
    
    main_df['verb'] = main_df['verb'] + '_(' + main_df['stimulus_id'].astype(str) + ')'
    main_df['verb'] = main_df['verb'].apply(lambda row: row[:row.find('_')] if row[:5] != 'öltöz' else row)
    answ_roles_data['verb'] = answ_roles_data['verb'] + '_(' + answ_roles_data['stimulus_id'].astype(str) + ')'
    answ_roles_data['verb'] = answ_roles_data['verb'].apply(lambda row: row[:row.find('_')] if row[:5] != 'öltöz' else row)
    
    ratio_f = lambda x,y: x/(x+y)

    df = answ_roles_data.query(f"stimulus_type == '{stimtype}' and stimulus_plaus == '{plaus}'")
    df = df.sort_values(by='verb')
    p_vals = np.zeros((len(df), len(df)))
    relation_type = np.zeros((len(df), len(df)), dtype = str)
    for i, j in product(range(len(df)), range(len(df))):
        # print(i, j)
        p_vals[i, j] = stats.fisher_exact([df.iloc[i][['a', 'p']].values, df.iloc[j][['a', 'p']].values])[1]
        ratio_1, ratio_2 = ratio_f(df.iloc[i]['a'], df.iloc[i]['p']), ratio_f(df.iloc[j]['a'], df.iloc[j]['p'])
        if ratio_1 > ratio_2:
            relation_type[i, j] = '>'
        elif ratio_1 < ratio_2:
            relation_type[i, j] = '<'
        else:
            relation_type[i, j] = '='
            
    viridis = cm.get_cmap('viridis', 256)
    newcolors = viridis(np.linspace(0, 1, 256))
    pink = np.array([200/256, 0/256, 0/256, 1])
    newcolors[:13, :] = pink
    if lname == 'cum':
        newcolors[13:, :] = np.array([1, 1, 1, 1])
    newcmp = ListedColormap(newcolors)

    fig, ax = plt.subplots(figsize = (12,12), dpi = 300)
    im = ax.imshow(p_vals, cmap = newcmp, vmin=0, vmax=1)
    fig.colorbar(im, ax=ax, ticks = [0, 0.05, 0.1, 0.5, 1], shrink=0.8)

    ax.set_xticks(np.arange(len(df)))
    ax.set_yticks(np.arange(len(df)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(df['verb'], fontsize = fontsizes[0])
    ax.set_yticklabels(df['verb'], fontsize = fontsizes[0])

    ax.set_xlim((-0.5, len(df)-0.5))
    ax.set_ylim((-0.5, len(df)-0.5))

    for i, j in product(range(len(df)), range(len(df))):
        text = ax.text(j, i, f'{p_vals[i, j]:.2f}\n{relation_type[i,j]}', ha="center", va="center", color="w", fontsize = fontsizes[1])
        
    # Minor ticks
    ax.set_xticks(np.arange(-.5, len(df['verb']), 1), minor=True);
    ax.set_yticks(np.arange(-.5, len(df['verb']), 1), minor=True);

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='grey', linestyle='-', linewidth=1, alpha=0.5)
        
    ax.set_title(f"""Analysis of differences on agent and patient-based answers
                    P-values for Fisher's exact test on pairs of stimuli, p<0.05 (red) is significant
                    {stimtype}_{plaus} category""")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.savefig(f'l{lname}_heatmap_agpat_{stimtype}_{plaus}.png', bbox_inches='tight')
    
    df = main_df.query(f"stimulus_type == '{stimtype}' and stimulus_plaus == '{plaus}'")


    df = df.groupby('verb')['key_resp_rt'].apply(list).reset_index()
    df = df.sort_values(by='verb')

    relation_type = np.zeros((len(df), len(df)), dtype = str)


    p_vals = np.zeros((len(df), len(df)))
    for i, j in product(range(len(df)), range(len(df))):
        # print(i, j)
        p_vals[i, j] = stats.ttest_rel(df.iloc[i]['key_resp_rt'], df.iloc[j]['key_resp_rt'])[1]
        
        if np.mean(df.iloc[i]['key_resp_rt']) > np.mean(df.iloc[j]['key_resp_rt']):
            relation_type[i, j] = '>'
        elif np.mean(df.iloc[i]['key_resp_rt']) < np.mean(df.iloc[j]['key_resp_rt']):
            relation_type[i, j] = '<'
        else:
            relation_type[i, j] = '='
            
    viridis = cm.get_cmap('viridis', 256)
    newcolors = viridis(np.linspace(0, 1, 256))
    pink = np.array([200/256, 0/256, 0/256, 1])
    newcolors[:13, :] = pink
    
    if lname == 'cum':
        newcolors[13:, :] = np.array([1, 1, 1, 1])
        
    newcmp = ListedColormap(newcolors)

    fig, ax = plt.subplots(figsize = (12,12), dpi = 300)
    im = ax.imshow(p_vals, cmap = newcmp, vmin=0, vmax=1)
    fig.colorbar(im, ax=ax, ticks = [0, 0.05, 0.1, 0.5, 1], shrink=0.8)


    ax.set_xticks(np.arange(len(df)))
    ax.set_yticks(np.arange(len(df)))   

    # ... and label them with the respective list entries
    ax.set_xticklabels(df['verb'], fontsize = fontsizes[0])
    ax.set_yticklabels(df['verb'], fontsize = fontsizes[0])

    ax.set_xlim((-0.5, len(df)-0.5))
    ax.set_ylim((-0.5, len(df)-0.5))
    
    # Minor ticks
    ax.set_xticks(np.arange(-.5, len(df['verb']), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(df['verb']), 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='grey', linestyle='-', linewidth=1, alpha=0.5)

    for i, j in product(range(len(df)), range(len(df))):
        text = ax.text(j, i, f'{p_vals[i, j]:.2f}\n{relation_type[i,j]}', ha="center", va="center", color="w", fontsize = fontsizes[1])

        
    ax.set_title(f"""Analysis of differences in reaction time
                    P-values for paired T-test on pairs of stimuli, p<0.05 (red) is significant
                    {stimtype}_{plaus} category, symbol is based on mean""")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.savefig(f'l{lname}_heatmap_rt_{stimtype}_{plaus}.png', bbox_inches='tight')



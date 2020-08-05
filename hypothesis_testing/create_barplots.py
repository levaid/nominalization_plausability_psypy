import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from itertools import product

variations = list(product(['image', 'sentence'], ['plaus', 'implaus'], ['1', '2', 'cum']))


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
            cat_change_by_word[nom] = morph.count('_')-1

    normal = [12, 10]
    smaller = [7, 5.5]

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

    
    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)


    df = main_df.query(f"stimulus_type == '{stimtype}' and stimulus_plaus == '{plaus}'")
    data_agentive = df.query("answer_role == 'a'").groupby('verb')['key_resp_rt'].apply(list)
    data_patientive = df.query("answer_role == 'p'").groupby('verb')['key_resp_rt'].apply(list)

    df_resp = pd.DataFrame(data_agentive).join(data_patientive, how = 'outer', lsuffix = 'ag', rsuffix='pat').reset_index()
    df_resp['cat_change'] = [cat_change_by_word[verb[:verb.find('_')]] if '_' in verb else cat_change_by_word[verb] for verb in df_resp.verb]
    df_resp = df_resp.sort_values(by=['cat_change', 'verb'])
    df_resp['key_resp_rtag'] = df_resp['key_resp_rtag'].apply(lambda x: [] if isinstance(x, float) else x)

    plt.figure(figsize=(9,4), dpi=300)
    plt.grid()
    barWidth = 0.25

    first_two = np.argwhere(df_resp.cat_change.values-1).flatten()[0]*2-0.8
    plt.plot([first_two-barWidth, first_two-barWidth], [1, 8], color = 'red', linewidth=3)


    bpl = plt.boxplot(df_resp.key_resp_rtag, positions=np.array(range(len(df_resp.key_resp_rtag)))*2.0-0.4, widths=0.6)
    bpr = plt.boxplot(df_resp.key_resp_rtpat, positions=np.array(range(len(df_resp.key_resp_rtpat)))*2.0+0.4, widths=0.6)
    set_box_color(bpl, 'green') # colors are from http://colorbrewer2.org/
    set_box_color(bpr, 'blue')

    plt.plot([], c='green', label='agent')
    plt.plot([], c='blue', label='patient')

    plt.legend()

    plt.xticks(range(0, len(df_resp.verb) * 2, 2), df_resp.verb, rotation=45, ha='right', fontsize=6)
    plt.ylim((0.9,8.1))

    plt.title(f'Distribution of reaction times in {plaus}_{stimtype} category \nwith 1 category change on left side, 2 on the right side')

    plt.savefig(f'l{lname}_rt_barplot_{stimtype}_{plaus}.png', bbox_inches='tight')
    
    #answ_roles_data.plot.bar(x='verb', y='p', figsize=(16, 8), rot=45)
    df = answ_roles_data.query(f"stimulus_type == '{stimtype}' and stimulus_plaus == '{plaus}'").sort_values(by=['cat_change', 'verb'])

    barWidth = 0.3

    r1 = np.arange(len(df['verb']))
    r2 = [x + barWidth for x in r1]

    first_two = np.argwhere(df.cat_change.values-1).flatten()[0]

    plt.figure(figsize=(9,4), dpi=300)
    plt.grid()

    plt.bar(r1, df['a'], color='green', width=barWidth, edgecolor='white', label='agent')
    plt.bar(r2, df['p'], color='blue', width=barWidth, edgecolor='white', label='patient')
    plt.plot([first_two-barWidth, first_two-barWidth], [0, 23], color = 'red', linewidth=3)
    #plt.xlim((-0.5, 19.5))

    plt.xticks([r + barWidth/2 for r in range(len(df['verb']))], df['verb'], rotation=45, ha='right', fontsize=6)

    for i, v in zip(list(r1) + list(r2), list(df['a']) + list(df['p'])):
        if i % 1 != 0:
            color = 'blue'
        else:
            color = 'green'
        plt.text(i, v+0.4, str(v), color=color, fontsize = 6, ha='center', va='center')


    plt.ylim((0, 23))
    
    plt.yticks(range(0,22,3))

    plt.title(f'Answers\' distribution in {plaus}_{stimtype} category \nwith 1 category change on left side, 2 on the right side')
    plt.legend()
    plt.savefig(f'l{lname}_ap_lineplot_{stimtype}_{plaus}.png', bbox_inches='tight')

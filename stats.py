import pandas as pd
import os
import csv
# print(os.listdir(os.path.join('..', 'data')))

def do_statistics(filename):
    output_tables = []

    raw_output = pd.read_csv(filename+'.csv', engine='python', encoding='utf-8-sig')

    raw_output['answer_role'] = raw_output['key_resp.keys'].where(pd.isna(raw_output['answer_role']), raw_output['answer_role'])
    writer = pd.ExcelWriter(filename+'_data.xlsx')
    raw_output.to_excel(writer, 'sheet1', index=False, float_format='%.4f')
    writer.save()

    # have to inspect that the xls created is, in fact, valid
    table = pd.read_excel(filename+'_data.xlsx')
    table_answered = table[table['key_resp.keys'] != 'n']

    if sum(table['key_resp.keys'] != 'n') == len(table):
        theresnotanswered = False
    else:
        theresnotanswered = True

    if sum(table['retried']) > 0:
        theresretry = True
    else:
        theresretry = False

    table_answered_but_retried = table_answered[table_answered['retried'] == 1]
    # print(table)
    table_sentence = table_answered[(table_answered['stimulus_type'] == 'sentence')].rename(columns={'stimulus_plaus':'sentences_stimulus_plaus', 'word_order':'sentences_word_order'})
    table_image = table_answered[(table_answered['stimulus_type'] == 'image')].rename({'stimulus_plaus':'images_stimulus_plaus'})

    output_tables.append(pd.crosstab([table['stimulus_type'],table['stimulus_plaus']],table['answer_role'], margins = True))

    output_tables += [table_answered.groupby(['stimulus_plaus'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]

    output_tables += [table_sentence.groupby(['sentences_word_order'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]

    if theresretry:
        output_tables += [table_sentence.groupby(['sentences_word_order', 'retried'], as_index=True).agg(
                        {'key_resp.rt':['mean','std', 'min', 'max']})]

        output_tables += [table_answered.groupby(['stimulus_plaus', 'retried'], as_index=True).agg(
                        {'key_resp.rt':['mean','std', 'min', 'max']})]

    output_tables += [table_sentence.groupby(['sentences_word_order', 'sentences_stimulus_plaus'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]

    output_tables += [table_sentence.groupby(['sentences_word_order', 'sentences_stimulus_plaus', 'answer_role'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
                    
    output_tables += [table_answered.groupby(['stimulus_type'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
    output_tables += [table_answered.groupby(['stimulus_type', 'stimulus_plaus'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
    output_tables += [table_answered.groupby(['answer_role'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
    output_tables += [table_answered.groupby(['nom1_indented'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
    output_tables += [table_answered.groupby(['nom2_indented'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]
    output_tables += [table_answered.groupby(['key_resp.keys'], as_index=True).agg(
                    {'key_resp.rt':['mean','std', 'min', 'max']})]

    # BUG in old pandas, you can't normalize by multiindex
    # output_tables.append(pd.crosstab([table['stimulus_type'],table['stimulus_plaus']],table['answer_role'], margins = True, normalize='index'))
    output_tables.append(pd.crosstab(table['stimulus_plaus'],table['answer_role'], margins = True, normalize='index'))

    if theresretry:
        output_tables.append(pd.crosstab(table['retried'],table['stimulus_plaus'], margins = True, normalize='index'))
        output_tables.append(pd.crosstab(table['retried'],table['answer_role'], margins = True, normalize='index'))
    output_tables.append(pd.crosstab(table_sentence['sentences_stimulus_plaus'],table_sentence['answer_role'], margins = True))
    test = pd.crosstab(table_sentence['sentences_word_order'],table_sentence['answer_role'], margins = True)
    output_tables.append(test)
    #output_tables.append(pd.crosstab(table_image['stimulus_plaus'],table_image['answer_role'], margins = True))
    output_tables.append(pd.crosstab(table['key_resp.keys'],table['answer_role'], margins = True))
    output_tables.append(pd.crosstab(table['nom1_indented'],table['key_resp.keys'], margins = True))
    output_tables.append(pd.crosstab(table['nom2_indented'],table['key_resp.keys'], margins = True))


    writer = pd.ExcelWriter(filename+'_statistics.xlsx')
    offset = 0
    for dataframe in output_tables:
        # print(dataframe)
        dataframe.to_excel(writer, "sheet1", index=True, startrow=offset, float_format='%.4f')
        offset += len(dataframe) + 5
    writer.save()

if __name__=='__main__':
    filename = 'data/int_Zimmerertest_2019_Dec_17_1445'
    do_statistics(filename)
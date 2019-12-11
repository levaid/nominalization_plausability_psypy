import pandas as pd
import os
import csv
# print(os.listdir(os.path.join('..', 'data')))
filename = 'data/xls_2_teszt_Zimmerertest_2019_Dec_10_1226'

output_tables = []

raw_output = pd.read_csv(filename+'.csv', engine='python', encoding='utf-8-sig')
writer = pd.ExcelWriter(filename+'_data.xlsx')
raw_output.to_excel(writer, 'sheet1', index=False)
writer.save()

# have to inspect that the xls created is, in fact, valid
table = pd.read_excel(filename+'_data.xlsx')
# print(table)
table_sentence = table[(table['stimulus_type'] == 'sentence')].rename(columns={'stimulus_plaus':'sentences_stimulus_plaus', 'word_order':'sentences_word_order'})
table_image = table[(table['stimulus_type'] == 'image')].rename({'stimulus_plaus':'images_stimulus_plaus'})
# table_csv = pd.read_csv(filename+'.csv', engine='python')
output_tables.append(pd.crosstab([table['stimulus_type'],table['stimulus_plaus']],table['answer_role'], margins = True))

output_tables += [table.groupby(['stimulus_plaus'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]

output_tables += [table_sentence.groupby(['sentences_word_order'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]

output_tables += [table_sentence.groupby(['sentences_word_order', 'sentences_stimulus_plaus'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
                
output_tables += [table.groupby(['stimulus_type'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
output_tables += [table.groupby(['stimulus_type', 'stimulus_plaus'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
output_tables += [table.groupby(['answer_role'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
output_tables += [table.groupby(['nom1_indented'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
output_tables += [table.groupby(['nom2_indented'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]
output_tables += [table.groupby(['key_resp.keys'], as_index=False).agg(
                {'key_resp.rt':['mean','std', 'min', 'max']})]

# BUG in old pandas, you can't normalize by multiindex
# output_tables.append(pd.crosstab([table['stimulus_type'],table['stimulus_plaus']],table['answer_role'], margins = True, normalize='index'))
output_tables.append(pd.crosstab(table['stimulus_plaus'],table['answer_role'], margins = True, normalize='index'))

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
    dataframe.to_excel(writer, "sheet1", index=True, startrow=offset)
    offset += len(dataframe) + 5
writer.save()

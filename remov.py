text_list = ['over1000_2019_08_14_09_01',
             'over500-1000_2019_08_14_09_01',
             'over50-500_2019_08_14_09_00']

count = 0

for text in text_list:

    with open(text+'.txt','r') as text_line:

        for line in text_line:
            col = line.strip().split('\t')

            if 'gene_id' in col[0]:
                if count == 0:
                    count+=1
                    with open('all_range_data.txt','w') as w:
                        w.write(line)
                else:
                    continue

            elif 'TCGA' in col[0]:
                continue

            elif '\t' in line:
                if 'MT-' in col[19]:
                    continue
                else:
                    with open('all_range_data.txt', 'a') as w:
                        w.write(line)

            else:
                continue
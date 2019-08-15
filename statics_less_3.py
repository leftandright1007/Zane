with open('ncbi_yes_value.txt','r') as r:
    count1 = 0
    for line in r:
        item = line.strip().split('\t')
        if count1 == 0:
            count1+=1
            item.extend(['avg','num_line'])
            with open('picture_value_statics.txt','w') as w:
                w.write('\t'.join(item)+'\n')
        else:
            avg = 0
            count_avg = 0
            for i in range(len(item)):
                if i >= 2:
                    numbbb = float(item[i])
                    avg = avg+numbbb
                    count_avg+=1
            avg = avg / count_avg

            num_line = 0
            for boln in range(len(item)):
                if boln >= 2:
                    if float(item[boln]) > avg * 0.5:
                        num_line+=1
                    else:
                        pass
            if num_line == 1:# and num_line <= 3:
                item.extend([str(avg),str(num_line)])
                with open('picture_value_statics.txt', 'a') as w:
                    w.write('\t'.join(item) + '\n')


# with open('fin_all_numid.txt','r') as gene:
#     gene_dict = {}
#     for line1 in gene:
#         gene_item = line1.strip().split('\t')
#         gene_dict[gene_item[1]] = gene_item[0]
#
#     with open('picture_value_statics.txt', 'r') as va:
#         count_gnv = 0
#         for line2 in va:
#             va_item = line2.strip().split('\t')
#             if count_avg == 0:
#                 count_avg+=1
#                 with open('gene_num_value.txt', 'w') as gnv:
#                     gnv.write(gene_dict[str(va_item[0])] + '\t' + line2)
#             else:
#                 with open('gene_num_value.txt', 'a') as gnv:
#                     gnv.write(gene_dict[str(va_item[0])]+'\t'+line2)


with open('picture_value_statics.txt', 'r') as tail:
    tail_list = []
    for line3 in tail:
        tail_item = line3.strip().split('\t')
        tail_list.append(tail_item[0])

    with open('all_range_data.txt', 'r') as rna:
        count_rna = 0
        for line4 in rna:
            rna_item = line4.strip().split('\t')
            if rna_item[1] in tail_list:
                if count_rna == 0:
                    count_rna+=1
                    with open('survel.txt','w') as finl:
                        finl.write(line4)
                else:
                    with open('survel.txt','a') as finl:
                        finl.write(line4)
            else:
                pass
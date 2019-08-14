ensg_ncbi_dict = {}
value_dict = {}

with open('onle_human.txt','r') as r:
    for line in r:
        item = line.rstrip().split('\t')
        if item[2] not in ensg_ncbi_dict:
            ensg_ncbi_dict[item[2]] = item[1]
        else:
            pass
# print(ensg_ncbi_dict['ENSG00000274012'])


with open('all_range_data.txt','r') as allr:
    for line2 in allr:
        item2 = line2.strip().split('\t')
        if 'gene_id' in item2[0]:
            with open('all_range_ncbi_data.txt', 'w') as ncbi:
                ncbi.write(line2)
            with open('ensg_error.txt', 'w') as error:
                error.write(line2)
            with open('ensg_ncbi_id.txt', 'w') as ncbi_ensg_id:
                ncbi_ensg_id.write(item2[1]+'\t'+'NCBI_id'+'\n')
        else:
            if item2[1] in ensg_ncbi_dict:
                with open('all_range_ncbi_data.txt','a') as ncbi:
                    ncbi.write(line2.rstrip()+'\t'+ensg_ncbi_dict[item2[1]]+'\n')

                if item2[1] not in value_dict:
                    value_dict[item2[1]] = ensg_ncbi_dict[item2[1]]
                # with open('ensg_ncbi_id.txt', 'a') as ncbi_ensg_id:
                #     ncbi_ensg_id.write(item2[1]+'\t'+ensg_ncbi_dict[item2[1]]+'\n')
            else:
                with open('ensg_error.txt','a') as error:
                    error.write(line2)
for key in value_dict:
    with open('ensg_ncbi_id.txt', 'a') as ncbi_ensg_id:
        ncbi_ensg_id.write(key+'\t'+ensg_ncbi_dict[key]+'\n')
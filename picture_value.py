import requests
count1 = 0
with open('ensg_ncbi_id.txt','r') as anil:
    for idid in anil:
        num_id = idid.strip().split('\t')
        va = []

        if count1 == 0:
            count1+=1
            with open('ncbi_yes_value.txt','w') as yes:
                yes.write(idid)
            with open('ncbi_no_value.txt','w') as no:
                no.write(idid)

        else:
            if len(num_id) <= 5:
                va.extend([num_id[0], num_id[1]])
                r = requests.get('https://www.ncbi.nlm.nih.gov/projects/Gene/download_expression.cgi?PROJECT_DESC=PRJEB4337&GENE='+num_id[1])
                # print(r)
                # print(r.text)

                text1 = r.text.strip().split('\t')
                # print(len(text1))
                if len(text1) >= 20:
                    for nmu in range(len(text1)):
                        # if count1 == 0:
                        #     print('gene_id',end='\t')
                        # if nmu > 0 and nmu <= 27:
                        #     if nmu == 28:
                        #         print(text1[nmu])
                        #     else:
                        #         print(text1[nmu],end='\t')
                        if nmu >=29:
                            va.append(text1[nmu])
                            # if nmu == len(text1):
                            #     print(text1[nmu])
                            # else:
                            #     print(text1[nmu],end='\t')
                    with open('ncbi_yes_value.txt','a') as yes:
                        # va1 = '\t'.join(va)
                        # va2 = va1.strip()
                        yes.write('\t'.join(va)+'\n')
                else:
                    with open('ncbi_no_value.txt', 'a') as no:
                        no.write(idid)

            else:
                with open('ncbi_yes_value.txt','a') as yes:
                    # va1 = '\t'.join(va)
                    # va2 = va1.strip()
                    yes.write(idid)
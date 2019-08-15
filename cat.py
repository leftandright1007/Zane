ncid_dict = {}
with open('new_yes.txt', 'r') as ncid:
    for line2 in ncid:
        item2 = line2.rstrip().split()
        ncid_dict[item2[0]] = []
        for aa in range(len(item2)):
            if aa >= 1:
                ncid_dict[item2[0]].append(item2[aa])

with open('all_range_data.txt','r') as all:
    for line in all:
        item = line.rstrip().split()

        if item[1] == 'ENSGID':
            with open('cat_all.txt', 'w') as cat:
                cat.write(line.rstrip() + '\t' + '\t'.join(ncid_dict[item[1]]) + '\n')

        elif item[1] in ncid_dict:
            with open('cat_all.txt', 'a') as cat:
                cat.write(line.rstrip() + '\t' + '\t'.join(ncid_dict[item[1]]) + '\n')
        else:
            with open('cat_all.txt', 'a') as cat:
                cat.write(line)

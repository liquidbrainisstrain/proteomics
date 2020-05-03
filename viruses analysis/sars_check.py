from pymongo import MongoClient
from modules import mot_finder as mf
from modules import seq_liner_full as slf
from modules import fasta_parser as fp
import pprint

#db init
client = MongoClient()
db = client.proteins
homo = db.homo_proteom
gen = db.gen_proteom_beta
# proteom = [i for i in homo.find()]
gproteom = [i for i in gen.find()]

covid_prots = fp('/viruses analysis/covid-19.fasta')

#compare otherXcorona
counter = 0
for protein in covid_prots:
    result = []
    for pr in gproteom:
        res = mf(pr['seq'], protein['seq'], motlen=8)
        if len(res) > 0:
            print('lucky!')
            lines = slf(res[0], [pr['seq'], protein['seq']])
            if lines[3] > 10:
                lines.append(pr['name'])
                lines.append(protein['name'])
                lines.append(pr['organism'])
                lines.append(pr['div_time'])
                pprint.pprint(lines)
                result.append(lines)
        counter+=1
        if counter % 1000 == 0:
            print(counter)
    result = sorted(result, key=lambda item: item[7], reverse=True)
    filename = '/Users/liquidbrain/projects/Proteomics/viruses analysis/results/' + protein['name'] + '.txt'
    with open(filename, 'a') as file:
        for i in result:
            line = "organism - {}\n   divtime = {} \n   homology = {} \n   organism protein name - {}\n   virus protein " \
                   "name{}\n{}\n{}\n{}\n-------------------\n".format(i[6], i[7], i[3], i[4], i[5], i[0], i[1], i[2])
            file.write(line)



# with open('/Users/liquidbrain/projects/Proteomics/viruses analysis/result.txt', 'a') as file:
#     for i in result:
#         line = "organism - {}\n   divtime = {} \n   homology = {} \n   organism protein name - {}\n   virus protein " \
#                "name{}\n{}\n{}\n{}\n-------------------\n".format(i[6], i[7], i[3], i[4], i[5], i[0], i[1], i[2])
#         file.write(line)
#         #i[0белок,1белок вируса,2общая последовательность,3сходство,4название белка,5белок вируса,6организм,7времядив]

from pymongo import MongoClient
from modules import dif_seq_liner as dsl
from modules import fasta_parser
seq1 = 'MVIKKMQPEDLTENDIRRFADSKRIFGRGESYYRRGKIRSMDVSRDKKEITAKVDGNYGIYDVEIYFDEDGISADCDCPYDGYGCKHIVAVLLEFLYEFKGDKKDNEDEEPWDITLEDIRGHTSKQSILDAFDLLKEKKVEIKSLTNKRMTAEIDEKITRHTYPWQKDIVGNAMVKITRGNYNLSYPLGTECNCTGYGRADCKHVAASLLAIFLQKNKKQISEVKEEFISQIRSERFNRFTRELDSISLEEPKVKHTRNYMFYFKAEKDTRPYSKFSLLIEKRCILKSCGLGTPSQVTTKFLKEYEDTIPNNRKRIFNSFIWSLENEERWRSSSEKLIKQNFKESDSKLLAEMRKLYMADPHAFENCVFPSEKGEIEIKISEEKKRKKSVLKLMVNIGEKKFQINKKNVTFLGKHPLWVSIFENEKNGFIIFELDCSQPEIIKKLAGFSNAELELNQLNAFIEKYYLTLSAIGKITLPENYDVEEQRFEPVPRLFLRDYGTSFSIELRFLYDKQEVLYTQKQDIVFKNDREKIIRIQRDREKEKEYFANLLDHHTTDCDDFLVPATDPYLWLVDVANDLITRGYEIYGASELLNTRIAPHEPKLRLEVSSGIDWFDLKGDVSYGAEKVPFDEIISHVNNHERFVKLSDGTRGVIPKKWLEKLSGTVGLLERDEKNGNAKASRSQIALVEALLDISEKSRVDKRFKQMKEKFSGFREIRNVSLPKKLDGELREYQKAGYDWLHFLKDFSFGGCLADEMGLGKTVQALSLLLYEKERGIKTPSLVVVPTSLVFNWVNEVKKFTPSLKVYIHHGSERVREGKQIWKKKANIILTTYGTLRNDANIFKNKKFHYVILDESQHIKNPLSKTAKKIYGLKSKHKLAMTGTPIENNSFELWSQFAFLNPGLLGNMDYFKKNFAKSIEKEKDEDKTKALKNMINPFLLMRKKEMVAKDLPEKQISVSYCEMDRKQREVYEFWKSRIRNEIETTIKEEGFMKSRFKILQGLMKLRQICNHPVLVDESFTGDSGKLNMLMEQIEEVIAEGHKVLVFSSFVKMLGVFRGEFERKGIRFSYLDGSTRNRKQVVEQFQEDPDMRAFLISLKAGGLGLNLTEADYVFIVDPWWNPAAEMQAIDRTHRIGQEKNIFVYKAITKDSIEEKILQLQESKLDLVKNVIAVDDGLFKKLNKEDINKLFA'
mot1 = 'LADEMGLGKTVQ'

mots = ['LADDMGLGKTLQ', 'LADEMGLGKTIQ', 'LADEMGLGKTVE', 'LGDDMGLGKTVQ', 'LADEMGLGKTIS', 'LADDMGLGKTCQ', 'LADEMGLGKTIA',
        'LADEMGLGKTIM', 'VADEMGLGKTIQ', 'LADEVGLGKTVE', 'LADQMGLGKTIQ', 'LADEMGLGKTCQ', 'LADEMGMGKTIQ', 'LADEMGLGKTVS',
        'LADEMGLGKTAQ', 'LADEMGLGKTVQ', 'LADDMGLGKTIQ', 'LADEMGLGKTLQ', 'MADEMGLGKTLQ', 'LADEMGLGKTIE', 'LGDEMGLGKTIQ',
        'LGDEMGLGKTCQ']

archea = fasta_parser('/Users/liquidbrain/Desktop/archea_full.fasta')

#db init
client = MongoClient()
db = client.proteins
all_proteins = db.gen_proteom_beta
arc_mots = db.archea_mots
# proteoms = [i for i in all_proteins.find()]

#export pattern
div = '-------------------------------------------------------------\n'

filename = '/Users/liquidbrain/Desktop/results/' + mot1 + '_in_archea.txt'

with open(filename, 'w') as file:
    line = 'Result file fo mot{' + mot1 + '}\n'
    file.write(line)
    for mot in mots:
        for prot in archea:
            if prot['seq'].count(mot) > 0:
                res = dsl(seq1, mot1, prot['seq'], mot)
                line = 'Organism - {}\n Protein - {}\n Link - {}\n Similarity percent - {}\n{}\n{}\n{}\n'.format(
                    prot['organism'], prot['name'], prot['ref'], res[3], res[0], res[1], res[2]
                )
                file.write(line)
                file.write(div)

from pymongo import MongoClient
from modules import mot_finder as mf
import pprint

#db init
client = MongoClient()
db = client.proteins
gen_prot2 = db.gen_proteom_beta

proteoms = [i for i in gen_prot2.find()]

app = 'MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTVAKETCSEKSTNLHDYGMLLPCGIDKFRGVEFVCCPLAEESDNVDSADAEEDDSDVWWGGADTDYADGSEDKVVEVAEEEEVAEVEEEEADDDEDDEDGDEVEEEAEEPYEEATERTTSIATTTTTTTESVEEVVREVCSEQAETGPCRAMISRWYFDVTEGKCAPFFYGGCGGNRNNFDTEEYCMAVCGSAMSQSLLKTTQEPLARDPVKLPTTAASTPDAVDKYLETPGDENEHAHFQKAKERLEAKHRERMSQVMREWEEAERQAKNLPKADKKAVIQHFQEKVESLEQEAANERQQLVETHMARVEAMLNDRRRLALENYITALQAVPPRPRHVFNMLKKYVRAEQKDRQHTLKHFEHVRMVDPKKAAQIRSQVMTHLRVIYERMNQSLSLLYNVPAVAEEIQDEVDELLQKEQNYSDDVLANMISEPRISYGNDALMPSLTETKTTVELLPVNGEFSLDDLQPWHSFGADSVPANTENEVEPVDARPAADRGLTTRPGSGLTNIKTEEISEVKMDAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIATVIVITLVMLKKKQYTSIHHGVVEVDAAVTPEERHLSKMQQNGYENPTYKFFEQMQN'
bam = 'GSNKGAIIGLM'
counter = 0
#prog start

app_mots = ['HLHWHTVAKE', 'NLHDYGMLLPCGID', 'ADKKAVIQHFQEKVE', 'VDPKKAAQIR', 'KKQYTSIHHGV', 'EVDAAVTPEERHL',
            'LNMHMNVQNGKW', 'SDPSGTKTCI', 'MSQSLLKTTQE', 'NGYENPTYK', 'AEPQIAMFCG', 'HLHWHTVAKE', 'NLHDYGMLLPCGID',
            'FRGVEFVCCP', 'DDSDVWWGGAD', 'DENEHAHFQKAKE', 'KKQYTSIHHG', 'WTARALEVPTDGNAGLLAEPQIAMFCG',
            'RALEVPTDGNAGLLAEPQIAMFCG']

for protein in proteoms:
    res = mf(app, protein['seq'], motlen=9)
    if len(res)>0:
        print(res)
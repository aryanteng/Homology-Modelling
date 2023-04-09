from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='5xjy', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5xjyA', atom_files='5xjy.pdb')
aln.append(file='Query.pir', align_codes='1YES')
aln.align2d(max_gap_length=50)
aln.write(file='Target-template.ali', alignment_format='PIR')
aln.write(file='Target-template.pap', alignment_format='PAP')
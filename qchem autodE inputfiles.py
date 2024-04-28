import autode as ade
from autode.wrappers.keywords import MaxOptCycles

ade.Config.QChem.keywords.low_opt = ['method wB97X-V', 'basis def2-SVP', "jobtype opt", MaxOptCycles(10)]
ade.Config.QChem.keywords.grad = ['method wB97X-V', 'basis def2-SVP', "jobtype force"]
ade.Config.QChem.keywords.low_sp = ['jobtype SP', 'method wB97X-V', 'basis def2-SVP']
ade.Config.QChem.keywords.opt = ['method wB97X-V', 'basis def2-TZVP', "jobtype opt"]
ade.Config.QChem.keywords.opt_ts = ['method wB97X-V', 'basis def2-TZVP', "jobtype TS"]
ade.Config.QChem.keywords.hess = ['method wB97X-V', 'basis def2-TZVP', "jobtype Freq"]
ade.Config.QChem.keywords.sp = ['jobtype SP', 'method wB97M-V', 'basis def2-tzvppd']

ade.Config.n_cores = 16
ade.Config.lcode = 'XTB'
ade.Config.hcode = 'QChem'

Testfinal1=ade.Molecule(smiles='C=CC')
Testfinal2=ade.Molecule(smiles='C/C=C\C')
Testfinal3=ade.Molecule(smiles='C=C(C)C')
Testfinal4=ade.Molecule(smiles='C/C(C)=C/C')
Testfinal5=ade.Molecule(smiles='C/C(C)=C(C)/C')


Testfinal1.optimise(method=ade.methods.get_lmethod())
Testfinal1.optimise(method=ade.methods.get_hmethod())

Testfinal2.optimise(method=ade.methods.get_lmethod())
Testfinal2.optimise(method=ade.methods.get_hmethod())

Testfinal3.optimise(method=ade.methods.get_lmethod())
Testfinal3.optimise(method=ade.methods.get_hmethod())

Testfinal4.optimise(method=ade.methods.get_lmethod())
Testfinal4.optimise(method=ade.methods.get_hmethod())

Testfinal5.optimise(method=ade.methods.get_lmethod())
Testfinal5.optimise(method=ade.methods.get_hmethod())

Testfinal1.energy.to('kcal')
Testfinal2.energy.to('kcal')
Testfinal3.energy.to('kcal')
Testfinal4.energy.to('kcal')
Testfinal5.energy.to('kcal')

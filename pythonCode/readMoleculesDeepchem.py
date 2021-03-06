#Copyright (C) 2018 Andreas Mayr
#Licensed under GNU General Public License v3.0 (see http://www.bioinf.jku.at/research/lsc/LICENSE and https://github.com/ml-jku/lsc/blob/master/LICENSE)

import rdkit
import rdkit.Chem
import deepchem
import deepchem.feat
import os



chemblFilename=os.environ.get("HOME")+"/mydata/raw/chembl20/chembl_20.sdf"
chemblMols=rdkit.Chem.SDMolSupplier(chemblFilename, True, False, False)
chemblMolsArr=[]
for ind in range(len(chemblMols)):
  mol=chemblMols[ind]
  if mol is not None:
    mol=rdkit.Chem.rdmolops.RenumberAtoms(mol, rdkit.Chem.rdmolfiles.CanonicalRankAtoms(mol))  
  chemblMolsArr.append(mol)

import numpy as np
chemblMolsArrCopy=np.array(chemblMolsArr)



import pickle
import os

fileObject=open(os.getenv("HOME")+"/mydata/trgpred/chembl20/dataPython/chembl20Deepchem.pckl",'wb')
pickle.dump(chemblMolsArrCopy, fileObject)
fileObject.close()

# Content Descrption

## Sample Molecules 
847 test molecules were held out from training and
used in analysis.
246 molecules for the Natural Product Data Base 
(Rigid molecules) and
601 molecules from the Marine data base


In tab sperated xyz files.
- Line 1 
   -- Name of molecule, 
   -- energy for the geometry method,
   -- number of negative frequencies
- Line 2
   -- number of atoms
- Remaining lines
  -- atom label (indicating atom type)
  -- x y z coordinates
  -- predicted/neural-net NMR shift
  -- wB97XD predicted shift at wB97XD geometry
  -- for the "Rigid Set" the experimentally determined NMR value
- Then Line 1 of the next molecule, etc.

## XYZ Files
- marine_newNNgeoms_v15.xyz
- marine_newXDgeoms_v15.xyz
- NPDB_Rigid_for_test_with_expt_v15_NNgeom.xyz
- NPDB_Rigid_for_test_with_expt_v15_XDgeom.xyz
- input.xyz (a small sample file)

## Files to run the Neural Net module
- **read_xyz.py**  subroutine to read xyz files
- **run_model.py**  wrapper to
- **DLNMR1.pt** the weights for the Neural Network

## Training set InChIs
- **selected_drugs.xlsx** some synthetic drugs and drug like molecules used in the training set

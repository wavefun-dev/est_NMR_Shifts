run_model.py: This can be used to apply the shift (proton + C) computation.  It defaults to using the 'input.xyz' molecule.

847 test molecules were held out from training and used in analysis. The respective geometries are defined as:

246 molecules for the Natural Product Data Base (Rigid molecules):
 NPDB_Rigid_for_test_with_expt_v15_NNgeom.xyz
  "Name" "X-coord" "Y-coord" "Z-Coord" NN//NN-shift  XD//XD-shift expt.-shift

 NPDB_Rigid_for_test_with_expt_v15_XDgeom.xyz
  "Name" "X-coord" "Y-coord" "Z-Coord" NN//XD-shift  XD//XD-shift expt.-shift
  
601 molecules from the Marine data base:
 marine_newNNgeoms_v15.xyz
  "Name" "X-coord" "Y-coord" "Z-Coord" NN//NN-shift  XD//XD-shift 
 marine_newXDgeoms_v15.xyz
  "Name" "X-coord" "Y-coord" "Z-Coord" NN//XD-shift  XD//XD-shift 

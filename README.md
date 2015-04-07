# mindist-membrane-lipids


Python scripts for analyzing molecular dynamics simulation trajectories.
Molecular system: lipid bilayer system with transmembrane molecules.


step1:
   dcd_unwrap.tcl: to unwrap molecular dynamics simulation trajectories.

   # unwrap trajectory
   vmd -dispdev none
   vmd> source dcd_unwrap.tcl

   # convert dcd to xyz
   catdcd -o dppc_p.xyz -otype xyz -stype pdb -s ../dppc_p.pdb  dppc_p.dcd


step2: 
   dist_nearest_neighbor.py: to plot time series and histograms of all pairs of DPPC P atoms that are initially nearest neighbors.

   # analysis:
   ./dist_nearest_neighbor.py dppc_p.xyz

   # test: test.xyz is an example file of dppc_p.xyz
   ./dist_nearest_neighbor.py test.xyz

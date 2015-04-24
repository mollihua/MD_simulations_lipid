# mindist-membrane-lipids


Python and Tcl scripts for analyzing molecular dynamics simulation trajectories.

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
   
   ./dist_nearest_neighbor.py dppc_p.xyz 1 -1
   
   or
   
   ./dist_nearest_neighbor.py dppc_p.xyz framenum1 framenum2
   
   for user-defined framenum1 and framenum2

   # test: test.xyz is an example file of dppc_p.xyz
   
   ./dist_nearest_neighbor.py test.xyz 1 -1

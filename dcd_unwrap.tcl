# Macbook:
#source /Users/chemo/Desktop/VMD\ 1.9.2.app/Contents/vmd/plugins/noarch/tcl/pbctools2.8/pbctools.tcl

# Ubuntu:
package require pbctools

# load in trajectories
set mol [mol new ../step5_assembly.psf type psf waitfor all]
mol addfile step7.1_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.2_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.3_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.4_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.5_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.6_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.7_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.8_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.9_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol
mol addfile step7.10_production.dcd type dcd first 0 last -1 step 10 waitfor all $mol

# can also use animate to load in trajectories,for example:
# animate read dcd step7.1_production.dcd skip 10 waitfor all

# unwrap trajectory
pbc unwrap -all

# write dppc P trajectory
animate write dcd dppc_p.dcd sel [atomselect top "resname DPPC and name P"] waitfor all
[atomselect top "resname DPPC and name P" frame 0] writepdb dppc_p.pdb
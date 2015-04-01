#!/usr/bin/env python
# Purpose: Plot time series and histograms of all pairs of dppc P atoms that are initially nearest neighbors
# Syntax: ./dist_dppc.py dppc_p.xyz
# Note: no periodic boundary condition is considered yet


import numpy as np
import scipy 
import sys, string
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt


# Get the number of atoms from xyz file
def get_num_atom ():
    xyzfile = open( sys.argv[1] )
    num_atom = int( xyzfile.readlines()[0] )
    return num_atom


# Collect all coordinate from the same frame into an array
def get_coor_by_frame( framenum ):

    # calculate the row range of the framenum_th frame
    xyzfile = open( sys.argv[1] )
    num_atom = get_num_atom()
    r_unit = num_atom + 2
    r_begin = r_unit * ( framenum -1 ) + 2
    r_end = r_unit * framenum

    # put coordinates of all atoms in framenum_th frame into an array
    xyzfile = open( sys.argv[1] )
    xyzframe = xyzfile.readlines()[r_begin:r_end]
    xyzlist = []
    for line in xyzframe:
        terms = string.split( line )
        xyz = [float( terms[1] ), float( terms[2] ), float( terms[3] )]
        xyzlist.append( xyz ) 
    xyzarray = np.array( xyzlist )
    return( xyzarray )
          

# Find the id's of all the nearest neighboring P pairs at the initial stage (framenum = 1)
def find_id_pairs():
    
    # get coordinate of all atoms in the 1st frame
    coor_frame1 = get_coor_by_frame( 1 )
    
    # use cKDTree to find the neareset neighboring atom pairs
    pair_idlist = []
    for i in enumerate( coor_frame1 ):
        ind1, xyz_ind = i[0], i[1]
        coor_frame1_cp = coor_frame1.copy()
        # avoid self distance calculation
        coor_frame1_cp[ind1] = [np.nan, np.nan, np.nan] 
        tree = cKDTree( coor_frame1_cp )
        dist, ind2 = tree.query( xyz_ind )
        pair_idlist.append( [ind1, ind2] )

    # substitute one of the duplicates using nan
    ttrow = len( pair_idlist )
    for i in xrange( ttrow ):
        id1l, id1r = pair_idlist[i][0], pair_idlist[i][1]
        for j in xrange( ttrow ): 
            id2r = pair_idlist[j][1]
            if id2r == id1l:
                id2l = pair_idlist[j][0]
                if id2l == id1r:  # found duplicate
                    pair_idlist[j] = np.nan, np.nan
    pair_idarr = np.array( pair_idlist )

    # remove nan terms
    pair_idarr2 = pair_idarr[~np.isnan(pair_idarr).any(1)]  
    pair_idarr3 = [ [int(i), int(j)] for i,j in pair_idarr2 ]

    return ( pair_idarr3 )


# Get the total number of frames
def get_num_frame ():
    xyzfile = open( sys.argv[1] )
    ttframenum = 0
    for line in xyzfile:
        if line[0:-1] == ' generated by VMD':
            ttframenum = ttframenum + 1
    return ( ttframenum )


# Process the whole trajectory to get time series of the nearest neighbor distance
def dist_vs_time():
    nnpairlist = find_id_pairs()
    ttframenum = get_num_frame()
    
    # each subarray is for each pair id
    timeseries = np.empty( (len(nnpairlist), ttframenum), dtype=float )

    for framenum in xrange( 1, ttframenum+1 ):
        xyzframe = get_coor_by_frame( framenum )
        for i in xrange( len( nnpairlist )):
            [id1, id2] = nnpairlist[i]
            xyz1, xyz2 = xyzframe[id1], xyzframe[id2]
            dist = np.linalg.norm( xyz1 - xyz2 )
            timeseries[i,framenum-1] = dist
    return ( timeseries )


# Plot timeseries of all nearest neighboring atom pairs
def plot_timeseries():
    
    # row: different pairs of atoms; colume: timeseries for each pair
    data = dist_vs_time()
    time = range( len( data[0] ) )
    time = [ti/100.0 for ti in time]    # unit: ns
    for i in xrange( len(data) ):
        datai = data[i]
        p1 = plt.plot(time, datai)
    plt.show()


# Plot distribution of all nearest neighboring atom pairs
def plot_distribution():
    # row: different pairs of atoms; colume: timeseries for each pair
    data = dist_vs_time()
    for i in xrange( len(data) ):
        datai = data[i]
        plt.hist(datai, bins= range(100), normed=True)
    plt.show()


# Concatenate the distance of all pairs of nearest neighbor atoms and plot
def plot_distribution_concat():
    # row: different pairs of atoms; colume: timeseries for each pair
    data = dist_vs_time()
    data_concat = np.concatenate( data )
    plt.hist(data_concat, bins= range(100), normed=True)
    plt.show()


plot_distribution_concat()








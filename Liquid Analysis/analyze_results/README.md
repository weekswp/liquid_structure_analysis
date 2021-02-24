The first task accomplished by the codes in this directory are accomplished by the `motif_determination.sh` script, which can be created y running the `find_all_motifs.py` file. The most important code for this process is the `find_motifs_single.py` code that extracts motifs from the HDBSCAN groups of a given split group (replicate). For each HDBSCAN group, this code determines which local structure has the LOWEST AVERAGE DISSIMILARITY to the other structures in the group and then extracts this local structure to the `/data/split/#/motifs/` directory where "#" refers to the replicate of interest that is fed into the `find_motifs_single.py` code as an input.

The second task accomplished by this directory is the recombination of the motifs into a final set of local structures, accomplished by running the `transfer_motifs.py` code. After this recombination, we have a valid representative for every local structure in the simulation cell. This file creates two set of files:

1.) A recombined "clusters" directory of the recombined motifs from the different split groups. This is stored in the `../data/Recombined/clusters` directory.

2.) Group trackers for each of these motifs, which keep track of the atoms that each of the structures in the `../data/Recombined/clusters` directory represent. These group trackers are stored in the `../data/Recombined/group_trackers` directory.

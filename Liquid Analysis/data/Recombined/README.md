This directory contains the data for the Recombined analysis and the discussion picks up where we left off in the `data/split` directory.
# Clusters
The `clusters/` directory contains the combined motifs from the various split groups from step 4 of the procedure in the `Liquid Analysis/` directory. Unlike in the split groups, all files are included in this directory and these files are used for the further analysis of the recombined motifs.
# Results
The `results/` directory contains the results of the "final_alignment" process from step 5 of the procedure in the `Liquid Analysis/` directory. Again, unlike in the split systems, all of the data is provided as opposed to a small sample of data.
# Errors
The `errors/` directory contains the results of the "final_errors" process from step 5 of the procedure in the `Liquid Analysis/` directory. Again, unlike in the split systems, all of the data is provided as opposed to a small sample of data.
# Affinities
The `affinities/` directory comtains the results of the "final_analysis" process from step 6 of the procedure in the `Liquid Analysis/` directory. 
# Group Trackers
The `group_trackers/` directory keeps track of the structures that are represented by each of the Recombined motifs where these files are needed for the final "traceback" process in step 7 of the procedure in the `Liquid Analysis/` directory.
# Final_Groups
The `final_groups/` directory contains the files resulting from step step 7 of the provedure in the `Liquid Analysis/` directory. These are the result of the "traceback" process where we use the `group_trackers/` data to determine the structures that each recombined motif represents. In the `final_groups/` directory, there is a file that lines up with each of the HDBSCAN groups in the `affinities/refined_indices` directory with the only difference being that we have traced each of the motifs in these original groups back to those structures that the motifs represent.
#Commonality_Groups
The `commonality_groups/` directory contains the finalized data from which we can calculate the variance. These files are created by carrying out step 8 of the procedure in the `Liquid Analysis/` directoryThe way that this data is calculated is under the premise of a few assumptions:

1.) We start with the largest of the `final_groups/` files and assume that each structure can appear in a group only once (no repeats).

2.) Each structure can only appear in one group. So, if '100.xyz' shows up in a large group, we remove this structure from consideration in all smaller groups. In other words, we assume that each structure should belong to the largest group of which it is a member.

To calculate the variance, we determine the fraction of the system contained in each `commonality_groups/` file and take the mathematical variance of these fractions. Note that we have fewer `commonality_groups/` than `final_groups/` and that this is due to the fact that there are groups in the later directory that only contain structures that have already been seen in more common groups. In this case, the smaller group becomes irrelevant and does not require a file in the `commonality_groups/` directory.

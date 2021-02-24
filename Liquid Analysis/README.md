# Liquid Analysis
This folder goes through implementation examples for the simulated liquid analysis of a Cu-Zr alloy. Note that this analysis could similarly be performed for any other Cu-Zr alloy or an alloy from a completely separate system so long as the parameters marked in the codes are changed accordingly.

## Directories
The `data/` directory is where the outputs of the analysis will be stored. The other directories will all be used to help organize the codes necessary for the analysis

## Procedure:
0.) Start with a large xyz file such as that in the 'create_clusters' directory. Follow `create_clusters/clusters.sh` workflow by running `create_clusters/generate_clusters_for_alignment.py` with the filename as an input. (See `create_clusters/` folder for additional details)

1.) Split the clusters resulting from the previous step into randomly selected groups of 1000 atoms by running `split_clusters.py` in `split_clusters/` directory. The data resulting from this analysis is stored in `data/split/#/clusters/` where "#" corresponds to a particular split group number.

2.) Next, we need to run `alignment/align_clusters.py` on each structure in each split group followed by `alignment/extract_errors.py` on each of the resultant results files. In order to perform this analysis, run `alignment/write_shells.py` followed by `alignment/run_all.sh`.

3.) Once we have this data, the initial PPM alignment is complete. Now, we need to run `clustering/cluster_all.sh` where this shell file runs `clustering/create_affinities.py`, `clustering/clustering.py`, and `clustering/refine_labels.py` on each of the split sets. (See `clustering/` folder for additional details.)

4.) After step 3, we have grouped the structures in each split set into groups that are "similar enough to one another to be considered the same" through the use of the HDBSCAN clustering algorithm. Now, we need to determine the motifs for each of these HDBSCAN groups by running the `motif_determination.sh` script in the `analyze_results/` directory. Next, we need to perform the "recombination" by running the `transfer_motifs.py` code in the `analyze_results/` directory.

5.) Now that the motifs have been "recombined" into a single set, we need to perform one more set of alignments on these motifs by executing the `alignment/final_alignment.sh` script followed by one more set of error extractions on the aligned results by executing the `alignment/final_errors.sh` script.

6.) Once the final errors are created, we need to perform the final affinity creation and HDBSCAN analysis on these results by running the `clustering/final_clustering.sh` script.

7.) Once we have these affinties created, we can use the data in `data/Recombined/group_trackers` to traceback the recombined motifs to the structures that they represent. To perform this analysis, we run the `final_analysis/traceback_groups.py` code with these finalized groups being stored in the `data/Recombined/final_groups` directory.

8.) The last step is to analyze the results in the `data/Recombined/final_groups` directory by running `final_analysis/forced_commonality.py`. This code performs a very specific analysis on the final groupings that is described in the `final_analysis/` directory. We are now done! We can calculate the variance of the group sizes in the `data/Recombined/commonality_groups` directory and this variance should give us important information about the structure. 

# Summary
Note that we started at the beginning with a large simulation cell and now have added additional information about the structure present within this simulation cell. For our purposes, we used this code to analyze the structure of metallic liquids. However, the general framework could be used for any number of applications where one is interested in structural similarity!
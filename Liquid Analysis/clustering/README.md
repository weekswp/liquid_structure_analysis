This directory is run after the alignment and error extraction procedures have been performed. While running the `cluster_all.sh` workflow, it is worth talking about each of codes that are called by this script:

`create_affinities.py`: This file creates "affinity" arrays that essentially combine all of the error arrays into much larger numpy arrays where the `combined_affinity.npy` file contains all of the data and the others contain each fo the four metrics individually. This code is run on all split groups by the `run_affinities.sh` script and the affinity arrays are stored in `../data/split/#/affinities` where "#" corresponds to the split group that we are interested in.

`clustering.py`: This is where the HDBSCAN clustering of the data is performed. We feed in the `combined_affinity.npy` array created above and the preliminary results are stored in the `../data/split/#/affinities/indices` directory. This process is run on all split groups by the `run_clustering.sh` script.

`refine_labels.py`: This code makes the results easier to interpret by renaming the HDBSCAN groupings in a more logical fashion with the results stored in the `../data/split/#/affinities/refined_indices` directory. This process is run on all split groups by the `run_refine.sh` script.

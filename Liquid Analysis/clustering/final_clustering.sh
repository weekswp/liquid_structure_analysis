#!/bin/bash
python create_final_affinities.py
python recombined_clustering.py ../data/Recombined/affinities/combined_affinity.npy
python refine_labels.py ../data/Recombined/affinities/combined_affinity.npy

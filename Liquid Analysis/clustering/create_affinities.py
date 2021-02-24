from path import Path
import json
import joblib
import six
from motifextraction.clustering import create_affinities
from motifextraction.utils import load_cns, get_norm_factors
import sys

#This file pulls together all the error files into "affinity matrices" including the data from all alignments/error extractions.
#Inputs:
#replicate: the split set that we want to create the affinities for.
replicate = sys.argv[1]
if __name__ == "__main__":
    affinity_paths = ['../data/split/'+str(replicate)+'/affinities/L2_affinity.npy',
                      '../data/split/'+str(replicate)+'/affinities/L1_affinity.npy',
                      '../data/split/'+str(replicate)+'/affinities/Linf_affinity.npy',
                      '../data/split/'+str(replicate)+'/affinities/angular_affinity.npy']
    cns = load_cns(Path("../data/split/"+str(replicate)+"/clusters/"))
    nclusters = len(cns)
    error_files = (Path(f'../data/errors/{i}_errors.npy') for i in range(0, nclusters))

    create_affinities(nclusters=nclusters,
                      error_files=error_files,
                      affinity_paths=affinity_paths,
                      cluster_cns=cns,
                      affinities_path='../data/split/'+str(replicate)+'/affinities'
                      )

    norm_dict = {}
    norm_dict["L2"] = get_norm_factors('../data/split/'+str(replicate)+'/affinities/L2_affinity.npy')
    print("Finished loading norm factors for L2.")
    norm_dict["L1"] = get_norm_factors('../data/split/'+str(replicate)+'/affinities/L1_affinity.npy')
    print("Finished loading norm factors for L1.")
    norm_dict["Linf"] = get_norm_factors('../data/split/'+str(replicate)+'/affinities/Linf_affinity.npy')
    print("Finished loading norm factors for Linf.")
    norm_dict["angular"] = get_norm_factors('../data/split/'+str(replicate)+'/affinities/angular_affinity.npy')
    print("Finished loading norm factors for angular.")
    with open("../data/split/'+str(replicate)+'/norm_factors.json", "w") as f:
        json.dump(norm_dict, f, indent=2)

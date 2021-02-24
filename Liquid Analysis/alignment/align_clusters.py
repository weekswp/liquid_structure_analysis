import sys
from path import Path
from natsort import natsorted
from motifextraction.alignment import run_alignments
replicate = sys.argv[2]

##FILE: This file performs PPM alignments of all atoms in a group relative to some local structure. Each run must be provided with inputs of the structure we are
#aligning to and the split replicate in which we want to perform these alignments.

#Inputs:
#cluster_number corresponds to the cluster that we are performing the alignment with respect to.
#
#Parameters:
#model_files used to store the cluster filed that the alignment needs to be performed on.
#target_files used to reference the input cluster number. This method will align all files in model_files to the target_files object.
#**Other parameters define save directories and locations of files with Path objects.
#
#Returns: result of "run_alignments" call.
def align_all_to(cluster_number):
    save_dir = Path('../data/split/'+str(replicate)+'/results')
    clusters_path = Path('../data/split/'+str(replicate)+'/clusters')
    xyz_files = natsorted(clusters_path.glob("*.xyz"))
    model_files = xyz_files
    target_files = [xyz_files[cluster_number]]
    print(target_files)
    assert len(model_files) > len(target_files)
    run_alignments(target_files=target_files, model_files=model_files, save_dir=save_dir)


def main():
    cluster_number = int(sys.argv[1])
    align_all_to(cluster_number)


if __name__ == '__main__':
    main()

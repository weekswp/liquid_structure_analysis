import sys
from path import Path

from motifextraction.alignment import extract_errors

##FILE COMMENTS: This file is used to extract error data from the results file for a given local structure.
# Each run of this file requires an input of the results file we want to extract errors from and the cutoff for the alignment.
# Note that this file is intended to be run after the recombination process.

#Inputs: NONE
#
#Parameters: 
#cutoff was defined as the first valley in the pair distribution function for the original simulation.
#**Other parameters lead to save and cluster directories for the data.
#
#Returns: results of "extract_errors" call.
def main():
    results_fn = Path(sys.argv[1])
    cutoff = float(sys.argv[2])
    cluster_number = int(results_fn.name.split('.')[0])
    extract_errors(cluster_number=cluster_number,
                   results_fn=results_fn,
                   save_dir=Path("../data/Recombined/errors/"),
                   cluster_dir=Path("../data/Recombined/clusters/"),
                   cutoff=cutoff)


if __name__ == '__main__':
    main()
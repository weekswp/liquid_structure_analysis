This folder contains the files used for the alignment of local structures (`align_clusters.py`) and the extraction of errors from the resultant files (`extract_errors.py`).
See the individual parameters for comments describing the parameters that should be changed depending upon the application. The results files from `align_clusters.py` and the error files from `extract_errors.py` are stored in `../data/split/#/results` and `../data/split/#/errors`, respectively.

The other codes in this directory are for the "final_alignment" and "final_error_extraction" processes from step 5 of the procedure in the `Liquid Analysis/` directory. The `final_alignment.sh` and `final_errors.sh` perform the proper analyses where the data is stored in `../data/Recombined/results` and `../data/Recombined/errors`, respectively. Note that one could run the `final_alignment_shell.py` code to create shell files accurate to their particular system.


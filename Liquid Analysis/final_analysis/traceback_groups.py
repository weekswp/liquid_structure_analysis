import os
from path import Path

#This file serves to traceback the motifs in each of the final HDBSCAN groups to the structures that each of them represent
#and then saves group files that contain these represented atoms as opposed to just the motifs in the save_doir location.
refined_dir = Path('../data/Recombined/affinities/refined_indices')
tracker_dir = Path('../data/Recombined/group_trackers')
save_dir = Path('../data/Recombined/final_groups')

#Read in the motifs for a given HDBSCAN group and return
def read_group(group):
    os.chdir(refined_dir)
    group_members = []
    with open(group,"r") as group_file:
        group_file.readline()
        line = group_file.readline()
        while line != "":
            group_members.append(int(line))
            line = group_file.readline()
        group_file.close()
    return group_members

#Traceback to original groups that the motifs came from and create file containing all atoms in these groups.
def traceback_group(group_array,group_identifier):
    os.chdir(tracker_dir)
    data = "Finalized group "+str(group_identifier)+"\n"
    for group in group_array:
        filename = str(group)+".txt"
        with open(filename,"r") as old_group:
            old_group.readline()
            line = old_group.readline()
            while line != "":
                data += line
                line = old_group.readline()
            old_group.close()
    os.chdir(save_dir)
    with open(group_identifier,"w") as final_group:
        final_group.write(data)
        final_group.close()
    os.chdir(refined_dir)

#Main body
def main():
    os.chdir(refined_dir)
    for file in os.listdir(refined_dir):
        group_members = read_group(file)
        traceback_group(group_members,file)

if __name__=='__main__':
    main()



import os
import openpyxl as op
import numpy as np
import scipy.stats
import sys
from path import Path

final_group_dir = Path('../data/Recombined/final_groups')
commonality_dir = Path('../data/Recombined/commonality_groups')

#Create dict object containing each HDBSCAN group (keys) and associated recmobined motifs (values)
def create_group_dictionary():
    original_dict = {}
    os.chdir(final_group_dir)
    #Iterate through all groups
    for file in os.listdir(final_group_dir):
        local_array = []
        #Within each group, add the atoms to an array
        with open(file,"r") as in_file:
            in_file.readline()
            line = in_file.readline()
            while line != "":
                next_atom = int(line)
                local_array.append(next_atom)
                line = in_file.readline()
        #Store an item in the dictionary associating each file with the atoms it contains.
        original_dict[file]=local_array
    return original_dict

#Create dict object containing each HDBSCAN group (keys) and the number of motifs associated with each (values)
# Returns sorted dictionary with largest HDBSCAN group first. 
def populate_combined_dictionary():
    group_counter = {}
    sorted_groups = []
    os.chdir(final_group_dir)
    for file in os.listdir(final_group_dir):
        local_count = 0
        found_atoms = []
        with open(file,"r") as in_file:
            in_file.readline()
            line = in_file.readline()
            while line != "":
                #The following if statement is what makes sure we haven't seen a given structure before.
                if int(line) not in found_atoms:
                    local_count += 1
                    found_atoms.append(int(line))
                line = in_file.readline()
            in_file.close()
        group_counter[file]=local_count
        print(str(file)+" found to contain "+str(local_count)+" atoms")
    #Extract most common group and iterate until none left.
    while bool(group_counter) == True:
        most_common = find_max(group_counter)
        sorted_groups.append(most_common)
        del group_counter[most_common]
    return sorted_groups
    
#Create commonality_groups by sorting through the dictionaries and keeping track of the structures that we have already seen.
def shrink_clusters_common():
    working_dictionary = create_group_dictionary()
    sorted_groups = populate_combined_dictionary()
    observed_atoms = []
    new_working_dict = {}
    #This for loop makes sure that we start by looking at the largest HDBSCAN group by looking at the sorted_groups array.
    for i in range(len(sorted_groups)):
        target_list = working_dictionary[sorted_groups[i]]
        local_list = []
        for atom in target_list:
            #This if...else combination takes care of "duplicates" or structures that have already been seen.
            if atom in observed_atoms:
                pass
            else:
                local_list.append(atom)
                observed_atoms.append(atom)
        #This if statement only activated if no atoms were found. This corresponds to the groups that end up without a file in the
        #commonality_groups directory.
        if len(local_list) == 0:
            print("Group "+str(sorted_groups[i])+" list empty")
        else:
            print(sorted_groups[i])
            new_working_dict[sorted_groups[i]] = local_list
    working_copy = {}
    for group,atoms in new_working_dict.items():
        working_copy[group] = int(len(atoms))
    resorted_groups = []
    while bool(working_copy) == True:
        group = find_max(working_copy)
        resorted_groups.append(group)
        del working_copy[group]
    print(resorted_groups)
    os.chdir(commonality_dir)
    for group in new_working_dict.keys():
        with open(group,"w") as in_file:
            in_file.write("Group "+group+" condensed by commonality!\n")
            atoms = new_working_dict[group]
            for i in range(len(atoms)):
                in_file.write(str(atoms[i])+"\n")
            in_file.close()
    return resorted_groups

#Used to find the largest item in the dictionary. Used by the populate_combined_dictionary() method.
def find_max(dictionary):
    largest = 0
    largest_group = ""
    for group, number in dictionary.items():
        if number > largest:
            largest = number
            largest_group = group
    return largest_group

if __name__ == '__main__':
    shrink_clusters_common()

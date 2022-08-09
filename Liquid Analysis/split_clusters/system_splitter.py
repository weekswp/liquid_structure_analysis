import os
import shutil
import random
from path import Path
original_cluster_dir = Path('../data/original_clusters/clusters')
split_dir = Path('../data/split/')

#Purpose: takes randomly selected cluster files and puts them into split directories of max size "split_size"
#
#Inputs: NONE
#
#Parameters:
#size: length of original clusters directory.
#split_size: number of structures we want in each group
#limit: dependent upon size and split_size parameters and tells us how many folders we are going to have.
#new_allocation: keeps track of the result from the run of copy_set() local to the current iteration of the for loop.
#
#Returns: NONE
def main():
    size = len(os.listdir(original_cluster_dir))
    #split_size can be changed to another value if desired.
    split_size = 1000
    limit = (size/1000)+1
    unallocated_atoms = []
    for i in range(size):
        unallocated_atoms.append(i)
    for j in range(1,limit):
        os.chdir(split_dir)
        if os.path.isdir(str(j)) == False:
            os.mkdir(str(j))
        os.chdir(str(j))
        if os.path.isdir("data") == False:
            os.mkdir("data")
        os.chdir("data")
        if os.path.isdir("clusters") == False:
            os.mkdir("clusters")
        #Calls copy_set() function and resets the unallocated_atoms array to the returned array from copy_set().
        #In this way, we can make sure that those structures selected and copied are removed from consideration in future folders.
        new_allocation = copy_set(size,unallocated_atoms,j)
        unallocated_atoms = new_allocation
    os.chdir(split_dir)

#Purpose: Randomly select at most split_size(1000) atoms from original_cluster_dir and move to copy to the appropriate split directory.
#
#Inputs:
#size: input from select_files() that defined how many initial clusters we had.
#split_size: input from select_files() that defines how big we want our randomly selected groups to be.
#unallocated_atoms: keeps track of atoms that have not been selected from previous sets.
#rep: split group number that we want to save the files to. (i.e., would be 2 if we are selecting for the second split group).
#
#Parameters:
#start_count: keeps track of how many clusters have already been selected.
#current_unallocated: total number of unallocated structures that still need to be assigned.
#selection: makes random selection from unallocated_atoms array.
#local_count: keeps track of number of structures that we have appropriately renamed within the new split directory.
#
#Returns:
#unallocated_atoms: The new unallocated list is returned and is, at most, split_size smaller than the input array.
def copy_set(size,split_size,unallocated_atoms,rep):
    start_count = (rep*split_size) - split_size
    for i in range(start_count,start_count+split_size):
        if i < size:
            current_unallocated = len(unallocated_atoms)
            selection = unallocated_atoms[random.randint(0,current_unallocated-1)]
            #Copies random selection from original to new location and remove the selection from the unallocated_atoms array
            #so that it isn't selected again.
            filename = str(selection)+".xyz"
            source = str(original_cluster_dir)+"/"+filename
            destination = str(split_dir)+"/"+str(rep)+"/data/clusters/"+"old_"+filename
            shutil.copy(source,destination)
            unallocated_atoms.remove(selection)
    os.chdir(str(split_dir)+"/"+str(rep)+"/data/clusters")
    local_count = 0
    #renames files in split cluster directory
    for file in os.listdir(os.getcwd()):
        filename = str(file)
        new_name = str(local_count)+".xyz"
        os.rename(filename,new_name)
        local_count += 1
    return unallocated_atoms

if __name__=='__main__':
    main()


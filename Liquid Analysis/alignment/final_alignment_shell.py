import os
from path import Path
recombined_cluster_dir = Path("../data/Recombined/clusters")
length = len(os.listdir(recombined_cluster_dir))
data = "#!/bin/bash\n"
for i in range(length):
    data += "python final_align_clusters.py "+str(i)+"\n"
with open("final_alignment.sh",'w') as out_file:
    out_file.write(data)
    out_file.close()
data = "#!/bin/bash\n"
for i in range(length):
    data += "python final_extract_errors ../data/Recombined/"+str(i)+".xyz.json 3.7\n"
with open("final_errors.sh",'w') as out_file:
    out_file.write(data)
    out_file.close()

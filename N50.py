import sys
import os
import re

# get the contig fasta file
from typing import Dict

if len(sys.argv) < 2:
    ctg_fa = str(input("Enter the contig fasta file:\n"))
else:
    ctg_fa = sys.argv[1]

# check the input file
if not os.path.isfile(ctg_fa):
    print("MSG: No contig fasta file!\nPlease take a look the usage.")
    exit()

if not str.endswith(ctg_fa, '.fa') and not str.endswith(ctg_fa, '.fasta'):
    print("MSG: The contig fasta file is wrong name!\nPlease take a look the usage.")
    exit()

print("MSG: contig fasta file:", ctg_fa)

# open contig fasta file
# ctg_seqlen = {}
ctg_seqlen: Dict[str, int] = {}
ctgid_num = {}
with open(ctg_fa,'r') as f:
    for line in f:
        line = line.strip('\n')
        ctg_idre = re.search(r"^>(.+) Myxosarcina .+ GI1 (contig_\d+)", line)
        ctg_id: str

        if ctg_idre:
            # print(ctg_idre.group(1))
            ctgid_num[ctg_idre.group(1)] = ctg_idre.group(2)
            ctg_id = ctg_idre.group(1)
            # print(ctg_id)
            ctg_seqlen[ctg_id] = 0
        else:
            # print(line)
            ctg_seqlen[ctg_id] += int(len(line))
f.close()

print(ctg_seqlen)
#for key, value in ctg_seq.items():
#    ctg_seqlen[key] = len(value)


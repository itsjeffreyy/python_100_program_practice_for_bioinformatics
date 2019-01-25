import sys
import os

# get the fastq file name
fqfn = ""
if len(sys.argv) > 1:
    fqfn = sys.argv[1]
else:
    fqfn = str(input("Please enter fastq: "))

# check fastq file name and whether the file isexcite
if not fqfn.endswith('.fq') and not fqfn.endswith('.fastq'):
    print("ERR: The fastq file name is wrong!")
    print("MSG: The file name should end with \".fq\" otr \".fastq\"")
    exit()
elif not os.path.isfile(fqfn):
    print("ERR: The fastq file " + fqfn + " does not excite!")
    exit()
print("The fastq file is:", fqfn)

# open fastq file
fq = open(fqfn)
fq_len = len(fq.readlines())
fq.close()

# check the line number is correct
if fq_len % 4 != 0:
    print("ERR: Fastq file "+fqfn+ " is not fastq format!")
    exit()

# count how many reads
reads_number = fq_len/4
print("Fastq", fqfn ,"reads counts:", int(reads_number))
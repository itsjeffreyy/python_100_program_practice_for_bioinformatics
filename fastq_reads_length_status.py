#!/usr/bin/env python
# author: Jeffreyy C.H. Yu
# Note: Calculate the number of the read length and the average read length of the fastq file.
# usage: `python fastq_reads_length_status.py` or `python fastq_reads_length_status.py your_fastq.fq`.
#
import sys
import os

def load_fq():
    fqfn = ''
    if len(sys.argv) > 1:
        fqfn = sys.argv[1]
    else:
        fqfn = str(input("Please enter the fastq:"))

    return fqfn

def check_fq(fqfn):
    # check the file name and exist
    fqfn = str(fqfn)
    if not fqfn.endswith('.fq') and not fqfn.endswith('.fastq'):
        print("ERR: The fastq file name is wrong!")
        print("MSG: The file name not end with \".fq\" otr \".fastq\"")
        exit()
    elif not os.path.isfile(fqfn):
        print("ERR: The fastq file " + fqfn + " does not excite!")
        exit()

    # check the file lines
    fq = open(fqfn,'r')
    fq_lines_len = len(fq.readlines())
    fq.close()

    if fq_lines_len % 4 != 0:
        print("ERR: Fastq file "+fqfn+ " is not fastq format!")
        exit()

    print("The fastq file is:", fqfn)
    return fqfn

def collect_fq_len(fqfn):
    fq = open(fqfn,'tr')
    fq_line_num = len(fq.readlines())
    fq.close()

    reads_lens_number = {}
    fq = open(fqfn,'r')
    for i in range(0, fq_line_num, 4):
        t1 = (fq.readline()).strip('\n')
        seq = (fq.readline()).strip('\n')
        t2 = (fq.readline()).strip('\n')
        qs = (fq.readline()).strip('\n')

        if len(seq) not in reads_lens_number.keys():
            reads_lens_number[len(seq)] = 0

        reads_lens_number[len(seq)] += 1
    fq.close()
    return(reads_lens_number)

def main():
    fqfn = load_fq()
    fqfn = check_fq(fqfn)
    reads_lens_number = collect_fq_len(fqfn)

    # print
    total_nuc = 0
    print("reads_length (bp)\tnumber")
    for i in reads_lens_number.keys():
        print(str(i) + "\t" + str(reads_lens_number[i]))
        total_nuc += i * reads_lens_number[i]

    # average
    total_reads = sum(reads_lens_number.values())
    average_reads_len = total_nuc / total_reads
    print("Total reads number:",total_reads)
    print("average reads length (bp):",average_reads_len,)


###########
main()
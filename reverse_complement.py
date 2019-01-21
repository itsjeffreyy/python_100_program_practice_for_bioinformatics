# author: Jeffreyy C.H. Yu
# note: The script function is reserve complement DNA sequence.
# usage: `python reverse_complement.py` or `python reverse_complement.py your_seq`
import sys

# get the sequence
if len(sys.argv) > 1:
    seq = sys.argv[1]
else:
    seq = str(input("Please enter your sequence: "))

# do the complement
table = str.maketrans('ATCGatcg','TAGCtagc',)
c_seq = seq.translate(table)

# do reverse
rc_seq = c_seq[::-1]
print("original sequence:\n" + seq)
print("reverse complement sequence:\n" + rc_seq)


# complement = {"A":"T", "T":"A", "G":"C", "C":"G", "a":"t", "t":"a", "c":"g", "g":"c"}
#for i in seq:
#    complete_seq = complement[i]
#print(complement_seq)
#parser setup
import sys
import argparse
parser = argparse.ArgumentParser()
parser.prog = 'progName.py'
parser.description = 'You can provide the program with three parameters through the terminal'
parser.add_argument("-n", type=int, help='Number of integration regions generated')
parser.add_argument("-r", type=int, help='Range-value: defines an interval where the IR is located')
parser.add_argument("-d", type=int, help='Delta-value: expands the range with the value provided by user')
#add new input argument
parser.add_argument("-i", help='Input-file .txt with names of chromosomes and their lengths in bp organized into two columns and separated by \t')
namespace = parser.parse_args((sys.argv[1:]))
dimension_dict = {}
with open(namespace.i) as dimension_file:
    for line in dimension_file:
        key, value = line.split("\t")
        dimension_dict[key.strip()]=int(value.strip())
    dimension_file.close()
#loop on n random IR
import random
count = 1
print "chr#", '\t', 'Start', '\t\t', 'End', '\t\trnd#'
for i in range(namespace.n):
    #select a chromosome
    chrom = random.choice(dimension_dict.keys())

    #select a site on that chromosome
    start = random.randint(1,dimension_dict[chrom])

    #select a random region
    end = start + random.randint(0,namespace.r) + namespace.d
    if len(str(chrom))==1:
        print chrom,'',"\t",start,"\t",end,"\trnd{}".format(count)
    else:
        print chrom,"\t",start,"\t",end,"\trnd{}".format(count)
    count +=1
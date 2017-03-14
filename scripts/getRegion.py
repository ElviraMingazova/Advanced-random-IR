import sys
import argparse
parser = argparse.ArgumentParser()
parser.prog = 'progName.py'
parser.description = 'You can provide the program with three parameters through the terminal'
parser.add_argument("-n", type=int, help='Number of integration regions generated')
parser.add_argument("-r", type=int, help='Range-value: defines an interval where the IR is located')
parser.add_argument("-d", type=int, help='Delta-value: expands the range with the value provided by user')

#input parsing
namespace = parser.parse_args((sys.argv[1:]))
#create a dictionary for the chromosoms lengths
import random
chrLen = {}
chrLen[1]=224999719
chrLen[2]=237712649
chrLen[3]=194704827
chrLen[4]=187297063
chrLen[5]=177702766
chrLen[6]=167273993
chrLen[7]=154952424
chrLen[8]=142612826
chrLen[9]=120312298
chrLen[10]=131624737
chrLen[11]=131130853
chrLen[12]=130303534
chrLen[13]=95559980
chrLen[14]=88290585
chrLen[15]=81341915
chrLen[16]=78884754
chrLen[17]=77800220
chrLen[18]=74656155
chrLen[19]=55785651
chrLen[20]=59505254
chrLen[21]=34171998
chrLen[22]=34893953
chrLen[23]=151058754
chrLen[24]=57741652
count = 1
#loop on n random IR
print "chr#", '\t', 'Start', '\t\t', 'End', '\t\trnd#'
for i in range(namespace.n):
   #select a chromosome
   chrom = random.randint(1,24) #the name "chrom" was chosen because "chr" is a built-in function

   #select a site on that chromosome
   start = random.randint(1,chrLen[chrom])

   #select a random region
   end = start + random.randint(0,namespace.r) + namespace.d
   if len(str(chrom))==1:
       print "chr{}".format(chrom),'',"\t",start,"\t",end,"\trnd{}".format(count)
   else:
       print "chr{}".format(chrom),"\t",start,"\t",end,"\trnd{}".format(count)
   count +=1
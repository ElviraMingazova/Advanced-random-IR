
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

#a function that proves whether the input file contains  two columns
def checkFormatting():
    check=True
    with open(namespace.i) as dimension_file:
        #go through all of the lines and check whether exactly two columns are present
        for line in dimension_file:
            result=line.split()
            if len(result)==2:
                continue
            else:
                print 'Checking format: the text file has to contain two columns'
                check=False
                break
    dimension_file.close()
    if check == True:
        print "Checking format: the file is well formatted"
    return check

#a function that proves whether the first column contains a string "chrXY" where X and Y are digits
def checkColumn1():
    check = True
    #use regEx
    import re
    #save a regEx pattern matching "chrXY" where XY are digits
    pattern = re.compile('(chr\d\Z|chr\d\d\Z)',re.IGNORECASE)
    with open(namespace.i) as dimension_file:
        column1=[]
        lines=dimension_file.readlines()
        for line in lines:
            column1.append(line.split()[0].strip())
        for word in column1:
            if re.match(pattern,word):
                continue
            else:
                print "Checking the first column: {} is not a chromosome name".format(word)
                check = False
                break
        if check == True:
            print "Checking the first column: the names of chromosomes are correct"
    dimension_file.close()
    return check
    
#a function that proves whether the second column contains a positive integer
def checkColumn2():
    check = True
    with open(namespace.i) as dimension_file:
        column2=[]
        lines=dimension_file.readlines()
        for line in lines:
            try:
                #extract the second column to a list and try to convert each element into an integer
                column2.append(int(line.split()[1].strip()))
            #catch a ValueError: invalid literal for int()
            except ValueError:
                check = False
                print "Checking the second column: could not convert {} to an integer".format(line.split()[1].strip())
    dimension_file.close()
    if check == True:
        for length in column2:
            if length<0:
                print "Checking the second column: you provided a negative chromosome length: {}".format(length)
                check = False
    if check == True:
        print "Checking the second column: the lengths of chromosomes are correct"
    return check

#check the input file    
check=checkFormatting()
if check==True:
    check=checkColumn1()
    if check==True:
        check=checkColumn2()
        if check == True:
            
    
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
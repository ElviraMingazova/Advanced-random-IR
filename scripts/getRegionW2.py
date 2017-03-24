#parser setup
def parseArgs():
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
    return namespace
#a function that proves whether the input file contains  two columns
def checkFormatting():
    check=True
    #go through all of the lines and check whether exactly two columns are present
    for line in dimension_file:
        result=line.split()
        if len(result)==2:
            continue
        else:
            print 'Checking format: the text file has to contain two columns'
            check=False
            break
    if check == True:
        print "Checking format: the file is well formatted"
    return check

#a function that proves whether the first column contains a string "chrXY" where X and Y are digits
def checkColumn1():
    check = True
    column1=[]
    for line in dimension_file:
        if line.split()[0].strip() not in column1:
            column1.append(line.split()[0].strip())
        else:
            print "Checking the first column: one of the chromosome names is duplicated"
            check = False
            break
    if check == True:
        print "Checking the first column: the names of chromosomes are correct"
    return check
    
#a function that proves whether the second column contains a positive integer
def checkColumn2():
    check = True
    column2=[]
    for line in dimension_file:
        try:
            #extract the second column to a list and try to convert each element into an integer
            column2.append(int(line.split()[1].strip()))
        #catch a ValueError: invalid literal for int()
        except ValueError:
            check = False
            print "Checking the second column: could not convert {} to an integer".format(line.split()[1].strip())
    if check == True:
        for length in column2:
            if length<0:
                print "Checking the second column: you provided a negative chromosome length: {}".format(length)
                check = False
    if check == True:
        print "Checking the second column: the lengths of chromosomes are correct"
    return check
#a function which will process the given text file and return {"chr name": chr length} pairs inside of a dictionary
def getDimensionDict(filename):
    d={}
    with open(filename) as dimension_file:
        for line in dimension_file:
            key, value = line.split()
            d[key.strip()]=int(value.strip())
        dimension_file.close()
    return d
#the following line will protect the code frome executing if I will import the file as a module
if __name__ == "__main__":
    #check the input file
    namespace = parseArgs()
    f = open(namespace.i,"r")
    dimension_file=f.readlines()
    check=checkFormatting()
    if check==True:
        check=checkColumn1()
        if check==True:
            check=checkColumn2()
            if check == True:
                dimension_dict = getDimensionDict(namespace.i)
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
    f.close()
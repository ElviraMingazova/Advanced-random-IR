#total lengths of the chromosomes
dimension_dict={'chr13': 114364328, 'chr12': 133275309, 'chr11': 135086622, 'chr10': 133797422, 'chr17': 83257441, 'chr16': 90338345, 'chr15': 101991189, 'chr14': 107043718, 'chr19': 58617616, 'chr18': 80373285, 'chr24': 57227415, 'chr22': 50818468, 'chr23': 156040895, 'chr20': 64444167, 'chr21': 46709983, 'chr7': 159345973, 'chr6': 170805979, 'chr5': 181538259, 'chr4': 190214555, 'chr3': 198295559, 'chr2': 242193529, 'chr1': 248956422, 'chr9': 138394717, 'chr8': 145138636}
#dictionaries containing the factors to calculate the number of positions to be generated on the respective chromosome
kmer40={'chr1':0.0788750,'chr2':0.086109,'chr3':0.071728,'chr4':0.068060,'chr5':0.063896,'chr6':0.059406,'chr7':0.053514,'chr8':0.051220,'chr9':0.039697,'chr10':0.046955,'chr11':0.046680,'chr12':0.046712,'chr13':0.035519,'chr14':0.030916,'chr15':0.026443,'chr16':0.025715,'chr17':0.024516,'chr18':0.027496,'chr19':0.017131,'chr20':0.022020,'chr21':0.011919,'chr22':0.011228,'chrX':0.050153,'chrY':0.004092}
kmer100={'chr1':0.079149,'chr2':0.085056,'chr3':0.071048,'chr4':0.067183,'chr5':0.063207,'chr6':0.058915,'chr7':0.053848,'chr8':0.050605,'chr9':0.039585,'chr10':0.046928,'chr11':0.046556,'chr12':0.047077,'chr13':0.034862,'chr14':0.030896,'chr15':0.026539,'chr16':0.026195,'chr17':0.025596,'chr18':0.026942,'chr19':0.019023,'chr20':0.022081,'chr21':0.011808,'chr22':0.011606,'chrX':0.050983,'chrY':0.004312}
kmer200={'chr1':0.079156,'chr2':0.084813,'chr3':0.070927,'chr4':0.067097,'chr5':0.063081,'chr6':0.058819,'chr7':0.053983,'chr8':0.050402,'chr9':0.039582,'chr10':0.046868,'chr11':0.046584,'chr12':0.047115,'chr13':0.034707,'chr14':0.030854,'chr15':0.026544,'chr16':0.026175,'chr17':0.025815,'chr18':0.026807,'chr19':0.019354,'chr20':0.022078,'chr21':0.011794,'chr22':0.011689,'chrX':0.051301,'chrY':0.004455}
import numpy as np
from __future__ import print_function
def getMappableIR(inputf,chr_name,kmer,mapname,N,outputf):
    """Generate N*kmer[chr_name] positions on a respective chromosome using the map of choice, where N is the total number of positions to be generated on the genome"""
    with open(inputf,"r"):
        chr_arr = np.genfromtxt(inputf,dtype=None)
    counter = 1
    while counter<=round(N*kmer[chr_name]):
        rand_num = np.random.randint(1,dimension_dict[chr_name])
        matched_index = np.searchsorted(chr_arr["f0"],rand_num)-1
        if chr_arr["f1"][matched_index] == True:
            #append to the file that has been previously created with headers
            with open(outputf, 'a') as f:
                print (chr_name,"\t",rand_num,"\t",rand_num+1,"\t", "unmatched","\t",mapname,"\t", "hg38", file=f)                    
                counter+=1
        else:
            continue
            
#first write a new file with tables header (example kmer=40, N=100000):            
with open('results/map40_IS100000.txt', 'w') as f:
    print("Chromosome\tStart\tEnd\tMatch\tRnd Model\tAssembly", file=f)
    
listofchr = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22","chrX","chrY"]

#for each chromosome compute the corresponding number of IR and append to the file
for chrom in listofchr:
    getMappableIR('textfiles/map40/{0}_40_mappable.txt'.format(chrom), chrom, kmer40, "map_40", 100000, 'results/map40_IS100000.txt')
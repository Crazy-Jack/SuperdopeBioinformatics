"""
getGeneList.py takes in one argument of PRAS result .txt file and outputs a .txt file of all the genes from PRAS result

Runs with command line "python getGeneList.py inputfile.txt"

Top 5% of the ranked genes are used for GO analysis
"""

import sys

with open(sys.argv[1]) as pras:
    gene_list = [line.split()[0] for line in pras]

gene_list = gene_list[1:(len(gene_list)*0.05)+1]

with open("GeneList.txt","w") as f:
    for gene in gene_list:
        f.write('%s\n' % gene) 


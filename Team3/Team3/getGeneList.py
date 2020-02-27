"""
getGeneList is a function takes in PRAS result .txt file as input and outputs a list of top 5% ranked genes from PRAS result

Top 5% of the ranked genes are used for GO analysis
"""

def getGeneList(filename):
    with open(filename) as pras:
        gene_list = [line.split()[0] for line in pras]
    
    gene_list = gene_list[1: int(len(gene_list)*0.05)+2]
    

    return gene_list


"""
getGeneList is a function takes in PRAS result .txt file as input and outputs a .txt file of the top 5% ranked gene list from PRAS result

Top 5% of the ranked genes are used for GO analysis
"""

def getGeneList(filename, save_dir, percent=0.05):
    try:
        with open(filename) as pras:
            gene_list = [line.split()[0] for line in pras]

        gene_list = gene_list[1: int(len(gene_list)*percent)+2]

        gene_list_loc = save_dir + "/"+ "Top" + str(percent*100) + "percentGeneList.txt"

        with open(gene_list_loc, "w") as f:
            for gene in gene_list:
                f.write('%s\n' % gene)
        return gene_list_loc
    except Exception as e:
        print("GO getGeneList Error: ", e)






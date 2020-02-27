#for enrichment of those gene pick out by the correlation between WER and background gene's expression
library(DOSE)
library(clusterProfiler)
library(ReactomePA)
library(enrichplot)
library(topGO)
library(Rgraphviz)

args <- commandArgs(TRUE)
gene.name.file <- args[1]
GOresults.file <- paste(gene.name.file, "GOresults.txt", sep=".")
GOresults.dotpot.file <- paste(GOresults.file, "img-dotplot.pdf",sep=".")
GOresults.plotGOgraph.file <- paste(GOresults.file, "img-topplot.pdf",sep=".")
GOresults.enrich.file <- paste(GOresults.file, "img-enrich.pdf",sep=".")
Keggresults.file <- paste(gene.name.file, "KEGGresults.txt", sep=".")
ReactomeResults.file <- paste(gene.name.file, "ReactomeResults.txt", sep=".")


# enrich.file <- read.table("D:\\zengyr\\m6Aø\\plot_somedata\\Replot_All_m6ACancer\\GenesetEnrichment_WERs_cytoscape\\for_enrichment.txt",header=F)
enrich.file <- read.table(gene.name.file, header=F)
enrich.genes <- as.character(enrich.file$V1)

entrez.genes <- bitr(enrich.genes,fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")


# first, for GO enrichment, just need BP
GO.enrich <- enrichGO(gene     = entrez.genes$ENTREZID,
                      ont      = "BP",
                      readable = TRUE,
                      OrgDb    = "org.Hs.eg.db",
                      pvalueCutoff = 0.01,
                      pAdjustMethod = "fdr",
                      qvalueCutoff = 0.05)

# plot dot plot for GO
pdf(GOresults.dotpot.file)
dotplot(GO.enrich,  showCategory=30)
dev.off()



# plot top plot
pdf(GOresults.plotGOgraph.file)
plotGOgraph(GO.enrich)
dev.off()

write.table(GO.enrich,
            file = GOresults.file,
            quote=F,row.names=F,sep="\t")

# enrichment map
pdf(GOresults.enrich.file)
cnetplot(GO.enrich, categorySize="pvalue", foldChange=as.character(enrich.file$V1))
dev.off()

# second, for KEGG enrichment
KEGG.enrich <- enrichKEGG(gene = entrez.genes$ENTREZID,
                          organism = "hsa",
                          pAdjustMethod = "fdr",
                          use_internal_data = T,
                          pvalueCutoff = 0.05)  # using external data may be more accurate.
write.table(KEGG.enrich,
            file = Keggresults.file,
            quote=F,row.names=F,sep="\t")
# change entrez to symbol and re-write them into the same file
change.df <- read.table(Keggresults.file,
                        header=T,stringsAsFactors=F,sep="\t")
rnames <- rownames(change.df)
for (name in rnames) {
  map.symbol <- c()
  entrez.list <- as.character(change.df[name,"geneID"])
  each.entrez <- strsplit(entrez.list,"/")
  for (entrez in each.entrez[[1]]) {
    symbol <- entrez.genes[which(entrez.genes$ENTREZID==entrez),"SYMBOL"]
    map.symbol <- c(map.symbol,symbol)
  }
  symbol.list <- paste(map.symbol,sep="",collapse="/")
  # print(symbol.list)
  change.df[name,"geneID"] <- symbol.list
}
write.table(change.df,
            file = Keggresults.file,
            quote=F,row.names=F,sep="\t")

# third, reactome pathway enrichment
Reactome.enrich <- enrichPathway(entrez.genes$ENTREZID,
                                 organism = "human",
                                 pvalueCutoff = 0.05,
                                 pAdjustMethod = "fdr",
                                 readable = T)

write.table(Reactome.enrich,
            file = ReactomeResults.file,
            quote=F,row.names=F,sep="\t")






### 
ncg <- enrichNCG(entrez.genes)




is.normal <- function (h) {
  if ("." %in% unlist(strsplit(h, "")) | "-" %in% unlist(strsplit(h, ""))) {
    return (F)
  } else {
    return (T)
  }
}

n <- c()
for (i in 1:length(enrich.genes)) {
  if (is.normal(enrich.genes[i])) {
    n <- c(n, enrich.genes[i])
  }
}






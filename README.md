# Predicting Biochemical Pathways Involving Target RBP

BioPro is a bioinformatics pipeline that processes and analyzes eCLIP data of RNA-binding proteins (RBP) to predict the functional targets of RBP and biological processes to which the functional targets of RBP contributes.

BioPro pipeline cleans raw eCLIP data of a target RBP with Cutadapt and aligns the RNA sequence with STAR. Peak calling is then performed with PureCLIP. Then, based on the peaks, PRAS predicts the functional target genes of RBP and produces a ranked gene list. The pipeline then performs gene ontology (GO) analysis on the top 5% ranked genes to predict the biological processes. 


## Install

### Install via source code

To install via source code, clone our github repo and run:

```
git clone https://github.com/Crazy-Jack/SuperdopeBioinformatics
bash install.sh
```


### Install via pip

Or you can directly install our software from pip:

`pip install BioPro`

Our package can be found at: https://pypi.org/project/BioPro/


## Attribution

This project is created as a course project for Bioinformatics. All memebers of our team contributed equally to the final product. Great thanks to Tianqin Li, Zeyuan Zuo, Jui-Chia Chung, Snigdha Agarwal and SerenaAbraham. 

## Maintainance

Tianqin Li (jacklitianqin@gmail.com)

Carnegie Mellon University

Pittsburgh, PA, 15213, US.


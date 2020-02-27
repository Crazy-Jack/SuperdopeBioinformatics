pip3 install -e Team3

## PRAS setup commands
wget https://github.com/ouyang-lab/PRAS/blob/master/zipped_code/script.zip
unzip script.zip
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/gtfToGenePred
chmod +x gtfToGenePred
futurize -w script/PRAS_1.0.py
futurize -w script/extract_genomic_regions.py
futurize -w script/genepred2PRAS.py
wget https://github.com/arq5x/bedtools2/releases/download/v2.29.2/bedtools.static.binary
mv bedtools.static.binary bedtools
chmod a+x bedtools
PATH="$PATH:$(pwd)"
cd script

import subprocess
import argparse
import signal
#import cutadapt_fastuniq as cf
from cutadapt import CutAdapt
from pureclip import PureClip
from star import STAR
from samtools import SAM
from go_analysis import GO
from pars import PARS


"""
Sample data test from ENCODE project has passed
"""
######################################
## Begin OF configuration of Paramters##
######################################

# -------------------------This part is for GLOBAL parameter -------------------------
# SECTION-1: create argparse structures for final software input and output.

# Create a parser
parser = argparse.ArgumentParser(
    description="Command line for cutadapt.")

# Create argument for the first input file
parser.add_argument("input_file1", type=str, help="Paired end 1 fastq file")

# Create argument for second input file
parser.add_argument("input_file2", type=str, help="Paired end 2 fastq file")

# Create argument for genome reference file
parser.add_argument("reference_genome", type=str,
                    help="Input for the reference genome")

# Creat argument for first output file
parser.add_argument("outputFiles1", type=str, help="Name of first output file")

# Creat argument for second output file
parser.add_argument("outputFiles2", type=str,
                    help="Name of second output file")

# Intermediate Data stroge
parser.add_argument(
    "-inter", "--intermediate_file", type=str, help="intermediate file storage, default is same dirctory of output file.")


# SECTION-2: create argparse structure for each subsoftware we use.

# SECTION-2.1 Cutadapt

# Create argument for 3' adapter and 5' adapter
parser.add_argument(
    "-a", type=str, help="Trim 3' reads adapter", action='append')
parser.add_argument(
    "-g", type=str, help="Trim 5' reads adapter", action='append')

# Create argument for more adapters of 3' and 5'
parser.add_argument(
    "-A", type=str, help="Second 3' reads adapter", action='append')
parser.add_argument(
    "-G", type=str, help="Second 5' reads adapter", action='append')

# For simplification, I will keep every other parameters the same as process from Yeo's lab.

# SECTION-2.2 STAR
# TODO: build parser structure for STAR, specify which what kind of parameters is needed for STAR related input.


# SECTION-2.3: SAMtools
# TODO: build parser structure for SAMtools, specify which what kind of parameters is needed for SAMtools related input.


# SECTION-2.4: PureClip
# TODO: build parser structure for PureClip, specify which what kind of parameters is needed for PureClip related input.
parser.add_argument("-pcn", '--pureclip-parallel-num',
                    help="pureclip parallelism number")
parser.add_argument("-pcchr", '--pureclip-chr',
                    help="if specificed, then pureclip can have more narrow focus.")

# SECTION-2.5: PRAS
# TODO: build parser structure for PARS, specify which what kind of parameters is needed for PARS related input.
parser.add_argument("-t",'--id_file',type=str, help="Input the ID file. This file has to have two columns, the first column is the transcript ID, and the second column is the gene id or gene name. Please check the instruction page for file example.", action='append')
parser.add_argument("-s",'--pras_region', type=str, help="Input the Genomic region. Comma separated multiple genomic regions are acceptable. For single genomic region, there are five options: '5UTR' is the 5'UTR, 'CDS' is the coding region, '3UTR' is the 3'UTR, 'transcript' is the entire transcript, and 'splice' is for splicing site (SS). If no input provided, PRAS will take the transcript as the default input. As for multiple genomic regions, any combination of '5UTR', 'CDS', and '3UTR' is accepted. 'splice' cannot appear in the multiple genomice region input.")

# SECTION-2.6: GO
# TODO: build parser structure for GO, specify which what kind of parameters is needed for GO related input.


# Get all the arguments
args = parser.parse_args()

# SECTION-2.7: Shared parameters
# TODO: If you need any shared parameters, please include them here. And for minimal redundancy, use the shared param if possible.
share_param = {
    'genome_ref': args.reference_genome,
}

######################################
## End OF configuration of Paramters##
######################################


# SECTION 3: CALL FUNCTIONs

# SECTION 3.1: CutAdapt
# TODO: Define your local parameter dict you want to pass into the class.


cutadapt_param = {
    'input_file1': args.input_file1,
    'input_file2': args.input_file2,
    'adpater_a': args.a,
    'adapter_A': args.A,
    'adapter_g': args.g,
    'adapter_G': args.G,
}

# cf.CallCutadapt(args)
# cf.CallInputlist(args)
# cf.CallFastuniq(args)
cf = CutAdapt(cutadapt_param)
cf.CallCutAdapt()


# SECTION-3.2: Calling STAR
# TODO: Define your local parameter dict you want to pass into the class.
star_param = {
    'output_bam': 'star_output.bam',
}  # MODIFY this

st = STAR(star_param)
st.CallSTAR()


# SECTION-3.3: Calling Samtools
# TODO: Define your local parameter dict you want to pass into the class.
samtool_param = {
    'output_bai': start_param + '.bai'
}  # MODIFY this

sm = SAM(samtool_param)
sm.CallSAM()

# SECTION-3.4: Calling pureclip
# TODO: Define your local parameter dict you want to pass into the class.
# call the functions for commandline
pureclip_param = {
    'reads': star_param['output_bam'],
    'align': samtool_param['output_bai'],
    'genome': share_param['genome_ref'],
    'output_bed': 'pureclip_output.bed',
    'parallel_num': args.pureclip_parallel_num,
    'specific_chromosome': args.pureclip_chr,
}  # MODIFY this

pc = PureClip(pureclip_param)
pc.CallPureClip()


# SECTION-3.5: Calling PRAS
# TODO: Define your local parameter dict you want to pass into the class.

pras_param = {
	'annot_file':star_param['annot_file'],
	'id_file':args.id_file,
	'region':args.pras_region,
	'input_file':pureclip_param['output_bed']
}


# SECTION-3.6: Calling GO
# TODO: Define your local parameter dict you want to pass into the class.
go_param = {}  # MODIFY this
go = GO(go_param)
go.CallGO()

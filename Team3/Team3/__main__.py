import subprocess
import argparse
import signal
import cutadapt_fastuniq as cf
from pureclip import PureClip



"""
Sample data test from ENCODE project has passed
"""
######################################
## Begin OF configuration of Paramters##
######################################

# -------------------------This part is for GLOBAL parameter -------------------------

# Create a parser
parser = argparse.ArgumentParser(
    description="Command line for cutadapt and fastuniq.")

# Create argument for the first input file
parser.add_argument("inputFiles1", type=str, help="The first input files")

# Create argument for second input file
parser.add_argument("inputFiles2", type=str, help="The second input raw fastq files")

# Create argument for genome reference file
parser.add_argument("reference_genome", type=str, help="Input for the reference genome")

# Creat argument for first output file
parser.add_argument("outputFiles1", type=str, help="Name of first output file")

# Creat argument for second output file
parser.add_argument("outputFiles2", type=str,
                    help="Name of second output file")

# Intermediate Data stroge
parse.add_argument(
    "-inter", "--intermediate_file", type=str, help="intermediate file storage, defalt is same dirctory of output file.")

# -------------------------This part is for LOCAL parameters of each software -------------------------

## SECTION: Cutadapt -----------------------------------------------------------------------------------
# Create argument for 3' adapter and 5' adapter
parser.add_argument(
    "-a", type=str, help="Trim 3' reads adapter", action='append')
parser.add_argument(
    "-g", type=str, help="Trim 5' reads adapter", action='append')

# Create argument for second adapter of 3' and 5'
parser.add_argument(
    "-A", type=str, help="Second 3' reads adapter", action='append')
parser.add_argument(
    "-G", type=str, help="Second 5' reads adapter", action='append')

# Create arugment for error rate
parser.add_argument(
    "-e", type=str, help="Error rate"
)


## SECTION: STAR

## SECTION: PureClip
parser.add_argument("-pcn", '--pureclip-parallel-num', help="pureclip parallelism number")
parser.add_argument("-pcchr", '--pureclip-chr', help="if specificed, then pureclip can have more narrow focus.")

## SECTION: PARS



## SECTION: GO




# Get all the arguments
args = parser.parse_args()


share_param = {
        'genome_ref': args.reference_genome,
    }
######################################
## End OF configuration of Paramters##
######################################


# -------------------------This part is for cutadapt-------------------------
# call the functions for commandline
cf.CallCutadapt(args)
cf.CallInputlist(args)
cf.CallFastuniq(args)

# -------------------------This part is for STAR -------------------------
# Section: Calling STAR
# Input_file_name1: reads_


# -------------------------This part is for Samtools-------------------------
# Section: Calling Samtools



# -------------------------This part is for PureClip-------------------------
# Section: Calling pureclip
# input_file_name1: pureclip_reads.bam
# input_file_name2: pureclip_reads.bam.bai
# input_file_name3: genome.fa
# output_file_name1: pureclip_output.bed
# parallel number: pureclip_parallel_num
pureclip_param = {
        'reads': star_param['output_bam'],
        'align': samtool_param['output_bai'],
        'genome': share_param['genome_ref'],
        'output_bed': 'pureclip_output.bed',
        'parallel_num': args.pureclip_parallel_num,
        'specific_chromsome': args.pureclip_chr,
        }
pc = PureClip(pureclip_param)
pc.CallPureClip(args)



# -------------------------This part is for PARS-------------------------
# Section: Calling PARS


# -------------------------This part is for GO-------------------------
# Section: Calling GO

import subprocess
import argparse
import os
import signal
from .cutadapt import CutAdapt
from .pureclip import PureClip
from .star import STAR
from .samtools import SAM
from .go_analysis import GO
from .pras import PRAS


"""
Sample data test from ENCODE project has passed
"""
######################################
## Begin OF configuration of Paramters##
######################################

def main():
    # -------------------------This part is for GLOBAL parameter -------------------------
    # SECTION-1: create argparse structures for final software input and output.

    # Create a parser
    parser = argparse.ArgumentParser(
        description="Command line for cutadapt.")

    # Create argument for the first input file
    parser.add_argument("--input_file1", default="INPUT_FILE1", type=str, help="Paired end 1 fastq file")

    # Create argument for second input file
    parser.add_argument("--input_file2", default="INPUT_FILE2", type=str, help="Paired end 2 fastq file")

    # Create argument for genome reference file
    parser.add_argument("--reference_genome", default="HG38.FA", type=str,
                        help="Input for the reference genome")

    # Create argument for genome annotation file
    parser.add_argument("--genome_annot", type=str, default="GENOME_ANNOT",
                        help="Input for the genome annotation file")


    # Creat argument for second output file
    parser.add_argument("--GO_result_folder", default="GO-result-folder", type=str,
                        help="GO output folder name")

    # Intermediate Data stroge
    parser.add_argument(
        "-inter", "--intermediate_file", default="/tmp/biopro", type=str, help="intermediate file storage, default is same dirctory of output file.")

    parser.add_argument("-dependency", "--dependancy_script_folder", default="dependency", help="dependency folder for GO and PRAS script")


    # SECTION-2: create argparse structure for each subsoftware we use.

    # SECTION-2.1 Cutadapt

    # Round 1
    # Create argument for 3' adapter and 5' adapter
    parser.add_argument(
        "-a", type=str, default="ATCG", help="3' reads adapter forward reads, first round", action='append')
    parser.add_argument(
        "-g", type=str, default="TCGA", help="5' reads adapter forward reads, first round", action='append')

    # Create argument for more adapters of 3' and 5'
    parser.add_argument(
        "-A", type=str, default="CGAT", help="3' reads adapter reverse reads, first round", action='append')
    parser.add_argument(
        "-G", type=str, default="GATC", help="5' reads adapter reverse reads, first round", action='append')

    # Round 2
    parser.add_argument(
        "-a2", type=str, default="atcg", help="3' reads adapter forward reads, second round", action='append')
    parser.add_argument(
        "-g2", type=str, default="tcga", help="5' reads adapter forward reads, second round", action='append')

    # Create argument for more adapters of 3' and 5'
    parser.add_argument(
        "-A2", type=str, default="cgat", help="3' reads adapter reverse reads, second round", action='append')
    parser.add_argument(
        "-G2", type=str, default="gatc", help="5' reads adapter reverse reads, second round", action='append')

    # For simplification, I will keep every other parameters the same as process from Yeo's lab.

    # SECTION-2.2 STAR
    # TODO: build parser structure for STAR, specify which what kind of parameters is needed for STAR related input.
    # No Need to input parameters for STAR


    # SECTION-2.3: SAMtools
    # TODO: build parser structure for SAMtools, specify which what kind of parameters is needed for SAMtools related input.
    # No Need for Input


    # SECTION-2.4: PureClip
    # TODO: build parser structure for PureClip, specify which what kind of parameters is needed for PureClip related input.
    parser.add_argument("-pcn", '--pureclip-parallel-num', default=10, type=int,
                         help="pureclip parallelism number")
    parser.add_argument("-pcchr", '--pureclip-chr', default=None,
                         help="if specificed, then pureclip can have more narrow focus.")

    # SECTION-2.5: PRAS
    # TODO: build parser structure for PARS, specify which what kind of parameters is needed for PARS related input.

    parser.add_argument("-pout", "--pras_output", type=str, default="pras_assign.txt", help="Location for the dependency for PRAS software.")



    parser.add_argument("-pscl", "--pras_script_loc", type=str, default="PRAS_1.0.py", help="Location for the dependency for PRAS software.")

    parser.add_argument("-t",'--id_file',type=str, default="id_file", help="Input the ID file. This file has to have two columns, the first column is the transcript ID, and the second column is the gene id or gene name. Please check the instruction page for file example.", action='append')
    parser.add_argument("-s",'--pras_region', type=str, default="pras_region", help="Input the Genomic region. Comma separated multiple genomic regions are acceptable. For single genomic region, there are five options: '5UTR' is the 5'UTR, 'CDS' is the coding region, '3UTR' is the 3'UTR, 'transcript' is the entire transcript, and 'splice' is for splicing site (SS). If no input provided, PRAS will take the transcript as the default input. As for multiple genomic regions, any combination of '5UTR', 'CDS', and '3UTR' is accepted. 'splice' cannot appear in the multiple genomice region input.")

    # SECTION-2.6: GO
    # TODO: build parser structure for GO, specify which what kind of parameters is needed for GO related input.

    parser.add_argument("-gosl", '--go_script_file_name', type=str, default="GeneEnrichment.R",
                        help="Tell GO where to open the GO R script. Defalut is without starter folder.")
    parser.add_argument("-gotp", "--go_top_percent", type=float, default=0.05, help="go top percent")


    # Get all the arguments
    args = parser.parse_args()

    # SECTION-2.7: Shared parameters
    # TODO: If you need any shared parameters, please include them here. And for minimal redundancy, use the shared param if possible.
    share_param = {
        'genome_ref': args.reference_genome,
        'intermediate_folder': args.intermediate_file,
        'dependancy_script_folder': args.dependancy_script_folder
    }


    # make intermediate folder
    os.makedirs(share_param['intermediate_folder'], exist_ok=True)

    ######################################
    ## End OF configuration of Paramters##
    ######################################


    # SECTION 3: CALL FUNCTIONs


    # SECTION 3.1: CutAdapt
    # TODO: Define your local parameter dict you want to pass into the class.


    cutadapt_param = {
        'input_file1': args.input_file1,
        'input_file2': args.input_file2,
        'adapter_a1': args.a,
        'adapter_A1': args.A,
        'adapter_g1': args.g,
        'adapter_G1': args.G,
        'adapter_a2': args.a2,
        'adapter_A2': args.A2,
        'adapter_g2': args.g2,
        'adapter_G2': args.G2,
        'inter_folder': share_param['intermediate_folder'],
    }

    #print("cutadapt_param: ", cutadapt_param)
    cf = CutAdapt(cutadapt_param)
    cf.CallCutAdapt()


    # SECTION-3.2: Calling STAR
    # TODO: Define your local parameter dict you want to pass into the class.
    star_param = {
        'genome_ref': share_param['genome_ref'],
        'inter_folder': share_param['intermediate_folder'],
        'genome_annot': args.genome_annot,
        'output_bam': os.path.join(share_param['intermediate_folder'], 'star_output.bam')
    }  # MODIFY this

    #print("star parameters: ", star_param)
    st = STAR(star_param)
    st.CallSTAR()


    # SECTION-3.3: Calling Samtools
    # TODO: Define your local parameter dict you want to pass into the class.


    samtool_param = {
        'input_bam': star_param['output_bam'],
        'output_bai': star_param['output_bam'] + '.bai'
    }  # MODIFY this

    #print("samtools_parameters: \n", samtool_param)

    sm = SAM(samtool_param)
    sm.CallSAM()

    # SECTION-3.4: Calling pureclip
    # TODO: Define your local parameter dict you want to pass into the class.
    # call the functions for commandline
    pureclip_param = {
        'reads': os.path.join(share_param['intermediate_folder'], star_param['output_bam']),
        'align': os.path.join(share_param['intermediate_folder'], samtool_param['output_bai']),
        'genome': share_param['genome_ref'],
        'output_bed': os.path.join(share_param['intermediate_folder'], 'pureclip_output.bed'),
        'parallel_num': args.pureclip_parallel_num,
        'specific_chromosome': args.pureclip_chr,
    }  # MODIFY this

    #print("PureClip: \n", pureclip_param)
    pc = PureClip(pureclip_param)
    pc.CallPureClip()


    # SECTION-3.5: Calling PRAS
    # TODO: Define your local parameter dict you want to pass into the class.

    pras_param = {
    	'annot_file':star_param['genome_annot'],
    	'id_file':args.id_file,
    	'region':args.pras_region,
        'input_file':pureclip_param['output_bed'],
        'output_file': os.path.join(share_param['intermediate_folder'], args.pras_output),
        'script_loc': os.path.join(share_param['dependancy_script_folder'], args.pras_script_loc)
    }
    #print("pras: \n", pras_param)

    pr = PRAS(pras_param)
    pr.CallPRAS()


    # SECTION-3.6: Calling GO
    # TODO: Define your local parameter dict you want to pass into the class.
    go_param = {
            'pras_file': pras_param['output_file'],
            'output_folder': args.GO_result_folder,
            'script_loc': share_param['dependancy_script_folder'] + "/" + args.go_script_file_name ,# require args input
            'intermediate_dir': share_param['intermediate_folder'], # require shared param
            'top_percent': args.go_top_percent, # float please, require args input
            }  # MODIFY this
    #print("GO paramerters: \n", go_param)
    go = GO(go_param)
    go.CallGO()


if __name__ == "__main__":
    main()

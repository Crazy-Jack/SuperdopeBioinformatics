import subprocess
import argparse
import signal

# -------------------------This part is for skewer-------------------------
"""
Sample data test from ENCODE project has passed
"""
# Create a parser
parser = argparse.ArgumentParser(
    description="Command line for skewer and fastuniq.")

# Create argument for the first input file
parser.add_argument("inputFiles1", type=str, help="The first input files")

# Create argument for second input file
parser.add_argument("inputFiles2", type=str, help="The second input files")

# Creat argument for first output file
parser.add_argument("outputFiles1", type=str, help="Name of first output file")

# Creat argument for second output file
parser.add_argument("outputFiles2", type=str,
                    help="Name of second output file")

# Create argument for left adapter and right adapter
parser.add_argument("-l", type=str, help="Left adapter of the file")
parser.add_argument("-r", type=str, help="Right adapter of the file")

# Get all the arguments
args = parser.parse_args()
combine_args_skewer = ""
combine_args_skewer += "../skewer/skewer" + " "
# Combine all arguments to a command line
if args.l is not None:
    combine_args_skewer += "-x " + args.l + " "

if args.r is not None:
    combine_args_skewer += "-y " + args.r + " "

combine_args_skewer += args.inputFiles1 + " " + args.inputFiles2

# Call the command line, this causes a gzip: broken pipe bug
# subprocess.call(combine_args_skewer, shell=True)

# fix it from someone's blog but still do not konw how it works
p = subprocess.Popen(
    combine_args_skewer,
    preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
    shell=True,
).wait()


# ------------This part is to create input list file for Fastuniq-----------
"""
input_list.txt generated successfully and correctly
"""
# Create two command lines to generate input file list for fastuniq
combine_args_inputlist1 = ""
combine_args_inputlist1 = (
    'echo "' + args.inputFiles1[:-3] + '-trimmed-pair1.fastq" > input_list.txt'
)

combine_args_inputlist2 = ""
combine_args_inputlist2 = (
    'echo "' + args.inputFiles1[:-3]
    + '-trimmed-pair2.fastq" >> input_list.txt'
)

# Call the command line
subprocess.call(combine_args_inputlist1, shell=True)
subprocess.call(combine_args_inputlist2, shell=True)

# ------------This part is for Fastuniq--------------------------------------
"""
Sample data produced by skewer has passed
"""
combine_args_fastuniq = ""
combine_args_fastuniq = (
    "../FastUniq/source/fastuniq -i input_list.txt -t q -o "
    + args.outputFiles1
    + " -p "
    + args.outputFiles2
    + " -c 1"
)

p = subprocess.Popen(
    combine_args_fastuniq,
    preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
    shell=True,
).wait()

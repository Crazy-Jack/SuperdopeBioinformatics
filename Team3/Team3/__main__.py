import subprocess
import argparse
import signal

# -------------------------This part is for catadapt-------------------------
"""
Sample data test from ENCODE project has passed
"""
# Create a parser
parser = argparse.ArgumentParser(
    description="Command line for catadapt and fastuniq.")

# Create argument for the first input file
parser.add_argument("inputFiles1", type=str, help="The first input files")

# Create argument for second input file
parser.add_argument("inputFiles2", type=str, help="The second input files")

# Creat argument for first output file
parser.add_argument("outputFiles1", type=str, help="Name of first output file")

# Creat argument for second output file
parser.add_argument("outputFiles2", type=str,
                    help="Name of second output file")

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
# Get all the arguments
args = parser.parse_args()
combine_args_catadapt = ""
combine_args_catadapt += "cutadapt" + " "

# Combine all arguments to a command line
if args.e is not None:
    combine_args_catadapt += "-e " + args.e + " "
if args.a is not None:
    for i in args.a:
        combine_args_catadapt += "-a " + i + " "

if args.A is not None:
    for i in args.A:
        combine_args_catadapt += "-A " + i + " "
if args.g is not None:
    for i in args.g:
        combine_args_catadapt += "-g " + i + " "

if args.G is not None:
    for i in args.G:
        combine_args_catadapt += "-G " + i + " "


combine_args_catadapt += args.inputFiles1 + " " + args.inputFiles2 + " "
combine_args_catadapt += "-o " + args.inputFiles1 + \
    "-trimmed1.fastq " + "-p " + args.inputFiles2 + "-trimmed2.fastq "
# Call the command line, this causes a gzip: broken pipe bug
subprocess.call(combine_args_catadapt, shell=True)

# fix it from someone's blog but still do not konw how it wors
p = subprocess.Popen(
    combine_args_catadapt,
    preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
    shell=True,
).wait()


# # ------------This part is to create input list file for Fastuniq-----------
"""
input_list.txt generated successfully and correctly
"""
# Create two command lines to generate input file list for fastuniq
combine_args_inputlist1 = ""
combine_args_inputlist1 = (
    'echo "' + args.inputFiles1 + '-trimmed1.fastq" > input_list.txt'
)

combine_args_inputlist2 = ""
combine_args_inputlist2 = (
    'echo "' + args.inputFiles2
    + '-trimmed2.fastq" >> input_list.txt'
)

# Call the command line
subprocess.call(combine_args_inputlist1, shell=True)
subprocess.call(combine_args_inputlist2, shell=True)

# ------------This part is for Fastuniq--------------------------------------
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

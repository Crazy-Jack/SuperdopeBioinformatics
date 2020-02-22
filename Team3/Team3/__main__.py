import subprocess
import argparse
import signal
import cutadapt_fastuniq as cf


# -------------------------This part is for cutadapt-------------------------
"""
Sample data test from ENCODE project has passed
"""
# Create a parser
parser = argparse.ArgumentParser(
    description="Command line for cutadapt and fastuniq.")

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
# call the functions for commandline
cf.CallCutadapt(args)
cf.CallInputlist(args)
cf.CallFastuniq(args)

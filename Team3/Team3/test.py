import argparse

parser = argparse.ArgumentParser(
    description="Command line for cutadapt and fastuniq.")

# Create argument for the first input file
parser.add_argument("-ar", type=str, nargs=2, action='append',  help="The first input files")


a = parser.parse_args()

print(a.ar)

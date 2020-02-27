import subprocess
import signal


class CutAdapt:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
        self.input1 = parameters['input_file1']
        self.input2 = parameters['input_file2']
        self.adpater_a = parameters['adpater_a']
        self.adpater_A = parameters['adpater_A']
        self.adpater_g = parameters['adpater_g']
        self.adpater_G = parameters['adpater_G']
        pass

    def CallCutAdapt(self):
        # TODO: Please follow the try/except paradigm so that user can know which software to look for when it breaks. And also use subprocess to run the command.
        try:
            # fixed parameters
            combine_args_catadapt = ""
            combine_args_catadapt += "cutadapt -f fastq --match-read-wildcards --times 1 -e 0.1 -O 1 --quality-cutoff 6 -m 18" + " "

            # Concatenate adpaters parameters
            if self.adpater_a is not None:
                for i in self.adpater_a:
                    combine_args_catadapt += "-a " + i + " "

            if self.adpater_A is not None:
                for i in self.adpater_A:
                    combine_args_catadapt += "-A " + i + " "
            if self.adpater_g is not None:
                for i in self.adpater_g:
                    combine_args_catadapt += "-g " + i + " "

            if self.adpater_G is not None:
                for i in self.adpater_G:
                    combine_args_catadapt += "-G " + i + " "

            # Concatenate input and output parameters
            combine_args_catadapt += "-o " + self.input1 + \
                "-trimmed1.fastq " + "-p " + self.input2 + "-trimmed2.fastq "
            combine_args_catadapt += self.input1 + " " + self.input2 + " "

            # call the service
            print(combine_args_catadapt)
            p = subprocess.Popen(
                combine_args_catadapt,
                preexec_fn=lambda: signal.signal(
                    signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()
        except Exception as e:
            print("CutAdapt analysis Error: ", e)


# def CallCutadapt(args):
#     # fixed parameters
#     combine_args_catadapt = ""
#     combine_args_catadapt += "cutadapt -f fastq --match-read-wildcards -times 1 -e 0.1 -O 1 --quality cutoff 6 -m 18" + " "

#     # Concatenate adpaters parameters
#     if args.a is not None:
#         for i in args.a:
#             combine_args_catadapt += "-a " + i + " "

#     if args.A is not None:
#         for i in args.A:
#             combine_args_catadapt += "-A " + i + " "
#     if args.g is not None:
#         for i in args.g:
#             combine_args_catadapt += "-g " + i + " "

#     if args.G is not None:
#         for i in args.G:
#             combine_args_catadapt += "-G " + i + " "


#     # Concatenate input and output parameters
#     combine_args_catadapt += "-o " + args.inputFiles1 + \
#         "-trimmed1.fastq " + "-p " + args.inputFiles2 + "-trimmed2.fastq "
#     combine_args_catadapt += args.inputFiles1 + " " + args.inputFiles2 + " "

#     # Call the command line, this causes a gzip: broken pipe bug
#     # subprocess.call(combine_args_catadapt, shell=True)

#     # fix it from someone's blog but still do not konw how it works
#     p = subprocess.Popen(
#         combine_args_catadapt,
#         preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
#         shell=True,
#     ).wait()

# def CallInputlist(args):
#     combine_args_inputlist1 = ""
#     combine_args_inputlist1 = (
#         'echo "' + args.inputFiles1 + '-trimmed1.fastq" > input_list.txt'
#     )

#     combine_args_inputlist2 = ""
#     combine_args_inputlist2 = (
#         'echo "' + args.inputFiles2
#         + '-trimmed2.fastq" >> input_list.txt'
#     )

#     # Call the command line
#     subprocess.call(combine_args_inputlist1, shell=True)
#     subprocess.call(combine_args_inputlist2, shell=True)

# def CallFastuniq(args):
#     combine_args_fastuniq = ""
#     combine_args_fastuniq = (
#         "../FastUniq/source/fastuniq -i input_list.txt -t q -o "
#         + args.outputFiles1
#         + " -p "
#         + args.outputFiles2
#         + " -c 1"
#     )

#     p = subprocess.Popen(
#         combine_args_fastuniq,
#         preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
#         shell=True,
#     ).wait()

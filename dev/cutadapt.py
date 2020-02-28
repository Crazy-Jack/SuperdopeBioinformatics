import subprocess
import signal


class CutAdapt:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
        self.input1 = parameters['input_file1']
        self.input2 = parameters['input_file2']
        self.adapter_a1 = parameters['adapter_a1']
        self.adapter_A1 = parameters['adapter_A1']
        self.adapter_g1 = parameters['adapter_g1']
        self.adapter_G1 = parameters['adapter_G1']
        self.adapter_a2 = parameters['adapter_a2']
        self.adapter_A2 = parameters['adapter_A2']
        self.adapter_g2 = parameters['adapter_g2']
        self.adapter_G2 = parameters['adapter_G2']
        self.inter_folder = parameters['inter_folder']
        pass

    def CallCutAdapt(self):
        # TODO: Please follow the try/except paradigm so that user can know which software to look for when it breaks. And also use subprocess to run the command.
        try:
            # fixed parameters
            combine_args_catadapt = ""
            combine_args_catadapt += "cutadapt -f fastq --match-read-wildcards --times 1 -e 0.1 -O 1 --quality-cutoff 6 -m 18" + " "
            combine_args_catadapt2 = ""

            gzip1 = "gzip " + self.inter_folder + "/trimmed1.fastq"
            gzip2 = "gzip " + self.inter_folder + "/trimmed2.fastq"
            # Concatenate adapters parameters
            if self.adapter_a1 is not None:
                for i in self.adapter_a1:
                    combine_args_catadapt += "-a " + i + " "

            if self.adapter_A1 is not None:
                for i in self.adapter_A1:
                    combine_args_catadapt += "-A " + i + " "
            if self.adapter_g1 is not None:
                for i in self.adapter_g1:
                    combine_args_catadapt += "-g " + i + " "

            if self.adapter_G1 is not None:
                for i in self.adapter_G1:
                    combine_args_catadapt += "-G " + i + " "

            if self.adapter_a2 is None and self.adapter_A2 is None and self.adapter_g2 is None and self.adapter_G2 is None:
                combine_args_catadapt += "-o " + self.inter_folder + \
                    "/trimmed1.fastq " + "-p " + self.inter_folder + "/trimmed2.fastq "
                combine_args_catadapt += self.input1 + " " + self.input2 + " "

                p = subprocess.Popen(
                    combine_args_catadapt,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

                p = subprocess.Popen(
                    gzip1,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

                p = subprocess.Popen(
                    gzip2,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()
            else:
                combine_args_catadapt += "-o " + self.inter_folder + \
                    "/trimmed1_1.fastq " + "-p " + self.inter_folder + "/trimmed2_1.fastq "
                combine_args_catadapt += self.input1 + " " + self.input2 + " "

                combine_args_catadapt2 += "cutadapt -f fastq --match-read-wildcards --times 1 -e 0.1 -O 5 --quality-cutoff 6 -m 18" + " "
                if self.adapter_a2 is not None:
                    for i in self.adapter_a2:
                        combine_args_catadapt2 += "-a " + i + " "

                if self.adapter_A2 is not None:
                    for i in self.adapter_A2:
                        combine_args_catadapt2 += "-A " + i + " "
                if self.adapter_g2 is not None:
                    for i in self.adapter_g2:
                        combine_args_catadapt2 += "-g " + i + " "

                if self.adapter_G2 is not None:
                    for i in self.adapter_G2:
                        combine_args_catadapt2 += "-G " + i + " "

                combine_args_catadapt2 += "-o " + self.inter_folder + \
                    "/trimmed1.fastq " + "-p " + self.inter_folder + "/trimmed2.fastq "
                combine_args_catadapt2 += self.inter_folder + \
                    "/trimmed1_1.fastq " + self.inter_folder + "/trimmed2_1.fastq "

                p = subprocess.Popen(
                    combine_args_catadapt,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

                p = subprocess.Popen(
                    combine_args_catadapt2,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

                p = subprocess.Popen(
                    gzip1,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

                p = subprocess.Popen(
                    gzip2,
                    preexec_fn=lambda: signal.signal(
                        signal.SIGPIPE, signal.SIG_DFL),
                    shell=True,
                ).wait()

            # call the service
            # print(combine_args_catadapt)

        except Exception as e:
            print("CutAdapt analysis Error: ", e)


# def CallCutadapt(args):
#     # fixed parameters
#     combine_args_catadapt = ""
#     combine_args_catadapt += "cutadapt -f fastq --match-read-wildcards -times 1 -e 0.1 -O 1 --quality cutoff 6 -m 18" + " "

#     # Concatenate adapters parameters
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

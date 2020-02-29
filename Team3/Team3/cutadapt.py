import subprocess
import signal


class CutAdapt:
    def __init__(self, parameters):
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


        except Exception as e:
            print("CutAdapt analysis Error: ", e)


import subprocess
import signal

class PureClip:
    def __init__(self, parameter):
        self.reads_filename = parameter['reads']
        self.algin_filename = parameter['align']
        self.genome_filename = parameter['genome']
        self.parallel_num = parameter['parallel_num']
        self.specific_chromosome = parameter['specific_chromosome']
        self.output_filename = parameter['output_bed']


    def CallPureClip(self):
        try:
            command = "pureclip " + "-i " + self.reads_filename + " -bai " + self.algin_filename + " -g " + self.genome_filename + " -nt " +  str(self.parallel_num) + " -o " + self.output_filename
            if self.specific_chromosome != None:
                command += " -iv " + self.specific_chromosome

            #command += " &> /dev/null"
            # call the service

            p = subprocess.Popen(
                command,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()

        except Exception as e:
            print("PureClip Error: ", e)



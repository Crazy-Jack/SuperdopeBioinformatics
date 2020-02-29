import subprocess
import signal

class SAM:
    def __init__(self, parameters):
        self.bam = parameters['input_bam']
        self.bai = parameters['output_bai']


    def CallSAM(self):
        try:
            command = "samtools index " + self.bam + " " + self.bai # MODIFY this
            # call the service
            command += " &> /dev/null"
            # subprocess.call(command, shell=True)
            p = subprocess.Popen(
                command,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()
        except Exception as e:
            print("SAMtools analysis Error: ", e)

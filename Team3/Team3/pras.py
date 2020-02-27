import subprocess
import signal

class PARS:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
	self.annot_file=parameters['annot_file']
	self.id_file=parameters['id_file']
	self.region=parameters['region']
	self.input_file=parameters['input_file']

    def CallPARS(self):
        # TODO: Please follow the try/except paradigm so that user can know which software to look for when it breaks. And also use subprocess to run the command.
        try:
            command = "python3 PRAS_1.0.py -g " + self.annot_file+" -t "+self.id_file+" -m score -s"+self.region+" -i "+self.input_file+" -a pras_assign.txt -w 0 -d 1000" # MODIFY this
            # call the service
            print(command)
            p = subprocess.Popen(
                command,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()
        except Exception as e:
            print("PARS analysis Error: ", e)


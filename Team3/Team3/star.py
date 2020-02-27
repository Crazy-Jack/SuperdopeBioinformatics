import subprocess
import signal

class STAR:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
        pass

    def CallSTAR(self):
        # TODO: Please follow the try/except paradigm so that user can know which software to look for when it breaks. And also use subprocess to run the command.
        try:
            command = "" # MODIFY this
            # call the service
            print(command)
            p = subprocess.Popen(
                command,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()
        except Exception as e:
            print("STAR analysis Error: ", e)

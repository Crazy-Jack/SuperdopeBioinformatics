import subprocess
import signal
from getGeneList import getGeneList





class GO:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
        self.script_loc = parameters['script_loc']
        self.pras_file = parameters['pras_file']
        self.intermediate_dir = parameters['intermediate_dir']
        self.top_percent = parameters['top_percent']
        self.output_folder = parameters['output_folder']
        if self.output_folder[-1] == "/":
            self.output_folder = self.output_folder[:-1]

    def preprocess(self):
        """Process pars output into list of genes"""
        try:
            self.genelist_loc = getGeneList(self.intermediate_dir + '/' + self.pras_file, self.intermediate_dir, percent=self.top_percent)

        except Exception as e:
            print("GO Error: Fatal preprocessing: ", e)


    def CallGO(self):
        # TODO: Please follow the try/except paradigm so that user can know which software to look for when it breaks. And also use subprocess to run the command.
        try:
            self.preprocess()
            if not self.genelist_loc:
                raise NameError("GO Error: Gene List not found, preprocess them before feed into GO!")
            command = "Rscript " + self.script_loc + " " + self.genelist_loc + " " + self.output_folder# MODIFY this
            # call the service

            command += " &> /dev/null"
            print("-------------")
            print(command)
            print("\n")
            #p = subprocess.Popen(
            #    command,
            #    preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
            #    shell=True,
            #).wait()
        except Exception as e:
            print("GO analysis Error: ", e)




# test

#share_param = {
#    'intermediate_folder': 'intermediate',
#    'dependancy_script_folder': 'dependency_script'
#}
#go_param = {
#        'pras_file': 'binding_PRAS.txt',
#        'output_folder': 'GO-result-folder',
#        'script_loc': share_param['dependancy_script_folder'] + "/" + 'GeneEnrichment.R', # require args input
#        'intermediate_dir': share_param['intermediate_folder'], # require shared param
#        'top_percent': 0.05, # float please, require args input
#        }  # MODIFY this
#go = GO(go_param)
#go.CallGO()

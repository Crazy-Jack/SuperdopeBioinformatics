import subprocess
import signal


class CutAdapt:
    def __init__(self, parameters):
        # TODO: fill in as self.xxx = parameters['xxx']
        pass

    def CallCutAdapt(self):
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
            print("CutAdapt analysis Error: ", e)







def CallCutadapt(args):
    combine_args_catadapt = ""
    combine_args_catadapt += "cutadapt" + " "

    # Combine all arguments to a command line
    if args.e is not None:
        combine_args_catadapt += "-e " + args.e + " "
    if args.a is not None:
        for i in args.a:
            combine_args_catadapt += "-a " + i + " "

    if args.A is not None:
        for i in args.A:
            combine_args_catadapt += "-A " + i + " "
    if args.g is not None:
        for i in args.g:
            combine_args_catadapt += "-g " + i + " "

    if args.G is not None:
        for i in args.G:
            combine_args_catadapt += "-G " + i + " "


    combine_args_catadapt += args.inputFiles1 + " " + args.inputFiles2 + " "
    combine_args_catadapt += "-o " + args.inputFiles1 + \
        "-trimmed1.fastq " + "-p " + args.inputFiles2 + "-trimmed2.fastq "

    # Call the command line, this causes a gzip: broken pipe bug
    # subprocess.call(combine_args_catadapt, shell=True)

    # fix it from someone's blog but still do not konw how it works
    p = subprocess.Popen(
        combine_args_catadapt,
        preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
        shell=True,
    ).wait()

def CallInputlist(args):
    combine_args_inputlist1 = ""
    combine_args_inputlist1 = (
        'echo "' + args.inputFiles1 + '-trimmed1.fastq" > input_list.txt'
    )

    combine_args_inputlist2 = ""
    combine_args_inputlist2 = (
        'echo "' + args.inputFiles2
        + '-trimmed2.fastq" >> input_list.txt'
    )

    # Call the command line
    subprocess.call(combine_args_inputlist1, shell=True)
    subprocess.call(combine_args_inputlist2, shell=True)

def CallFastuniq(args):
    combine_args_fastuniq = ""
    combine_args_fastuniq = (
        "../FastUniq/source/fastuniq -i input_list.txt -t q -o "
        + args.outputFiles1
        + " -p "
        + args.outputFiles2
        + " -c 1"
    )

    p = subprocess.Popen(
        combine_args_fastuniq,
        preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
        shell=True,
    ).wait()

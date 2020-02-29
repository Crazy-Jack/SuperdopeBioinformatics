import subprocess
import signal

class STAR:
    def __init__(self, parameters):
        self.genome_ref = parameters['genome_ref']
        self.inter_folder = parameters['inter_folder']
        self.genome_annot = parameters['genome_annot']

    def CallSTAR(self):
        try:
            command_gene_index = "STAR --runThreadN 10 --runMode genomeGenerate --genomeDir "
            command_gene_index += self.inter_folder + "/"
            command_gene_index += " --genomeFastaFiles "
            command_gene_index += self.genome_ref
            command_gene_index += " --sjdbGTFfile "
            command_gene_index += self.genome_annot
            command_gene_index += " --sjdbOverhang 49"

            command_mapping = "STAR --outSAMtype BAM SortedByCoordinate --runThreadN 10 --genomeDir "
            command_mapping += self.inter_folder + "/"
            command_mapping += " --readFilesIn "
            command_mapping += self.inter_folder + "/"
            command_mapping += "trimmed1.fastq.gz "
            command_mapping += self.inter_folder + "/"
            command_mapping += "trimmed2.fastq.gz"
            command_mapping += " --readFilesCommand  zcat --outFilterType BySJout --outFilterMultimapNmax 1 --alignSJoverhangMin 8 --alignSJDBoverhangMin 1 --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --scoreDelOpen -1 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000 "
            command_mapping += "--outFileNamePrefix " + self.inter_folder +"/ --alignEndsType EndToEnd"
            # call the service
            # print(command_mapping)

            command_gene_index += " &> /dev/null"
            command_mapping += " &> /dev/null"
            p = subprocess.Popen(
                command_gene_index,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()

            p = subprocess.Popen(
                command_mapping,
                preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL),
                shell=True,
            ).wait()

            print(command_mapping)
        except Exception as e:
            print("STAR analysis Error: ", e)

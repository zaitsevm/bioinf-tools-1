""" Bio-files processor 

This script contains functions that could be utilised
as tools for processing ubiquitos biologycal file types, such as: fasta, fastq, gbk
"""

import os 

def convert_multiline_fasta_to_oneline(
    input_fasta: str, 
    output_fasta: str =None
) -> None:
    """This function converts multi-line FASTA sequences
     in a given file input_fasta to single-line sequences 
     and writes updated oneline FASTA into a new file. 
     Arguments: input_file (str): path to the input FASTA file, 
     output_fasta(optional): path to the output file. If not provided, 
     a new file will be created in the current directory.
    """
    if output_fasta is None:
        output_fasta = "output_fasta.fasta"
    with open(input_fasta, "r") as file, open(output_fasta, "w") as temp_file:
        line1 = file.readline()
        file.seek(0)
        for line in file:
            if line.startswith(("A", "T", "G", "C", "U")):
                line = line.replace("\n", "")
                temp_file.write(line)
            else:
                if line == line1:
                    temp_file.write(line)
                else:
                    temp_file.write("\n")
                    temp_file.write(line)


def parse_blast_output(
    input_file: str, 
    output_file: str =None
) -> None:
    """This function processes the output of a BLAST analysis 
    from a specified input file, extracting  lines with protein names 
    from first QUERY hit and saving them into a FASTQ format file. 
    If no output file is specified, the function defaults to naming 
    the output file output_file_blast.fastq. 
    Arguments: input_file (str): the path to the input file containing BLAST results, 
    output_file (str, optional): the path where the output will be saved. Defaults to "output_file_blast.fastq" if not provided.
    """
    if output_file is None:
        output_file = "output_file_blast.fastq"

    inner_file = "inner_file_blast.fastq"

    with open(input_file, "r") as file, open(inner_file, "w") as temp_file:
        for line in file:
            if line.startswith("Description"):
                line = file.readline()
                line = line.split("   ")[0]
                temp_file.write(line + "\n")

    with open(inner_file, "r") as temp_file2, open(output_file, "w") as final_file:
        lines = [line.strip() for line in temp_file2]
        sorted_lines = sorted(lines)

        for line in sorted_lines:
            final_file.write(line + "\n")

    os.remove(inner_file)


def select_genes_from_gbk_to_fasta(
    input_gbk, genes, n_before=1, n_after=1, output_fasta=None
):
    """ This function doesn't work poperly 
    (it returns incorrect genes and their translations 
    - not closest to target genes given as argument), 
    but i still left this schizo-text in there as an evidence of my struggle
    Probably need to fix how gene_translation_dictionary is sorted 
    or how i collect before and after genes in the last steps
    """
    if output_fasta is None:
        output_fasta = "output_fasta_from_gbk.fasta"

    gene_translation_dict = {}

    with open(input_gbk, "r") as file:
        gene_hold = ""
        translation_hold = ""

        for line in file:
            line = line.strip()

            if line.startswith("CDS"):
                if translation_hold and gene_hold:
                    gene_translation_dict[gene_hold] = translation_hold

                translation_hold = ""
                gene_hold = ""

            if line.startswith("/gene="):
                gene_hold = line.split("=")[1].strip('"')

            if line.startswith("/translation="):
                translation_hold = line.split("=")[1].strip('"')
            elif translation_hold:
                translation_hold += line.strip('"')

        if translation_hold and gene_hold:
            gene_translation_dict[gene_hold] = translation_hold

    with open(output_fasta, "w") as inside_file:
        for target_gene in genes:

            before_count = 0
            for gene in gene_translation_dict.keys():
                if before_count < n_before and gene < target_gene:
                    inside_file.write(f">{gene}\n{gene_translation_dict[gene]}\n")
                    before_count += 1

            after_count = 0
            for gene in gene_translation_dict.keys():
                if after_count < n_after and gene > target_gene:
                    inside_file.write(f">{gene}\n{gene_translation_dict[gene]}\n")
                    after_count += 1

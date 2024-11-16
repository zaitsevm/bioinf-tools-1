# Bioinformatics Tools 1

## What is it?

This repository contains scripts with various bioinformatics tools designed for processing and filtering sequences (DNA/RNA) and for working with common types of biological files, 
such as: fasta, fastq, gbk. 

## Requirements

To use this script, you need the following custom modules:
- `filter_fastq_module`
- `dna_rna_tools_module`
- `input_output_module`

## Installation

You can clone this repository to your local:
 `git clone git@github.com:zaitsevm/bioinf-tools-1.git && cd bioinf-tools-1`
 or download scripts bioinf_tools.py, bio_files_processor.py and modules (filter_fastq_module, dna_rna_tools_module) separately. Make sure the required modules are available. Ensure they are in the same directory as this script.

## Functions

### 1. `filter_fastq(input_fastq, gc_bounds, length_bounds, quality_threshold, output_fastq)`

This function filters sequences based on the specified parameters:
Returns a dictionary containing sequences that meet the specified criteria.

#### Arguments:

- `input_fastq`: Path to the input FASTA file, where names, sequences and sequence quality are stored, str.
- `gc_bounds`: Tuple or single number specifying GC content limits, set to (0, 100) by default.
- `length_bounds`: Tuple or single number specifying length limits, if given single number sets it as an upper bound, set to (0, 2**32) by default.
- `quality_threshold`: Minimum average quality score for filtering sequences, set to 0 by default.
- `output_fastq`:  Optional argument, path to the output file. 
If not provided, a new file will be created in the current directory.

### 2. `run_dna_rna_tools(*args)`

This function processes DNA or RNA sequences based on the operation provided:
The function raises a `ValueError` if any sequence is not recognized as valid DNA or RNA.
Returns a string or a list of strings, containing new sequences in accordance with the executed function.

#### Arguments:

- Multiple sequences followed by the name of the operation as the final argument.

#####Operations:

- `reverse`: Reverses the sequence.
- `transcribe`: Transcribes DNA to RNA.
- `complement`: Finds the complement sequence.
- `reverse_complement`: Finds the complement and reverses the sequence or vice versa.

### 3. `convert_multiline_fasta_to_oneline(input_fasta, output_fasta)`

This function converts multi-line FASTA sequences in a given file input_fasta to single-line sequences and writes updated one-line FASTA into a new file. 

#### Arguments:

- `input_file`: Path to the input FASTA file, str. 
- `output_fasta`: Optional argument, path to the output file. 
If not provided, a new file will be created in the current directory.

### 4. `parse_blast_output(input_file, output_file)`

This function processes the output of a BLAST analysis from a specified input file, extracting  lines with protein names from first QUERY hit and saving them into another FASTQ format file. 

#### Arguments:

- `input_file`: Path to the input file containing BLAST results, str.
- `output_file`: Optional argument, path where the output will be saved. 
Defaults to "output_file_blast.fastq" if not provided.

## Examples of usage

1. **Filtering Sequences:**

   To filter sequences based on length, GC content, and quality:

   ```python
   filtered_seqs = filter_fastq(seqs, gc_bounds=(40, 60), length_bounds=(50, 100), quality_threshold=30)
   ```

2. **DNA/RNA Tools:**

   To manipulate sequences:

   ```python
   result = run_dna_rna_tools("ATCG", "GCTA", "reverse")
   ```
     
   This will return reversed sequences of `"ATCG"` and `"GCTA"`.
   
3. **To select most prospective allighment matches:**

   To filter BLAST QUERY results:

   ```python
   path = '/content/example_blast_results.txt'
   parse_blast_output(path)
   ```

4. **To comfortably work with bio-files:**

    To rewrite multiline FASTA  sequences as one line:
        
    ```python
    path = '/content/example_multiline_fasta.fasta'
    convert_multiline_fasta_to_oneline(path)
    ```

## Contacts

For any help, contribution or bug report: contact me at cloudatlasfrrs@gmail.com.


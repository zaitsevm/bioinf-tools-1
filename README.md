# Bioinformatics Tools 1

## What is it?

This script contains various bioinformatics tools designed for processing and filtering sequences (DNA/RNA). 

## Requirements

To use this script, you need the following custom modules:
- `filter_fastq_module`
- `dna_rna_tools_module`

## Installation

You can clone this repository to your local or download script bioinf_tools.py and modules (filter_fastq_module, dna_rna_tools_module) separately. Make sure the required modules are available. Ensure they are in the same directory as this script.

## Functions

### 1. `filter_fastq(seqs, gc_bounds, length_bounds, quality_threshold)`

This function filters sequences based on the specified parameters:
Returns a dictionary containing sequences that meet the specified criteria.

#### Arguments:

- `seqs`: A dictionary where the keys are sequence identifiers and the values are tuples of (sequence, quality score).
- `gc_bounds`: Tuple or single number specifying GC content limits, set to (0, 100) by default.
- `length_bounds`: Tuple or single number specifying length limits, if given single number sets it as an upper bound, set to (0, 2**32) by default.
- `quality_threshold`: Minimum average quality score for filtering sequences, set to 0 by default.

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

## Contacts

For any help, contribution or bug report: contact me at cloudatlasfrrs@gmail.com.


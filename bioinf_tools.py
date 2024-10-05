""" Bioinformatics tools 1

This script contains various functions that could be utilised 
as bioinformatics tools by the user.
Imported modules (not Python build-in): 
filter_fastq_module, dna_rna_tools_module
"""

from add_modules.filter_fastq_module import length_control
from add_modules.filter_fastq_module import gc_control
from add_modules import dna_rna_tools_module
from statistics import mean


def filter_fastq(
    seqs: dict,
    gc_bounds: tuple or "num" = (0, 100),
    length_bounds: tuple or "num" = (0, 2**32),
    quality_threshold: "num" = 0,
) -> dict:
    """The function filters sequences
    based on the specified values ​​of the sequence length,
    its GC composition, and the threshold value
    of the average quality of the read.

    Sequences that do not meet the specified parameters are discarded.
    By default: the allowed values ​​for GC composition
    are within (0,100) range, for sequence length - (0, 2**32)
    and average read quality is 0.
    If one number is passed to the gc_bounds argument,
    then it is considered that this is the upper bound.
    The function returns a dictionary with sequences
    that meet the specified parameters.
    """

    seqs_checked = {}
    for name, (sequence, quality) in seqs.items():

        quality_scores = [(ord(char) - 33) for char in quality]
        n_seq = len(sequence)

        if (
            mean(quality_scores) > quality_threshold
            and length_control(n_seq, length_bounds)
            and gc_control(sequence, gc_bounds)
        ):
            seqs_checked[name] = (sequence, quality)

    return seqs_checked


def run_dna_rna_tools(*args: list) -> list or str:
    """The function can return complementary, reversed,
    transcribed and complementary to reversed sequences
    for an unlimited number of sequences given as arguments.

    It accepts as input a list of arguments,
    the last of which should be the name
    of one of the 4 following functions: "reverse", "transcribe",
    "complement", "reverse_complement".
    Returns a list with new sequences in accordance
    with the executed function.
    Raises ValueError if one of the given sequences
    is not recognised as DNA or RNA,
    halts the execution and specifies the erronous sequence.
    """

    *seqs, function = [*args]
    n_seqs = []
    for seq in seqs:
        if is_na(seq):
            n_seqs.append(seq)
        else:
            raise ValueError(f"Error: neither DNA nor RNA! Invalid sequence: {seq}")
    if function == "reverse":
        result = reverse(*n_seqs)
    elif function == "transcribe":
        result = transcribe(*n_seqs)
    elif function == "complement":
        result = complement(*n_seqs)
    elif function == "reverse_complement":
        res1 = complement(*n_seqs)
        result = reverse(*res1)
    return result


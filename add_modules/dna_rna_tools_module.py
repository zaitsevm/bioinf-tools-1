nucl_dna = {"a", "t", "g", "c", "A", "T", "G", "C"}
nucl_rna = {"a", "u", "g", "c", "A", "U", "G", "C"}
    
def is_na(seq: str) -> bool:
    if set(seq) <= (nucl_dna) or set(seq) <= (nucl_rna):
        return True
    else:
        return False

transcribe_dict = {"T": "U", "t": "u"}

def transcribe(*n_seqs: list) -> list:
    transcribed_seqs = []
    for seq in n_seqs:
        res1 = []
        for char in [*seq]:
            res1.append(transcribe_dict.get(char, char))
            res2 = "".join(res1)
        transcribed_seqs.append(res2)
    return transcribed_seqs


def reverse(*n_seqs: list) -> list:
    reversed_seqs = []
    for seq in n_seqs:
        reversed_seq = seq[::-1]
        reversed_seqs.append(reversed_seq)
    return reversed_seqs

complement_dict = {
        "A": "T",
        "G": "C",
        "a": "t",
        "g": "c",
        "T": "A",
        "C": "G",
        "t": "a",
        "c": "g",
        "U": "T",
        "u": "t",
        }

def complement(*n_seqs: list) -> list:
    complemented_seqs = []
    for seq in n_seqs:
        res1 = []
        for char in [*seq]:
            res1.append(complement_dict.get(char, char))
            res2 = "".join(res1)
        complemented_seqs.append(res2)
    return complemented_seqs

nucl_dna = {"a", "t", "g", "c", "A", "T", "G", "C"}
nucl_rna = {"a", "u", "g", "c", "A", "U", "G", "C"}
    
def is_na(seq: str) -> bool:
	    return set(seq) <= (nucl_dna) or set(seq) <= (nucl_rna)


transcribe_dict = {"T": "U", "t": "u"}


def transcribe(seq: str) -> str:
    res1 = []
    for char in seq:
        res1.append(transcribe_dict[char] if char in transcribe_dict else char)
        res2 = "".join(res1)
    return res2


def reverse(seq: str) -> str:
    return seq[::-1]


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


def complement(seq: str) -> str:
    res1 = []
    for char in seq:
        res1.append(complement_dict[char] if char in complement_dict else char)
        res2 = "".join(res1)
    return res2
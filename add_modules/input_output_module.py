import os


def write_as_dict(input_fastq: str) -> dict:
    seqs = {}
    with open(input_fastq) as file:
        for line in file:
            if line.startswith("@"):
                line1 = line.strip()
                name = line1.split(" ")[0]
                if not name:
                    break
                line2 = file.readline()
                sequence = line2.strip()
                line = file.readline()
                line3 = file.readline()
                quality = line3.strip()
                seqs[name] = (sequence, quality)
    return seqs


def save_filtered_sequences(seqs_checked: dict, output_fastq: str) -> None: 
    if output_fastq is None:
        output_fastq = "output_fastq.fastq"
    output_path = os.path.join("filtered", output_fastq)
    with open(output_fastq, "w") as file:
        for seq_id, (sequence, quality) in seqs_checked.items():
            file.write(f"{sequence}\n")

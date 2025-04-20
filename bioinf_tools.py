""" Bioinformatics tools 1

This script contains various functions that could be utilised 
as bioinformatics tools by the user.
"""
import os
import argparse
import logging
from typing import Union, Tuple
from statistics import mean
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction


log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


file_handler = logging.FileHandler("filter.log", mode='a')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)


def check_length(length: int, bounds: Union[Tuple[int, int], int]) -> bool:
    if isinstance(bounds, tuple):
        return bounds[0] <= length <= bounds[1]
    return length <= bounds


def check_gc(seq: SeqRecord, bounds: Union[Tuple[float, float], float]) -> bool:
    gc_content = gc_fraction(seq.seq) * 100
    if isinstance(bounds, tuple):
        return bounds[0] <= gc_content <= bounds[1]
    return gc_content <= bounds


def check_quality(seq: SeqRecord, threshold: float) -> bool:
    qualities = seq.letter_annotations["phred_quality"]
    return mean(qualities) > threshold


def filter_fastq(
    input_fastq: str,
    gc_bounds: Union[Tuple[float, float], float] = (0, 100),
    length_bounds: Union[Tuple[int, int], int] = (0, 2**32),
    quality_threshold: float = 0,
    output_fastq: str = None
) -> str:
    if output_fastq is None:
        output_fastq = "output_fastq.fastq"

    if not os.path.exists(input_fastq):
        logging.error(f"Input file not found: {input_fastq}")
        raise FileNotFoundError(f"No such file: {input_fastq}")

    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)

    filtered_records = []

    for record in SeqIO.parse(input_fastq, "fastq"):
        if (
            check_length(len(record.seq), length_bounds)
            and check_gc(record, gc_bounds)
            and check_quality(record, quality_threshold)
        ):
            filtered_records.append(record)

    SeqIO.write(filtered_records, output_path, "fastq")
    logging.info(f"{len(filtered_records)} sequences saved to {output_path}")
    return f"Filtered sequences saved to {output_path}"


def parse_args():
    parser = argparse.ArgumentParser(description="Filter FASTQ file based on length, GC content, and quality.")

    parser.add_argument("-i", "--input", required=True, help="Input FASTQ file")
    parser.add_argument("-o", "--output", help="Output FASTQ file name (optional, default: output_fastq.fastq)")

    parser.add_argument("--gc_bounds", nargs="+", type=float, default=[0, 100],
                        help="GC content bounds: one value (upper limit) or two values (lower and upper)")
    parser.add_argument("--length_bounds", nargs="+", type=int, default=[0, 2**32],
                        help="Sequence length bounds: one value (upper limit) or two values (lower and upper)")
    parser.add_argument("--quality", type=float, default=0, help="Minimum average quality score")

    return parser.parse_args()


def main():
    args = parse_args()

    gc_bounds = args.gc_bounds if len(args.gc_bounds) > 1 else args.gc_bounds[0]
    length_bounds = args.length_bounds if len(args.length_bounds) > 1 else args.length_bounds[0]

    try:
        result = filter_fastq(
            input_fastq=args.input,
            gc_bounds=gc_bounds,
            length_bounds=length_bounds,
            quality_threshold=args.quality,
            output_fastq=args.output
        )
        print(result)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()

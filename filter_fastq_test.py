import pytest
import os
import logging
from Bio import SeqIO
from bioinf_tools import filter_fastq, check_gc, check_length, check_quality


class TestInputOutputFilterFastq:
    def test_filter_fastq_nofile(self):
        with pytest.raises(FileNotFoundError):
            filter_fastq("nonexistent_file.fastq")

    def test_filter_fastq_creates_output_file(self, tmp_path):
        input_path = tmp_path / "test_input.fastq"
        input_path.write_text(
            "@seq1\nAGCGCGCG\n+\nIIIIIIII\n"
            )

        output_path = tmp_path / "out.fastq"

        filter_fastq(
            input_fastq=str(input_path),
            output_fastq=str(output_path.name),
            gc_bounds=(0, 100),
            length_bounds=(0, 50),
            quality_threshold=10
            )

        full_output_path = tmp_path / "filtered" / output_path.name
        assert full_output_path.exists(
        ), f"Output file was not created at {full_output_path}"

    def test_filter_fastq_logs_error(self, caplog):
      with caplog.at_level(logging.ERROR):
        try:
          filter_fastq("nonexistent.fastq")
        except FileNotFoundError:
          pass

      assert "Input file not found" in caplog.text

    def test_empty_input_file(self, tmp_path):
      input_file = tmp_path / "empty.fastq"
      input_file.write_text("")

      output_file = tmp_path / "out.fastq"
      filter_fastq(input_fastq=str(input_file), output_fastq=output_file.name)

      result_file = tmp_path / "filtered" / output_file.name
      records = list(SeqIO.parse(result_file, "fastq"))
      assert len(records) == 0


class TestArgsFilterFastq:
    def test_filter_fastq_excludes_short_sequences(self, tmp_path):
        input_file = tmp_path / "short.fastq"
        input_file.write_text("@short\nATCG\n+\nIIII\n")

        output_file = tmp_path / "out.fastq"
        filter_fastq(str(input_file), output_fastq=output_file.name,
                     length_bounds=(10, 100))

        result_file = tmp_path / "filtered" / output_file.name
        records = list(SeqIO.parse(result_file, "fastq"))
        assert len(records) == 0

    def test_filter_fastq_excludes_low_quality_sequences(self, tmp_path):
        input_file = tmp_path / "lowq.fastq"
        input_file.write_text("@lowq\nATCGATCG\n+\n!!!!!!!!\n")

        output_file = tmp_path / "out.fastq"
        filter_fastq(str(input_file), output_fastq=output_file.name,
                     quality_threshold=20)

        result_file = tmp_path / "filtered" / output_file.name
        records = list(SeqIO.parse(result_file, "fastq"))
        assert len(records) == 0

    def test_filter_fastq_excludes_bad_gc_sequences(self, tmp_path):
        input_file = tmp_path / "lowgc.fastq"
        input_file.write_text("@lowgc\nATATATAT\n+\nIIIIIIII\n")

        output_file = tmp_path / "out.fastq"
        filter_fastq(str(input_file),
                     output_fastq=output_file.name, gc_bounds=(40, 60))

        result_file = tmp_path / "filtered" / output_file.name
        records = list(SeqIO.parse(result_file, "fastq"))
        assert len(records) == 0
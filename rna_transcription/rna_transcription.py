def to_rna(dna_strand):
    return "".join(
        map(
            lambda nucleotide: {"G": "C", "C": "G", "T": "A", "A": "U"}.get(
                nucleotide, ""
            ),
            list(dna_strand),
        )
    )

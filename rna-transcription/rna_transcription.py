def to_rna(dna_strand):
    rna_strand = ''
    for dna in dna_strand:
        if dna == "A": rna_strand = rna_strand + 'U'
        elif dna == "G": rna_strand = rna_strand + "C"
        elif dna == "T": rna_strand = rna_strand + "A"
        elif dna == "C": rna_strand = rna_strand + "G"
    return rna_strand

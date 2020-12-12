def proteins(strand):
    meth = ["AUG"]
    phen = ["UUU", "UUC"]
    leuc = ["UUA", "UUG"]
    seri = ["UCU", "UCC", "UCA", "UCG"]
    tyro = ["UAU", "UAC"]
    cyst = ["UGU", "UGC"]
    tryp = ["UGG"]
    stop = ["UAA","UAG","UGA"]
    split = [strand[i:i+3] for i in range (0, len(strand), 3)]
    proteins = []
    for codon in split:
        if codon in meth: proteins.append("Methionine")
        elif codon in phen: proteins.append("Phenylalanine")
        elif codon in leuc: proteins.append("Leucine")
        elif codon in seri: proteins.append("Serine")
        elif codon in tyro: proteins.append("Tyrosine")
        elif codon in cyst: proteins.append("Cysteine")
        elif codon in tryp: proteins.append("Tryptophan")
        elif codon in stop: return proteins
        
    return proteins
        

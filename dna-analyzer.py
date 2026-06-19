dna = "ATCTCGCTAGCTGACGCTGACGCTGACGCTGACGCTGACACAATCGTAGTACGTTGACACGT"
print(dna.count("A"))
print(dna.count("T"))
print(dna.count("G"))
print(dna.count("C"))
print(len(dna))
A = (dna.count("A"))
T = (dna.count("T"))
G = (dna.count("G"))
C = (dna.count("C"))
print(A+T+G+C)
gc = ((G+C) / len(dna)) *100
print(gc)
at = ((A+T) / len(dna)) *100
print(at)
if gc>at:
    print("Adn riche en GC")
else:
    print("Adn riche en AT")
if (A+T+G+C) == len(dna):
    print("sequence valide")
else:
    print("sequence invalide")
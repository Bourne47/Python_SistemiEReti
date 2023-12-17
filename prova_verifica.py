def contaNucleotidi(genoma):
    for carattere in genoma:
        if (carattere == "A"):
            na+=1
        elif(carattere == "T"):
            nt+=1
        elif(carattere == "G"):
            ng+=1
        elif(carattere == "C"):
            nc+=1
    print(f"A: {na}, T: {nt}, G: {ng}, C: {nc}")

def contaNucleotidi2(genoma):
    dizNucleotidi = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for char in genoma:
        dizNucleotidi[char] += 1
    return dizNucleotidi

def contaNucleotidi3(genoma, nucleotide):
    return len([x for x in genoma if x == nucleotide])

def cercaProteinaSpike(genoma):
    proteinaSpike = "ATGTTTGTTTTT"
    for i, _ in enumerate(genoma[:-12]):
        if genoma[i:i+len(proteinaSpike)] == proteinaSpike:
            return i
    return -1    
    
def main():
    genoma = ""
    #na, nt, ng, nc = 0, 0, 0, 0
    file = open("covid-19_gen1.txt", "r")
    for riga in file:
        riga = riga[:-1]
        genoma = genoma + riga
    file.close()
    print(genoma)
    #contaNucleotidi(genoma)
    print(contaNucleotidi2(genoma))
    print(cercaProteinaSpike(genoma))
    


if __name__ == "__main__":
    main()
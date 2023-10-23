stringa = "ciao come va"
vocali = "AaEeIiOoUu"
stringa = [carattere for carattere in stringa if carattere not in vocali]
print("".join(stringa))
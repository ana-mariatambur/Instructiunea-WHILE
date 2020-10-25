"""Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi.
 Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. """
i=0
p=0
n=0
spoz=0
sneg=0

while i<12:
    t=eval(input("introduceti temperatura dintr-o luna:"))
    if t>=0:
        spoz+=t
        p+=1
        if t<=0:
            sneg+=t
            n+=1
            i=i+1

            if p>0:
                media_poz=float(spoz/p)
                print(f"media pozitiva este {round(media_poz,2)}")
            if p<0:
                media_neg=float(sneg/n)
                print(f"media negativa este {round(media_neg,2)}")
def suma(liczba):
    wynik = 0
    while liczba !=0:
        wynik += liczba % 10
        liczba //= 10
    return wynik

def czyJest13(liczba):
    cyfra = 0
    cyfrap = 0
    while True:
        cyfrap=cyfra
        cyfra = liczba % 10
        liczba //= 10
        if ((cyfra == 1) and (cyfrap == 3)):
            return True
        if (0 == liczba):
            return False
    return False



n = int(input("Podaj liczbe max:"))
cn = 139
it = 0
while cn < n:
    if (suma(cn) == 13):
        if (czyJest13(cn)):
            print(cn)
            it+=1
        cn+=8
    cn+=1
print(it)




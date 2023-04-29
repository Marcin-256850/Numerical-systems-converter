def system(cyfra):
    typ = input("Podaj system na który ma być przeliczona podana liczba(szesnastkowy lub dwojkowy:")
    if typ == "szesnastkowy":
        liczba = hex(int(cyfra))
        print("Oto liczba w systemie szesnastkowym:", liczba)
    elif typ == "dwojkowy":
        liczba = bin(int(cyfra))
        print("Oto liczba w systemie dwojkowym:", liczba)
    else:
        print("podaj poprawna nazwe z dwoch dostepnych")
        system(cyfra)


while True:
    dec = input("Podaj liczbę dziesiętną:")
    if dec.isdigit():
        system(dec)
        while 1:
            koniec = input("Czy chcesz przeliczyc kolejna liczbe?(tak/nie): ")
            if koniec == "tak":
                break
            elif koniec == "nie":
                exit(0)
            else:
                print("Podaj jedna z dwoch dosetpnych opcji")
    else:
        print("Wartość nie jest liczbą całkowitą.")

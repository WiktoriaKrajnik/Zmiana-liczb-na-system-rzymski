def tworzenie_tekstu(n):
    global rzymski
    global tekst
    global liczba
    p = 0
    p += liczba // n
    for i in range(0, p):
        tekst += rzymski.get(n)
    liczba -= n * p

rzymski = {1 : 'I', 5: 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
liczba = int(input("Wpisz liczbę, którą chcesz zmienić na system rzymski: "))
tekst = ""
n = 0
while liczba != 0:
    if liczba >= 900:
        if liczba >=1000:
            n = 1000
        elif liczba >= 900 and liczba <= 1000:
            tekst += rzymski.get(100) + rzymski.get(1000)
            liczba -= 900
    elif liczba >= 400:
        if liczba >=500:
            n = 500
        elif liczba >= 400 and liczba <= 500:
            tekst += rzymski.get(100) + rzymski.get(500)
            liczba -= 400
    elif liczba >= 90:
        if liczba >=100:
           n = 100
        elif liczba >= 90 and liczba <= 100:
            tekst += rzymski.get(10) + rzymski.get(100)
            liczba -= 90
    elif liczba >= 40:
        if liczba >=50:
            n = 50
        elif liczba >= 40 and liczba <= 50:
            tekst += rzymski.get(10) + rzymski.get(50)
            liczba -= 40
    elif liczba >= 9:
        if liczba >=10:
            n = 10
        elif liczba >= 9 and liczba <= 10:
            tekst += rzymski.get(1) + rzymski.get(10)
            liczba -= 9
    elif liczba >= 4:
        if liczba >=5:
            n = 5
        elif liczba >= 4 and liczba <= 5:
            tekst += rzymski.get(1) + rzymski.get(5)
            liczba -= 4
    elif liczba >= 1:
        n = 1
    if n != 0 :
        tworzenie_tekstu(n)
print(tekst)
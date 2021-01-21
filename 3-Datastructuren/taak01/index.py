getallen = {1: 'een', 2: 'twee', 3: 'drie', 4: 'vier', 5: 'vijf', 6: 'zes', 7: 'zeven', 8: 'acht', 9: 'negen', 10: 'tien'}
getal = int (input ("Vul een getal van 1 tot 10 in"))
if getal in range(1,10) :
    print(getallen[getal])
else:
    getal = int (input ("Vul een getal van 1 tot 10 in"))
    print(getallen[getal])


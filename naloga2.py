data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}


def najvecja_vrednost(data):
        najvecja_vrednost_prices = data["prices"]
        x = max(najvecja_vrednost_prices)
        najvecja_vrednost_volume = data["volume"]
        y = max(najvecja_vrednost_volume)
        najvecja_vrednost = [x,y]
        vrednosti = najvecja_vrednost
        print(vrednosti)

najvecja_vrednost(data)

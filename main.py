class Oyin:
    def __init__(self, nom):
        self.nom = nom


class Gamer:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game.nom)

    def show(self):
        print(self.games)


o1 = Oyin("PUBG")
o2 = Oyin("Minecraft")

g1 = Gamer()
g1.add_game(o1)
g1.add_game(o2)
g1.show()

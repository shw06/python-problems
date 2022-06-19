class Player:
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name


p1 = Player('Salah')
p2 = Player('Henderson')

print("Name: ",p1.name)
print("Team: ",p1.teamName)
print("Name: ",p2.name)
print("team: ",p2.teamName)
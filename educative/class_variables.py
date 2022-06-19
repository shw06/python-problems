class Player:
    teamName = "Liverpool" #class variable

    def __init__(self, name):
        self.name = name #instance variable


p1 = Player('Salah')
p2 = Player('Henderson')

print("Name: ",p1.name)
print("Team: ",p1.teamName)
print("Name: ",p2.name)
print("team: ",p2.teamName)
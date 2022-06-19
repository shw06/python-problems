class Player:
    teamName = "Liverpool"

    def __init__(self,name):
        self.name = name
        self.formerTeams = []


p1 = Player('Ronaldo')
p1.formerTeams.append('MCFC')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("name: ",p1.name)
print("Team: ",p1.teamName)
print(p1.formerTeams)
print("name: ",p2.name)
print("Team: ",p2.teamName)
print(p2.formerTeams)

'''Concept: Instance and Class Attributes

Q8. Create a class named Player with the following requirements:

A class variable called player_count

Instance variables called name and level

The class should keep track of how many Player objects are created.'''
# answer
class Player:
    player_count = 0
    def __init__(self,name,level):
        self.name = name 
        self.level = level
        Player.player_count +=1

p1 = Player("Aritra",435)
p2 = Player("hagh",243)
print(Player.player_count)
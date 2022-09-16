players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# # Assignment Tasks
# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    @classmethod
    def get_team(cls, data):
        playerobj = []
        for dict in data:
            playerobj.append(cls(dict))
        return playerobj

#heres my own bonus lol
#Access the values of the keys within the list of dictionaries using class instances.
player_kevin = Player(players[0])
print(players[0]["name"])
player_jason = Player(players[1])
print(players[1]["name"], "| Age:", players[1]["age"])
player_kyrie = Player(players[2])
print(players[2].values())

print("------")

# Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
challenge_kevin = Player(kevin)
print(challenge_kevin.position)
challenge_jason = Player(jason)
print(challenge_jason.age)
challenge_kyrie = Player(kyrie)
print(challenge_kyrie.team)

print(" ----- ")

new_team = []
for playerdict in players:
    player = Player(playerdict)
    new_team.append(player)
print(new_team)
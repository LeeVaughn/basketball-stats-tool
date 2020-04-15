# import data
from constants import TEAMS, PLAYERS

# clean data
    # create separate Lists for TEAMS and PlAYERS?
def create_teams(teams):
    return teams


def create_players(players):
    for player in players:
        # converts height string to int
        player["height"] = int(player["height"][0:2])

        # converts experience string to boolean
        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False

        # splits guardian field into a List of strings and uses list comprehension to remove whitespace
        guardians_split = player["guardians"].split("and")
        player["guardians"] = [guardian.strip(" ") for guardian in guardians_split]

    return players


# balance the number of players equally between teams
def draft(teams_list, players_list):
    # creates global variables for teams so they can be accessed in the menu function
    global panthers, bandits, warriors
    experienced = []
    inexperienced = []
    panthers = []
    bandits = []
    warriors = []

    # splits players into separate lists based on experience key
    for player in players_list:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    # iterates over list to divide experienced players equally between teams
    for num, player in enumerate(experienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    # iterates over list divide inexperienced players equally between teams
    for num, player in enumerate(inexperienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    return panthers, bandits, warriors


# displays team stats
def display_stats(team, players):
    # variables to track player stats
    exp_players = 0
    inexp_players = 0
    height = 0
    names_list = []
    guardians_list = []
    player_guardians = []

    # iterates over players list to create stats
    for player in players:
        # separates experienced and inexperienced players in to separate lists
        if player["experience"] == True:
            exp_players += 1
        elif player["experience"] == False:
            inexp_players += 1

        height += player["height"]
        names_list.append(player["name"])
        guardians_list.append(player["guardians"])
        # I wasn't completely sure I understood the Exceeds part of the Clean up data section so I created this list
        player_guardians.append({"player": player["name"], "guardians": player["guardians"]})

    # uses list comprehension to create a string of player names
    names = ", ".join([str(name) for name in names_list])
    # uses nested list comprehension to create a string of guardian names
    guardians = ", ".join([str(guardian) for sublist in guardians_list for guardian in sublist])

    print("\nDisplaying stats for the {}.\n".format(team))
    print("There are {} players on the team,".format(len(players)))
    print("{} experienced players and {} inexperienced.".format(exp_players, inexp_players))
    print("The average player height is {} inches.\n".format(height / len(players)))
    print("Players:", names, "\n")
    print("Guardians:", guardians, "\n")
    print(player_guardians)


# create a menu for user interaction
def menu(teams_list, players_list):
    teams = create_teams(teams_list)
    players = create_players(players_list)
    rosters = draft(teams_list, players_list)
    # display_stats(TEAMS[0], panthers)
    print("\nWelcome to the BasketBall Stats Tool!")
    print("""
        Enter "Panthers" to see stats for the Panthers.
        Enter "Bandits" to see stats for the Bandits.
        Enter "Warriors" to see stats for the Warriors.
        Enter "Quit" to exit the program.
    """)

    while True:
        try:
            response = input("> ")
            print(response.lower())
        except ValueError as err:
            print("There has been an error", err)
    # user should be able to display a given teams stats
    # user should be able to quit
    # user should be reprompted with the main menu until they quit the program

if __name__ == "__main__":
    # run initial function
    menu(TEAMS, PLAYERS)
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
    # panthers = [{
    #     "team": TEAMS[0],
    #     "num_players": 0,
    #     "num_exp": 0,
    #     "num_inexp": 0,
    #     "avg_height": 0
    # }]
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


# display stats
def display_stats(team, players):
    exp_players = 0
    inexp_players = 0
    height = 0

    # calculate stats
    for player in players:
        if player["experience"] == True:
            exp_players += 1
        elif player["experience"] == False:
            inexp_players += 1

        height += player["height"]

    # team name
    print("Displaying stats for the {}.".format(team))
    # number of players on team
    print("There are {} players on the team,".format(len(players)))
    # number of experience/inexperienced players (maybe combine these two steps?)
    print("{} experienced players and {} inexperienced.".format(exp_players, inexp_players))
    # average height of the team
    print("The average player height is {} inches.".format(height / len(players)))
    # player names seperated by commas
    # guardians of all players seperated by commas


# create a menu for user interaction
def menu(teams_list, players_list):
    teams = create_teams(teams_list)
    players = create_players(players_list)
    rosters = draft(teams_list, players_list)

    # print(teams)
    # print(players)
    # print(rosters)
    # user should be able to display a given teams stats
    display_stats(TEAMS[0], panthers)
    print(panthers)
    # user should be able to quit
    # user should be reprompted with the main menu until they quit the program

if __name__ == "__main__":
    # run initial function
    menu(TEAMS, PLAYERS)
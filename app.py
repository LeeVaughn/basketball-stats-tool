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
    experienced = []
    inexperienced = []
    panthers = []
    bandits = []
    warriors = []

    # teams should have an equal number of experienced and inexperienced players
        # might need to split experienced and inexperienced players into separate Lists for this?
    for player in players_list:
        if player["experience"] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)

    for num, player in enumerate(experienced, start = 1):
        if num % 3 == 0:
            panthers.append(player)
        elif num % 2 == 0:
            bandits.append(player)
        else:
            warriors.append(player)

    # print(experienced)
    # print(len(experienced))
    # print(len(inexperienced))
    return panthers, bandits, warriors


# display stats
    # team name
    # number of players on team
    # number of experience/inexperienced players (maybe combine these two steps?)
    # average height of the team
    # player names seperated by commas
    # guardians of all players seperated by commas


# create a menu for user interaction
def menu(teams_list, players_list):
    teams = create_teams(teams_list)
    players = create_players(players_list)
    rosters = draft(teams_list, players_list)

    # print(teams)
    # print(players)
    print(rosters)
    # user should be able to display a given teams stats
    # user should be able to quit
    # user should be reprompted with the main menu until they quit the program

if __name__ == "__main__":
    # run initial function
    menu(TEAMS, PLAYERS)
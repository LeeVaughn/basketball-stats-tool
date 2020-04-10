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
    return players
    # convert experienced string to boolean
    # split guardian field into a List of strings

# balance the number of players equally between teams
    # teams should have an equal number of experienced and inexperienced players
        # might need to split experienced and inexperienced players into separate Lists for this?

# display stats
    # team name
    # number of players on team
    # number of experience/inexperienced players (maybe combine these two steps?)
    # average height of the team
    # player names seperated by commas
    # guardians of all players seperated by commas

# create a menu for user interaction
def draft(teams_list, players_list):
    teams = create_teams(teams_list)
    players = create_players(players_list)

    print(teams)
    print(players)
    # user should be able to display a given teams stats
    # user should be able to quit
    # user should be reprompted with the main menu until they quit the program

if __name__ == "__main__":
    # run initial function
    draft(TEAMS, PLAYERS)
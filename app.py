import constants


def run_app():

    myPlayers = []
    myTeams = []

    for player in constants.PLAYERS:
        myPlayers.append(player)
    for team in constants.TEAMS:
        myTeams.append(team)
    print(myPlayers)
    print(myTeams)


if __name__ == '__main__':
    run_app()

import constants


def run_app():

    myPlayers = []
    myTeams = []

    for player in constants.PLAYERS:
        myPlayers.append(player)
    for team in constants.TEAMS:
        myTeams.append(team)

    print(len(myPlayers))

    teamNum = 0

    for player in myPlayers:
        if teamNum == 3:
            teamNum = 0
        player.update({"Team": myTeams[teamNum]})
        teamNum += 1


    for player in myPlayers:
        print(player)

    print("\n\nWelcome to the Team Stats Tool! \n\n")

    option = input("What would you like to do first?\n\n\n"
          "Enter one of the following options: \n\n"
          "1. Display Team Stats \n"
          "2. Quit \n\n"
          "Enter choice here: ")

    if option.upper() == "1":
        for team in myTeams:
            print(team)
        print("Goodbye!!!!!!!!!!!!!!!")
    elif option.upper() == "2":
        print("hello theareslksadfj")


if __name__ == '__main__':
    run_app()

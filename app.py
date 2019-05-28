import constants


def run_app():

    myPlayers = []
    myTeams = []

    for player in constants.PLAYERS:
        myPlayers.append(player)
    for team in constants.TEAMS:
        myTeams.append(team)

    print("\n\nWelcome to the Team Stats Tool! \n\n")

    option = input("What would you like to do first?\n\n\n"
          "Enter one of the following options: \n\n"
          "1. Display Team Stats \n"
          "2. Quit \n\n"
          "Enter choice here: ")

    if option.upper() =="1":
        pass
        print("Goodbye!!!!!!!!!!!!!!!")
    elif option.upper() =="2":
        print("hello theareslksadfj")

if __name__ == '__main__':
    run_app()

import constants


def run_app():

    myPlayers = []
    myTeams = []

    for player in constants.PLAYERS:
        myPlayers.append(player)
    for team in constants.TEAMS:
        myTeams.append(team)

    teamNum = 0

    for player in myPlayers:
        if teamNum == 3:
            teamNum = 0
        player.update({"Team": myTeams[teamNum]})
        teamNum += 1

    print("\n**********************************************"
          "\n****** Welcome to the Team Stats Tool! *******"
          "\n**********************************************\n")

    option = input("What would you like to do first?\n"
          "Enter one of the following options: \n\n"
          "1. Display Team Stats \n"
          "2. Quit \n\n"
          "Enter choice here: ")

    if option.upper() == "1":  # User wants to see team stats! Enter loop below
        counter = 1  # Set a counter so that we can loop through the teams and put a number in front of each
        print("\n")
        for team in myTeams: # Print out the list of teams to see stats for
            print("{}.) {}".format(counter, team))
            counter += 1

        validOption = False

        while validOption != True:

            try:
                option = input("\nEnter the number above for the team you'd like to see stats for: ")
                if 0 < int(option) < counter:
                    validOption = True
                    print("they chose a valid team!")
                else:
                    print("Please choose a valid option")
            except ValueError as e:
                print("\nOops, that was a bogus entry...Please try again with a value from 1 to {}. Error message: {}".format(len(myTeams), e))

    elif option.upper() == "2":
        print("\nGoodbye! It's been fun. Sorry we couldn't make this work :( I'm sure it's not me, it's you....right?")


if __name__ == '__main__':
    run_app()

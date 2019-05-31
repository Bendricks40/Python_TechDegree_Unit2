import constants

myPlayers = []
myTeams = []

def import_and_balance():


    for player in constants.PLAYERS:
        myPlayers.append(player)
    for team in constants.TEAMS:
        myTeams.append(team)

    # Cleaning up the guardian list to be a list of strings instead of one or more guardians as a single string
    # Also making the "height" string a list that is comprised of first
    # the numeric value and then unit of measure (inches in this data set)
    for player in myPlayers:
        guardianList = (player.get("guardians")).split(" and ")
        player.update({"guardians": guardianList})
        heightStats = (player.get("height")).split(" ")
        player.update({"height": heightStats})

    teamNum = 0

    # iterate through each player and assign them to a team.
    for player in myPlayers:
        if teamNum == 3:
            teamNum = 0
        player.update({"Team": myTeams[teamNum]})
        teamNum += 1


def display_teams():
    counter = 1  # Set a counter so that we can loop through the teams and put a number in front of each
    print("\n")
    for team in myTeams:  # Print out the list of teams to see stats for
        print("{}.) {}".format(counter, team))
        counter += 1


def run_app():

    import_and_balance()

    print("\n**********************************************"
          "\n****** Welcome to the Team Stats Tool! *******"
          "\n**********************************************\n")

    keepgoing = True

    while keepgoing == True:
        option = input("Enter one of the following options: \n\n"
                       "1. Display Team Stats \n2. Quit \n\nEnter choice here: ")

        if option.upper() == "1":  # User wants to see team stats! Enter loop below
            display_teams()
            counter = len(myTeams)
            validOption = False

            while validOption != True:

                try:
                    option = input("\nEnter the number above for the team you'd like to see stats for: ")
                    if 0 < int(option) < counter+1:
                        validOption = True
                        # put team stats here--team Name, # of total players, Names
                        print("\nStats for Team Name: {}\n".format(myTeams[int(option)-1]))
                        totalPlayers = 0
                        totalHeight = 0
                        playerString = " "
                        totalExperienced = 0
                        totalInexperienced = 0
                        for player in myPlayers:
                            # confirm as we loop through the players if they belong to the selected team
                            if player.get("Team") == myTeams[int(option)-1]:
                                totalPlayers += 1
                                # Then add their height to the total height pool
                                totalHeight += int(player.get("height")[0])
                                # and now verify if they are experienced or inexperienced, and increment appropriate bucket
                                if player.get("experience") == "YES":
                                    totalExperienced += 1
                                else:
                                    totalInexperienced += 1
                                # now start building out the player string for all players on the team:
                                if totalPlayers == 1:
                                    playerString += (player.get("name"))
                                else:
                                    playerString += (", " + player.get("name"))
                        print("* Total Players: {}".format(totalPlayers))
                        print("* Here are all the players: \n  {}".format(playerString))
                        print("* There are {} experienced players on the team, and {} inexperienced players".format(totalExperienced, totalInexperienced))
                        print("* Average height of team: {} inches\n\n".format(round(totalHeight/totalPlayers)))



                    else:
                        print("Please choose a valid option")
                except ValueError as e:
                    print("\nOops, that was a bogus entry..."
                          "Please try again with a value from 1 to {}. Error message: {}".format(len(myTeams), e))

            choice = input("\nWould you like to view another team? Enter 1 for Yes or 2 to quit/exit.")
            if choice == "1":
                keepgoing = True
            else:
                keepgoing = False
                print("\n\nThanks for using this tool! Goodbye.\n\n")

        elif option.upper() == "2":
            print("\nGoodbye! It's been fun. Sorry we couldn't make this work :( "
                  "I'm sure it's not me, it's you....right?")


if __name__ == '__main__':
    run_app()

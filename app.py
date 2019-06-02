import constants

myPlayers = []
myTeams = []


def import_and_balance():
    """this function takes the data from constants file and puts it in my own
    objects, and then cleans up the data per instructions in project"""
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

    experiencedteamNum = 0
    inexperiencedteamNum = 0

    # iterate through each player and assign them to a team, evenly balancing experienced and inexperienced players.
    for player in myPlayers:
        if player.get("experience") == "YES":
            if experiencedteamNum == 3:
                experiencedteamNum = 0
            player.update({"Team": myTeams[experiencedteamNum]})
            experiencedteamNum += 1
        else:  # not experienced...we found a noob!
            if inexperiencedteamNum == 3:
                inexperiencedteamNum = 0
            player.update({"Team": myTeams[inexperiencedteamNum]})
            inexperiencedteamNum += 1


def display_teams():
    """this function simply spits out the teams in a numbered list"""
    counter = 1  # Set a counter so that we can loop through the teams and put a number in front of each
    print("\n")
    for team in myTeams:  # Print out the list of teams to see stats for
        print("{}.) {}".format(counter, team))
        counter += 1


def run_app():
    """this function runs the main logic of the program so user can choose a team to display stats for!"""
    import_and_balance()

    print("\n**********************************************"
          "\n****** Welcome to the Team Stats Tool! *******"
          "\n**********************************************\n")

    keepgoing = True

    while keepgoing == True:
        option = input("\nEnter one of the numbers below for the following options: \n\n"
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
                        guardianString = " "
                        totalExperienced = 0
                        totalInexperienced = 0
                        for player in myPlayers:
                            # confirm as we loop through the players if they belong to the selected team
                            if player.get("Team") == myTeams[int(option)-1]:
                                totalPlayers += 1
                                # Then if they are on selected team, add their height to the total height pool
                                totalHeight += int(player.get("height")[0])
                                # and now verify if they are experienced or inexperienced, and increment appropriately
                                if player.get("experience") == "YES":
                                    totalExperienced += 1
                                else:
                                    totalInexperienced += 1
                                # now start building out the player string for all players on the team:
                                if totalPlayers == 1:
                                    playerString += (player.get("name"))
                                else:
                                    playerString += (", " + player.get("name"))
                                # And finally, build out the guardian string:
                                if totalPlayers == 1:
                                    guardianString += ((", ".join(player.get("guardians"))) + ",")
                                else:
                                    guardianString += (" " + (", ".join(player.get("guardians"))) + ",")

                        # couldn't figure out a better way to do this, but my guardian string
                        # building logic above leaves the last entry ending in a comma, even
                        # though there are no further entries... So chopping off last character :)
                        guardianString = guardianString[:-1]

                        print("* Total Players: {}".format(totalPlayers))
                        print("* Here are all the players: \n  {}".format(playerString))
                        print("* There are {} experienced players on the team, and {} inexperienced players".format(totalExperienced, totalInexperienced))
                        print("* Average height of team: {} inches".format(round(totalHeight/totalPlayers)))
                        print("* Guardians of players: \n  {}\n\n".format(guardianString))

                    else:
                        print("Please choose a valid option")
                except ValueError as e:
                    print("\nOops, that was a bogus entry..."
                          "Please try again with a value from 1 to {}. Error message: {}".format(len(myTeams), e))

            input("Press Enter to continue...")

        elif option.upper() == "2":
            print("\nGoodbye! It's been fun. Sorry we couldn't make this work :( "
                  "I'm sure it's not me, it's you....right???")
            keepgoing = False


if __name__ == '__main__':
    run_app()

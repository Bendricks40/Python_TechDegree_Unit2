import constants


def run_app():

    myPlayers = []

    for player in constants.PLAYERS:
        myPlayers.append(player)
    print(myPlayers)



if __name__ == '__main__':
    run_app()

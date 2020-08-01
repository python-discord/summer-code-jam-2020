import player


def login():
    username = input('Username:')
    password = input('Password?')
    ##need to add DB Lookup to validate credentials.
    _acitveplayer = player.Player(username,password)
    return _acitveplayer

def createPlayer():
    username = input('What is your username?')
    ## need to add DB look up to check that username already doesn't exist
    password = input('What is your password?') 
    ## need to add DB insert for new player
    newplayer = player.Player(username, password)
    return newplayer

def main():
    print('Hello welcome to MUD\n') 

    if input('Are you a new Player? (Y/N)') is 'Y':
        currentPlayer = createPlayer()
    else:
        currentPlayer = login()
    print(currentPlayer.checkStats())
    

main()
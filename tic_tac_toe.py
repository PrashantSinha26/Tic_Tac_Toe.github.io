
boared={'7':' ','8':' ','9':' ',
        '4':' ','5':' ','6':' ',
        '1':' ','2':' ','3':' '}


def print_boared(boared):

    print(boared['7'] + '|' + boared['8'] + '|' + boared['9'])
    print('-+-+-')
    print(boared['4'] + '|' + boared['5'] + '|' + boared['6'])
    print('-+-+-')
    print(boared['1'] + '|' + boared['2'] + '|' + boared['3'])

def game():

    turn='X'
    count=0

    while True:

        print_boared(boared)
        print(f"It is turn of {turn} and specify the location you want to go ")

        move_loc=input("Enter the location on boared : ")

        if boared[move_loc]==' ':
            boared[move_loc]=turn
            count+=1
        else:
            print("Sorry this cell location is filled, Please choose another one !!!")

            continue

        if count>=5:

            if boared['7']==boared['8']==boared['9'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break

            if boared['4']==boared['5']==boared['6'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break

            if boared['1']==boared['2']==boared['3'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break

            if boared['1']==boared['4']==boared['7'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break
            
            if boared['2']==boared['5']==boared['8'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break
            if boared['3']==boared['6']==boared['9'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break
            if boared['1']==boared['5']==boared['9'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break
            if boared['3']==boared['5']==boared['7'] != ' ':
                print_boared(boared)
                print("\nGame Over\n")
                print(f"Player {turn} won the game 🎉🎉🎉")
                break
        
        if count==9:
            print("\nGame Over 😴\n")
            print("The Game is Tie 😮")
            break
        
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'
        
    play_again=input("DO you want to play again ? (y/n) : ")

    if play_again.lower()=='y':
        for key in boared:
            boared[key] = ' '

        game()

game()
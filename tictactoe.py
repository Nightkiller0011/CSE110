import random
def main():
    gameloop = "y"
    while gameloop == "y":
            game_data = [" "," "," "," "," "," "," "," "," "]
            key_data = [1,2,3,4,5,6,7,8,9]
            loop = "y"
            while loop == "y":
                O = random.randint(0, 8)
                display(key_data)
                spot = int(input(f"What spot would you like to choose? "))
                game_data[spot-1] = "X"
                turnO = "y"
                while turnO == "y":
                    if game_data[O] == " ":
                        game_data[O] = "O"
                        turnO = "n"
                    else:
                        O = random.randint(0, 8)
                display(game_data)
                if (game_data[0] == "X" and game_data[3] == "X" and game_data[6] == "X") or (game_data[1] == "X" and game_data[4] == "X" and game_data[7] == "X") or (game_data[2] == "X" and game_data[5] == "X" and game_data[8] == "X") or (game_data[0] == "X" and game_data[4] == "X" and game_data[8] == "X") or (game_data[2] == "X" and game_data[4] == "X" and game_data[6] == "X") or (game_data[0] == "X" and game_data[1] == "X" and game_data[2] == "X") or (game_data[3] == "X" and game_data[4] == "X" and game_data[5] == "X") or (game_data[6] == "X" and game_data[7] == "X" and game_data[8] == "X"):
                    print(f"\nPlayer 1 wins! \n")
                    loop = "n"
                elif (game_data[0] == "O" and game_data[3] == "O" and game_data[6] == "O") or (game_data[1] == "O" and game_data[4] == "O" and game_data[7] == "O") or (game_data[2] == "O" and game_data[5] == "O" and game_data[8] == "O") or (game_data[0] == "O" and game_data[4] == "O" and game_data[8] == "O") or (game_data[2] == "O" and game_data[4] == "O" and game_data[6] == "O") or (game_data[0] == "O" and game_data[1] == "O" and game_data[2] == "O") or (game_data[3] == "O" and game_data[4] == "O" and game_data[5] == "O") or (game_data[6] == "O" and game_data[7] == "O" and game_data[8] == "O"):
                    print(f"\nPlayer 2 wins! \n")
                    loop = "n"
                elif game_data[0] != " " and game_data[1] != " " and game_data[2] != " " and game_data[3] != " " and game_data[4] != " " and game_data[5] != " " and game_data[6] != " " and game_data[7] != " " and game_data[8] != " ":
                    print(f"\nNobody wins! \n")
                    loop = "n"
                # loop = input("more? ")
            gameloop = input(f"\nWould you like to play again?(y/n) ")



def display(loop):
    print(f"\n{loop[0]} | {loop[1]} | {loop[2]}\n--+---+--\n{loop[3]} | {loop[4]} | {loop[5]}\n--+---+--\n{loop[6]} | {loop[7]} | {loop[8]}\n")


main()
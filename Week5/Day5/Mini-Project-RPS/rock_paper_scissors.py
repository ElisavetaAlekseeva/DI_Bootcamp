from ast import While
import game as g

results = {'won': 0, 'lose': 0, 'drew':0}

def get_user_menu_choice():
    users_choise = input("""
    Menu:
    (g) Play a new game
    (x) Show scores and exit
    Your choice: """)
    if users_choise == 'g' or users_choise == 'x':
        return users_choise
    else: 
        print('Invalid')
        return get_user_menu_choice()

    


def print_results(results):
    print(f"""
    Game Results:
     You won {results['won']} times
     You lose {results['lose']} times
     You drew {results['drew']} times

    Thank you for playing!
    """)
    

def main(results):
    game = g.Game()
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            game.play(results)
        elif choice == 'x':
            print_results(results)
            break


main(results)

from controllers.game_controller import GameController

def main_menu():
    print("\n=== Collection Organizer ===")
    print("1. Add a new game")
    print("2. List your games")
    print("3. Remove a game")
    print("4. Exit")

def main():

    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name of the game: ")
            platform = input("Platform (Playstation, Xbox, Nintendo, etc.): ")
            release_year = input("Year the game was released: ")
            developer = input("Developed by: ")
            condition = input("Condition of the item: ")
            controller.add_game(name, platform, release_year, developer, condition)

        elif choice == '2':
            controller.list_games()

        elif choice == '3':
            controller.list_games()
            index = int(input("Insert the number of the game to be removed from the list: ")) - 1
            controller.remove_game(index)

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == '__main__':
    controller = GameController()
    controller.add_game("Super Mario Bros Wonder", "Nintendo Switch", "2023", "Nintendo", "Brand-new")
    games = controller.list_games()
    print(games)
    controller.close()

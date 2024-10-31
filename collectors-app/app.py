from controllers.game_controller import GameController

controller = GameController()

def add_game(name, platform, release_year, developer, condition):
    controller.add_game(name, platform, release_year, developer, condition)

def list_games():
    return controller.list_games()

def remove_game(game_id):
    controller.remove_game(game_id)

from db.db_connection import DatabaseConnection
from models.game import Game

class GameController:
    def __init__(self):
        self.db = DatabaseConnection()

    def close(self):
        self.db.cursor.close()
        self.db.connection.close()

    def add_game(self, name, platform, release_year, developer, condition):
        game = Game(name, platform, release_year, developer, condition)
        try:
            self.db.cursor.execute("""
            INSERT INTO games (name, platform, release_year, developer, condition)
            VALUES (%s, %s, %s, %s, %s);
            """, (game.name, game.platform, game.release_year, game.developer, game.condition))
            self.db.connection.commit()
            print(f"Game '{game.name}' added successfully!")
        except Exception as e:
            print("Error when adding the game: ", e)

    def list_games(self):
        try:
            self.db.cursor.execute("SELECT * FROM games;")
            games = self.db.cursor.fetchall()
            return [
                {'id': game[0], 'name': game[1], 'platform': game[2], 'release_year': game[3],
                 'developer': game[4], 'condition': game[5]}
                for game in games
            ] if games else []
        except Exception as e:
            print("Error loading the game list.", e)
            return []

    def remove_game(self, game_id):
        try:
            self.db.cursor.execute("DELETE FROM games WHERE id = %s;", (int(game_id),))
            self.db.connection.commit()
            if self.db.cursor.rowcount > 0:
                print(f"Game with ID'{game_id}' has been removed successfully!")
            else:
                print("Game ID not found. Try again.")
        except Exception as e:
            print("Error deleting the game. ", e)
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

            if not games:
                print("No game registered yet.")
            else:
                for idx, game in enumerate(games, start=1):
                    print(f"{idx}. ID: {game[0]}, Name: {game[1]}, Platform: {game[2]}, Release Year: {game[3]}, Developer: {game[4]}, Condition: {game[5]}")
        except Exception as e:
            print("Error loading the game list. ", e)

    def remove_game(self, game_id):
        try:
            self.db.cursor.execute("DELETE FROM games WHERE id = %s;", (game_id,))
            self.db.connection.commit()
            if self.db.cursor.rowcount > 0:
                print(f"Game with ID'{game_id}' has been removed successfully!")
            else:
                print("Game ID not found. Try again.")
        except Exception as e:
            print("Error deleting the game. ", e)
class Game:
    def __init__(self, name, platform, release_year, developer, condition):
        self.name = name
        self.platform = platform
        self.release_year = release_year
        self.developer = developer
        self.condition = condition

    def __repr__(self):
        return f"{self.name} for {self.platform}, released in {self.release_year} by {self.developer}, condition: {self.condition}"
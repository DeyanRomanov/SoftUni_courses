from project_hero.dark_knight import DarkKnight


class BladeKnight(DarkKnight):

    def __init__(self, username: str, level: int):
        DarkKnight.__init__(self, username, level)

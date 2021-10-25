class GameState:
    def __init__(self):
        """
        Доска, состаящая из списка списков, где символ "." является ячейкой для хода игроков,
        символ "Gl" является ячейкой для вставки горизонтальных перекрытий,
        символ "Vl" является ячейкой для вставки вертикальных перекрытий
        Пробел является пустой ячейкой, не изменяемаяBl.
        Pl1 и Pl2 обозначение фишек первого и второго игрокаBl.
        """
        self.board = [
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Pl2", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
           ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"],
            ["Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl", "Cross", "Gl"],
            ["Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Pl1", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl", "Vl", "Bl"]
        ]
        self.pl1ToMove = True
        self.movelog = []

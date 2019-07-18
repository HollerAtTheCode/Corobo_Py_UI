class Field:

    def __init__(self, ident, x_pos, y_pos, type):
        self.ident = ident
        # 25 Prozent der Groesse wars in Unity
        self.height = 90
        self.width = 90
        self.x_px = 60 + x_pos * self.height
        self.y_px = 15 + y_pos * self.width
        self.type = type

class Field:

    def __init__(self, ident, x_pos, y_pos, type):
        self.ident = ident

        # 25 Prozent der Groesse wars in Unity
        self.height = 50
        self.width = 50
        self.x_px = 10 + x_pos * self.height
        self.y_px = 10 + y_pos * self.width
        self.type = type
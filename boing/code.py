import pytch


class BoingBackground(pytch.Stage):
    Backdrops = ["table.png"]


class PlayerBat(pytch.Sprite):
    Costumes = ["player-normal.png"]

    @pytch.when_green_flag_clicked
    def play(self):
        self.go_to_xy(-215, 0)

        while True:
            if pytch.key_pressed("w"):
                self.change_y(3)
            if pytch.key_pressed("s"):
                self.change_y(-3)

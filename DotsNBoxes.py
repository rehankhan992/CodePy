from tkinter import *
from tkinter import font
from tkinter import messagebox
import sys


class Player(object):
    def __init__(self, name, color="cyan"):
        self.score = 0
        self.str = StringVar()
        self.name = name
        self.color = color

    def update(self):
        self.str.set(self.name + ": %d" % self.score)


class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.GO_font = font.Font(self, name="GOFont", family="Times", weight="bold", size=36)
        self.canvas = Canvas(self, height=GAME_HEIGHT, width=GAME_WIDTH, bg="cyan")
        self.canvas.bind("<Button-1>", lambda e: self.click(e))  # binds to  button1 of mouse
        self.canvas.grid(row=1, column=0)
        self.dots = [[self.canvas.create_oval(CELLSIZE * i + OFFSET,
                                              CELLSIZE * j + OFFSET,
                                              CELLSIZE * i + OFFSET + 2 * CIRCLERAD,
                                              CELLSIZE * j + OFFSET + 2 * CIRCLERAD,
                                              fill="green")
                      for j in range(10)] for i in range(10)]
        self.lines = []
        self.infoframe = Frame(self)
        self.players = [Player("P1", "blue"), Player("P2", "red")]
        self.infoframe.players = [Label(self.infoframe, textvariable=i.str, bg="cyan", height=2, width=50) for i in
                                  self.players]
        for i in self.infoframe.players:
            i.grid()
        self.turn = self.players[0]
        self.update_players()
        self.infoframe.grid(row=0, column=0, sticky=N)
        self.grid()

    def update_players(self):
        for i in self.players:
            i.update()

    def click(self, event):
        x, y = event.x, event.y
        orient = self.is_close(x, y)
        if orient:
            if self.line_already_exists(x, y, orient):
                return
            l = self.create_line(x, y, orient)
            score = self.new_box_made(l)
            if score:
                self.turn.score += score
                self.turn.update()
                self.game_over_check()
            else:
                index = self.players.index(self.turn)
                self.turn = self.players[1 - index]
            self.lines.append(l)

    def create_line(self, x, y, orient):
        startx = CELLSIZE * ((x - OFFSET) // CELLSIZE) + DOTOFFSET
        starty = CELLSIZE * ((y - OFFSET) // CELLSIZE) + DOTOFFSET

        if orient == HORIZONTAL:
            endx = startx + CELLSIZE
            endy = starty
        else:
            endx = startx
            endy = starty + CELLSIZE
        return self.canvas.create_line(startx, starty, endx, endy, fill="red")

    def new_box_made(self, line):
        score = 0
        x0, y0, x1, y1 = self.canvas.coords(line)
        if x0 == x1:
            midx = x0
            midy = (y0 + y1) / 2
            pre = (x0 - CELLSIZE / 2, midy)
            post = (x0 + CELLSIZE / 2, midy)
        elif y0 == y1:
            midx = (x0 + x1) / 2
            midy = y0
            pre = (midx, y0 - CELLSIZE / 2)
            post = (midx, y0 + CELLSIZE / 2)

        if len(self.find_lines(pre)) == 3:
            self.fill_inside(pre)
            score += 1
        if len(self.find_lines(post)) == 3:
            self.fill_inside(post)
            score += 1
        return score

    def find_lines(self, coords):
        x, y = coords
        if x < 0 or x > GAME_WIDTH:
            return []
        if y < 0 or y > GAME_WIDTH:
            return []
        lines = [x for x in self.canvas.find_enclosed(x - CELLSIZE,
                                                      y - CELLSIZE,
                                                      x + CELLSIZE,
                                                      y + CELLSIZE)
                 if x in self.lines]
        return lines

    def fill_inside(self, coords):
        x, y = coords
        self.canvas.create_text(x, y, text=self.turn.name, fill=self.turn.color)

    def is_close(self, x, y):
        x -= OFFSET
        y -= OFFSET
        dx = x - (x // CELLSIZE) * CELLSIZE
        dy = y - (y // CELLSIZE) * CELLSIZE

        if abs(dx) < LOT:
            if abs(dy) < LOT:
                return None
            else:
                return VERTICAL
        elif abs(dy) < LOT:
            return HORIZONTAL
        else:
            return None

    def line_already_exists(self, x, y, orient):
        id_ = self.canvas.find_closest(x, y, halo=LOT)[0]
        if id_ in self.lines:
            return True
        else:
            return False

    def game_over_check(self):
        total = sum([x.score for x in self.players])
        if total == 81:
            if self.players[0].score > self.players[1].score:
                messagebox.showwarning(
                    title="GAME OVER",
                    message="Winner is Player1\n Player1 :%3d\n Player2: %3d\t" % (
                        self.players[0].score, self.players[1].score)
                )
            elif self.players[0].score == self.players[1].score:
                messagebox.showwarning(
                    title="GAME OVER",
                    message="Match is Draw\n Player1 :%3d\n Player2: %3d\t" % (
                        self.players[0].score, self.players[1].score)
                )

            else:
                messagebox.showwarning(
                    title="GAME OVER",
                    message="Winner is Player2\nPlayer1 :%3d\n Player2: %3d\t" % (
                        self.players[0].score, self.players[1].score)
                )
            sys.exit(0)

print("**** DOT AND BOX GAME ****     **** TKinter Package Required **** ")
LOT = 10
CELLSIZE = 40
OFFSET = 30
CIRCLERAD = 2
DOTOFFSET = OFFSET + CIRCLERAD
GAME_HEIGHT = 800
GAME_WIDTH = 800
mainw = Tk()
mainw.title('MB21ISDE279/Mohammad Rehan Khan')
mainw.f = MyFrame(mainw)
mainw.mainloop()

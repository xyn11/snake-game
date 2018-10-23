import curses
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        
    def draw(self, scr):
        for y in range(self.m):
            scr.addstr(y, 0, '+')
            scr.addstr(y, self.n, '+')
        for x in range(1, self.n):
            scr.addstr(0, x, '+')
            scr.addstr(self.m-1, x, '+')
        for y in range(1, self.m-1):
            for x in range(1, self.n):
                scr.addstr(y, x, '*')
        scr.refresh()

    def snakeposition(self, y, x):
        self.snakey = y
        self.snakex = x

    def drawsnake(self, scr):
        scr.addstr(self.snakey, self.snakex, '-')
        scr.refresh()

    def over(self):
        return self.over

    def move(self, dy, dx):
        if self.snakey + dy >= 0 and self.snakey + dy < self.m:
            self.snakey += dy
        if self.snakex + dx >= 0 and self.snakex + dx < self.n:
            self.snakex += dx


class Game:
        
    def startgame(self, scr):
        board = Board(6, 10)
        board.snakeposition(3, 3)
        board.draw(scr)
        board.drawsnake(scr)     

        while True:
            ch = scr.getch()
            if ch == curses.KEY_UP:
                board.move(-1, 0)
            if ch == curses.KEY_DOWN:
                board.move(1, 0)
            if ch == curses.KEY_LEFT:
                board.move(0, -1)
            if ch == curses.KEY_RIGHT:
                board.move(0, 1)
            if ch == ord('q'):
                break
            
            scr.clear()
            board.draw(scr)
            board.drawsnake(scr)
        


def main(scr):
    scr.clear()
    game = Game()
    game.startgame(scr)


if __name__ == '__main__':
    curses.wrapper(main)
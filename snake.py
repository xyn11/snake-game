import curses
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from random import randint

class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.score = 0
        self.l = []

    def snakeposition(self, y, x):
        self.snakey = y
        self.snakex = x

    def foodposition(self, y, x):
        self.foody = y
        self.foodx = x

    def uneaten(self):
        while self.snakey == self.foody and self.snakex == self.foodx:
            self.foody = randint(1, self.m - 1)
            self.foodx = randint(1, self.n - 1)

    def draw(self, scr):
        for y in range(self.m+1):
            scr.addstr(y, 0, '+')
            scr.addstr(y, self.n, '+')
        for x in range(1, self.n):
            scr.addstr(0, x, '+')
            scr.addstr(self.m, x, '+')
        scr.addstr(self.m+1, 1, 'score:'+str(self.score))

        if self.snakey == self.foody and self.snakex == self.foodx:
            self.score += 1
            self.l.append(self.tmp)
            self.uneaten()
        scr.addstr(self.foody, self.foodx, '?') 
        scr.addstr(self.snakey, self.snakex, '-')
        scr.move(self.m + 1, self.n + 1)
        scr.refresh()

    def over(self):
        return self.over

    def move(self, dy, dx):
        self.tmp = [self.snakey, self.snakex]
        if self.snakey + dy >= 0 and self.snakey + dy < self.m:
            self.snakey += dy
        if self.snakex + dx >= 0 and self.snakex + dx < self.n:
            self.snakex += dx


class Game:
        
    def startgame(self, scr):
        board = Board(6, 10)
        board.snakeposition(3, 3)
        board.foodposition(4,7)
        board.draw(scr)     
        score = 0

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
        


def main(scr):
    scr.clear()
    game = Game()
    game.startgame(scr)


if __name__ == '__main__':
    curses.wrapper(main)
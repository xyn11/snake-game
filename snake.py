import curses
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from random import randint
import time

class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.score = 0
        self.l = []

    def snakeposition(self, y, x):
        self.l = [[y, x]]

    def foodposition(self, y, x):
        self.foody = y
        self.foodx = x

    def snakehead(self):
        return self.l[-1]

    def oneaten(self):
        while [self.foody, self.foodx] in self.l:
            self.foody = randint(1, self.m - 1)
            self.foodx = randint(1, self.n - 1)

    def draw(self, scr):
        for y in range(self.m+1):
            scr.addstr(y, 0, '+')
            scr.addstr(y, self.n, '+')
        for x in range(1, self.n):
            scr.addstr(0, x, '+')
            scr.addstr(self.m, x, '+')
        scr.addstr(self.m+1, 5, 'score:'+str(self.score))

        scr.addstr(self.foody, self.foodx, '?') 
        scr.addstr(self.l[-1][0], self.l[-1][1], '*')
        for i in range(len(self.l) - 2, -1, -1):
            scr.addstr(self.l[i][0], self.l[i][1], 'o')
        scr.move(self.m + 1, self.n + 1)
        scr.refresh()

    def over(self):
        return self.over

    def move(self, dy, dx):
        yy, xx = self.snakehead()
        yy += dy
        xx += dx
        if [yy, xx] in self.l or yy < 1 or yy >= self.m or xx < 1 or xx >= self.n:
            return        
        if yy == self.foody and xx == self.foodx:
            self.score += 1
            self.l.append([yy, xx])
            self.oneaten()
        else:
            self.l = self.l[1:] + [[yy, xx]]

class Game:
        
    def startgame(self, scr):
        board = Board(8, 20)
        board.snakeposition(3, 3)
        board.foodposition(4,3)
        board.draw(scr)     
        direction = (-1, 0)
        while True:
            scr.timeout(150)
            ch = scr.getch()
            if ch == curses.KEY_UP:
                direction = (-1, 0)
            if ch == curses.KEY_DOWN:
                direction = (1, 0)
            if ch == curses.KEY_LEFT:
                direction = (0, -1)
            if ch == curses.KEY_RIGHT:
                direction = (0, 1)
            if ch == ord('q'):
                break
            board.move(direction[0], direction[1])
            scr.clear()
            board.draw(scr)
        


def main(scr):
    scr.clear()
    game = Game()
    game.startgame(scr)


if __name__ == '__main__':
    curses.wrapper(main)
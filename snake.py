import curses
from random import randint
import time

class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.score = 0
        self.l = []
        self.flag = False

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
        if self.over():
            scr.addstr(self.m+2, 5, 'Game Over')
        scr.addstr(self.foody, self.foodx, '?') 
        scr.addstr(self.l[-1][0], self.l[-1][1], '*')
        for i in range(len(self.l) - 2, -1, -1):
            scr.addstr(self.l[i][0], self.l[i][1], 'o')
        scr.move(self.m + 1, self.n + 1)
        scr.refresh()

    def over(self):
        if self.flag == True:
            return True        

    def move(self, dy, dx):
        yy, xx = self.snakehead()
        yy += dy
        xx += dx
        if [yy, xx] in self.l or yy < 1 or yy >= self.m or xx < 1 or xx >= self.n or [yy, xx] in self.l[:-1]:
            self.flag = True
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
        direction = (1, 0)
        while not board.over():
            scr.timeout(200)
            ch = scr.getch()
            if ch == curses.KEY_UP:
                if direction in {(-1, 0), (1,0)}:
                    continue
                direction = (-1, 0)
            if ch == curses.KEY_DOWN:
                if direction in {(-1, 0), (1,0)}:
                    continue
                direction = (1, 0)
            if ch == curses.KEY_LEFT:
                if direction in {(0, 1), (0,-1)}:
                    continue
                direction = (0, -1)
            if ch == curses.KEY_RIGHT:
                if direction in {(0, -1), (0,1)}:
                    continue
                direction = (0, 1)
            if ch == ord('q'):
                break
            board.move(direction[0], direction[1])
            scr.clear()
            board.draw(scr)
        while True:
            ch = scr.getch()
            if ch == ord('q'):
                return

def main(scr):
    scr.clear()
    game = Game()
    game.startgame(scr)

if __name__ == '__main__':
    curses.wrapper(main)
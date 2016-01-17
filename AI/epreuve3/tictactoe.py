#!/usr/bin/python
import random

"""
Essayez de faire mieux qu'un IA aléatoire!

Vous pouvez commencer avec size=3, comme un vrai tic-tac-toe,
mais idéalement une taille arbitraire devrait marcher.

Sinon, vous pouvez modifier la méthode isWon() pour qu'elle soit plus
efficace (pour une valeur de size arbitraire!).
"""

def main():

    b = Board(size=5)
    b.play(RandomIA(), RandomIA())


class RandomIA:
    def __init__(self):
        pass
    def play(self, board):
        return random.choice(board.emptyPositions)

class Board:
    def __init__(self, size = 3):
        self.t = [[" " for i in range(size)] for j in range(size)]
        self.size = size
        self.turn = "X"
        self.emptyPositions = [(i,j) for i in range(size) for j in range(size)]

    def draw(self):
        size = self.size
        s = "\n".join(["".join(self.t[i][j] for i in range(size)) for j in range(size)])
        print s


    def play(self,ia1,ia2):
        while 1:
            self.draw()
            if self.isWon():
                print "Et le vainqueur est:",self.winner,"!"
                break
            if len(self.emptyPositions) == 0:
                print "Partie nulle!"
                break
            if self.turn == "X":
                pos = ia1.play(self)
                self.turn = "O"
            else:
                pos = ia2.play(self)
                self.turn = "X"
            self.t[pos[0]][pos[1]] = self.turn
            print "--------------"
            self.emptyPositions.pop(self.emptyPositions.index(pos))
        self.draw()

    def isWon(self):
        deltas = [(0,1),(1,0),(1,1),(1,-1)]
        for i in range(self.size):
            for j in range(self.size):
                tp = self.t[i][j]
                if tp == " ":
                    continue
                for d in deltas:
                    pos = [i,j]
                    n = 1
                    for k in range(self.size-1):
                        pos[0] += d[0]
                        pos[1] += d[1]
                        if not (0<=pos[0]<self.size and 0<=pos[1]<self.size):
                            break
                        tk = self.t[pos[0]][pos[1]]
                        if tk == tp:
                            n+=1
                        else:
                            break
                    if n == self.size:
                        pos = [i,j]
                        for k in range(self.size):
                            self.t[pos[0]][pos[1]] = self.t[pos[0]][pos[1]].lower()
                            pos[0] += d[0]
                            pos[1] += d[1]
                        self.winner = tp
                        return True
        return False


main()

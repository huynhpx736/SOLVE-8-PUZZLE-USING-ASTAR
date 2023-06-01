# Nhóm 21
# Phan Xuân Huynh-N20DCCN023
# Phan Văn Lục-N20DCCN037
# Áp dụng thuật toán A* giải quyết bài toán 8 ô chữ

import copy
from colorama import Fore, Back, Style
from queue import PriorityQueue
class State:
    def __init__(self, data = None, par = None, g=0, h=0, op = None):
        self.data = data
        self.par = par
        self.g = g
        self.h = h
        self.op = op

    def clone(self):
        sn = copy.deepcopy(self)
        return sn

    def Print(self):
        print(Fore.BLACK+"g =",self.g , ",h =",self.h, ",f =",self.g+self.h)
        draw_board(self.data)

    def Key(self):
        if self.data == None:
            return None
        res = ''
        for i in self.data:
            res += (str)(i)
        return res
    def __lt__(self, other):
        if other == None:
            return False
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        if other == None:
            return False
        return self.Key() == other.Key()

class Operator:
    def __init__(self, i):
        self.i = i

    def checkStateNull(self, s):
        return s.data == None
    # s la State, x,y la vi tri trong state, i la lenh de doi vi tri tuong ung
    def swap(self, s, x, y, i):
        sn = s.clone()
        x_new = x
        y_new = y
        # xet up down
        if i == 0:
            x_new = x - 1
            y_new = y
        if i == 1:
            x_new = x + 1
            y_new = y
        # xet lefft, right
        if i == 2:
            x_new = x
            y_new = y - 1
        if i == 3:
            x_new = x
            y_new = y + 1
        sn.data[x * 3 + y] = s.data[x_new * 3 + y_new]  #thay đổi data cua ô trống với data của ô kia
        sn.data[x_new * 3 + y_new] = 0 #o trống di chuyển tới ô này nên không có data
        return sn

    def findPos(self, s):
        for i in range(3):
            for j in range(3):
                if s.data[i * 3 + j] == 0:
                    return i, j
        return None

    def Up(self, s): #s la state
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if x == 0:
            return None
        return self.swap(s, x, y, self.i)

    def Down(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if x == 2:
            return None
        return self.swap(s, x, y, self.i)

    def Left(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if y == 0:
            return None
        return self.swap(s, x, y, self.i)

    def Right(self, s):
        if self.checkStateNull(s):
            return None
        x, y = self.findPos(s)
        if y == 2:
            return None
        return self.swap(s, x, y, self.i)

    def Move(self, s):
        if self.i == 0:
            return self.Up(s)
        if self.i == 1:
            return self.Down(s)
        if self.i == 2:
            return self.Left(s)
        if self.i == 3:
            return self.Right(s)
        return None

def Equal(O, G):
    if O == None:
        return False
    return O == G

def Path(O):
    G=State(data= [1, 2, 3, 8, 0, 4, 7, 6, 5])
    if O.par != None:

        Path(O.par)
        if O.op.i == 0: print(Fore.RED+"Up")
        if O.op.i == 1: print(Fore.RED+"Down")
        if O.op.i == 2: print(Fore.RED+"Left")
        if O.op.i == 3: print(Fore.RED+"Right")
    O.Print()
    # A = O.par
    #
    # for x in range(4):
    #     if A!=None and A.op!=None and x != O.op.i:
    #        # A.Print()
    #         A.op.i = x
    #         op = Operator(x)
    #         child = op.Move(A)
    #         if child == None:
    #             continue
    #         if x == 0: print("If Up")
    #         if x == 1: print("If Down")
    #         if x == 2: print("If Left")
    #         if x == 3: print("If Right")
    #         #child.Print()
    #         child.g = A.g + 1
    #         child.h = Hx(child, G)
    #         child.Print()



def Hx(S, G):
    res = 0
    for i in range(9):
        if S.data[i ] != G.data[i]:
             res += 1
    if(S.data.index(0)==G.data.index(0)):
        return res
    else: return res-1

def taciAstar(S, G):
    Open = PriorityQueue()
    Closed = PriorityQueue()
    Open.put(S)
    S.g = 0
    S.h = Hx(S, G)
    Open.put(S)
    while True:
        if Open.empty() == True:
            print('Khong tim thay duong di')
            return
        O = Open.get()
        Closed.put(O)
        if Equal(O, G) == True:
            print("Tim thay duong di:")
            print()
            Path(O)
            return
        else: print("Xet trang thai tiep theo: ")
        print(Fore.RED+"Trang thai hien tai: ")
        O.Print()
        # tim tat ca cac trang thai con
        for i in range(4):
            op = Operator(i)
            child = op.Move(O)
            if child == None:
                continue
            if i == 0: print("Up")
            if i == 1: print("Down")
            if i == 2: print("Left")
            if i == 3: print("Right")
            child.g = O.g + 1
            child.h = Hx(child, G)
            child.Print()
            ok1 = child in Open.queue
            ok2 = child in Closed.queue
            if not ok1 and not ok2:
                child.par = O
                child.op = op
                child.g = O.g + 1
                child.h = Hx(child, G)
                Open.put(child)



def draw_board(board):
    for i in range(3):
        for j in range(3):
            if board[i*3+j] == 0:
                print(Fore.WHITE + Back.RED + ' x ' + Style.RESET_ALL, end=" ")
            else:
                print(Fore.BLACK + Back.LIGHTYELLOW_EX + f' {board[i*3+j]} ' + Style.RESET_ALL, end=' ')
        print()
    print()

def main():
    import time
    t1 = time.time()
    start = []
    goal = []
    with open("taci.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "start":
                for _ in range(3):
                    row = file.readline().strip().split()
                    start.extend([int(num) if num != "x" else 0 for num in row])
            elif line == "goal":
                for _ in range(3):
                    row = file.readline().strip().split()
                    goal.extend([int(num) if num != "x" else 0 for num in row])
    S = State(data=start)   #start=[2, 8, 3, 1, 6, 4, 7, 0, 5]
    G = State(data=goal)    #goal=[1, 2, 3, 8, 0, 4, 7, 6, 5]
    print("start")
    draw_board(start)
    print("goal")
    draw_board(goal)
    taciAstar(S,G)
    t2 = time.time()
    print('Thoi gian thuc hien: ', (t2 - t1))


if __name__ == '__main__':
    main()

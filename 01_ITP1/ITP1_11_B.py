class Dice:
    def __init__(self, a, b, c, d, e, f):
        # サイコロの現在一番上にある面
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

        self.n_list = [0, self.a, self.b, self.c, self.d, self.e, self.f]

    def is_right_surface(self, top, front):
        swapped = False
        if self.n_list.index(top) > self.n_list.index(front):
            tmp = front
            front = top
            top = tmp
            swapped = True

        if self.n_list.index(top) == 1 and self.n_list.index(front) == 2:
            return self.c, self.d, swapped
        if self.n_list.index(top) == 1 and self.n_list.index(front) == 3:
            return self.e, self.b, swapped
        if self.n_list.index(top) == 1 and self.n_list.index(front) == 4:
            return self.b, self.e, swapped
        if self.n_list.index(top) == 1 and self.n_list.index(front) == 5:
            return self.d, self.c, swapped
        if self.n_list.index(top) == 2 and self.n_list.index(front) == 3:
            return self.a, self.f, swapped
        if self.n_list.index(top) == 2 and self.n_list.index(front) == 4:
            return self.f, self.a, swapped
        if self.n_list.index(top) == 2 and self.n_list.index(front) == 6:
            return self.c, self.d, swapped
        if self.n_list.index(top) == 3 and self.n_list.index(front) == 5:
            return self.a, self.f, swapped
        if self.n_list.index(top) == 3 and self.n_list.index(front) == 6:
            return self.e, self.b, swapped
        if self.n_list.index(top) == 4 and self.n_list.index(front) == 5:
            return self.f, self.a, swapped
        if self.n_list.index(top) == 4 and self.n_list.index(front) == 6:
            return self.b, self.e, swapped
        if self.n_list.index(top) == 5 and self.n_list.index(front) == 6:
            return self.d, self.c, swapped

    def move(self, move_str):
        for i in move_str:
            if i == "N":
                self.move_N()
            elif i == "E":
                self.move_E()
            elif i == "W":
                self.move_W()
            elif i == "S":
                self.move_S()

    def move_N(self):
        tmp1 = self.a
        tmp2 = self.e
        self.a = self.b
        self.b = self.f
        self.e = tmp1
        self.f = tmp2

    def move_E(self):
        tmp1 = self.a
        tmp2 = self.c
        self.a = self.d
        self.c = tmp1
        self.d = self.f
        self.f = tmp2

    def move_W(self):
        tmp1 = self.a
        tmp2 = self.d
        self.a = self.c
        self.c = self.f
        self.d = tmp1
        self.f = tmp2

    def move_S(self):
        tmp1 = self.a
        tmp2 = self.b
        self.a = self.e
        self.b = tmp1
        self.e = self.f
        self.f = tmp2


a, b, c, d, e, f = map(int, input().split())
dice = Dice(a, b, c, d, e, f)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    right, left, is_swap = dice.is_right_surface(x, y)
    if is_swap:
        print(left)
    else:
        print(right)


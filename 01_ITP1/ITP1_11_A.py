class Dice:
    def __init__(self, a, b, c, d, e, f):
        # サイコロの現在一番上にある面
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

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
    """
    def debug(self):
        print("--------")
        print(f"{self.a=}")
        print(f"{self.b=}")
        print(f"{self.c=}")
        print(f"{self.d=}")
        print(f"{self.e=}")
        print(f"{self.f=}")
        print("--------")
    """


a, b, c, d, e, f = map(int, input().split())
dice = Dice(a, b, c, d, e, f)
li = list(input())
dice.move(li)
print(dice.a)

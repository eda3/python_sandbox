import itertools


class Dice:
    def __init__(self, a, b, c, d, e, f):
        # サイコロの現在一番上にある面
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

        # 他のダイスと一致したかどうか
        self.result = 0

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

    def check_one_around(self, dice):
        """チェックのために時計回りに一周させる"""
        for _ in range(4):
            """時計回りに回転"""
            tmp1 = self.b
            tmp2 = self.d
            self.b = self.c
            self.c = self.e
            self.d = tmp1
            self.e = tmp2

            # ダイスが一致しているかチェック
            self.check_dice_same(dice)

    def check_dice_same(self, dice):
        """引数指定したダイスと同一面かチェック"""
        if (
            self.a == dice.a and
            self.b == dice.b and
            self.c == dice.c and
            self.d == dice.d and
            self.e == dice.e and
            self.f == dice.f
        ):
            self.result += 1

    def all_check(self, dice):
        self.clear_result()

        self.check_one_around(dice)
        # b面をトップにする
        self.move("N")
        self.check_one_around(dice)

        # c面をトップにする
        self.move("W")
        self.check_one_around(dice)

        # e面をトップにする
        self.move("W")
        self.check_one_around(dice)

        # d面をトップにする
        self.move("W")
        self.check_one_around(dice)

        # f面をトップにする
        self.move("N")
        self.check_one_around(dice)

    def clear_result(self):
        self.result = 0

n = int(input())

li = []
for _ in range(n):
    a, b, c, d, e, f = map(int, input().split())
    dice = Dice(a, b, c, d, e, f)
    li.append(dice)

# 順列走査
flg = True
for v in itertools.combinations(li, 2):
    v[0].all_check(v[1])
    if v[0].result != 0:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")


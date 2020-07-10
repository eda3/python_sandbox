ranks = ["S", "H", "C", "D"]
cards = []
for rank in ranks:
    for i in range(1, 14, 1):
        cards.append([rank, str(i)])

n = int(input())
for i in range(n):
    x, y = map(str, input().split())

    for card in cards:
        if card[0] == x:
            if card[1] == y:
                cards.remove([x, y])

for card in cards:
    print(" ".join(card))

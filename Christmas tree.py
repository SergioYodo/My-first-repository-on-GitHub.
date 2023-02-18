class Shape:
    def __init__(self, color):
        self.color = color


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    # def draw(self):  # 11, 6, 6
    #     lst = [self.a, self.b, self.c]
    #     n = min(lst)  # 6
    #     for i in range(n):  # 1
    #         print('-' * (n - i - 1) + '*' * (2 * i + 1))  # "-" * 4 + "*" * 3

    def draw(self):
        lst = [self.a, self.b, self.c]
        n = min(lst)
        rows = [' ' * (n - i - 1) + '*' * (2 * i + 1) for i in range(n)]
        return '\n'.join(rows)


t = Triangle(11, 6, 6, "yellow")
# t.draw()
print(t.draw())

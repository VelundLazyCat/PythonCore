class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        self.color = color


first_animal = Animal('bob', 23)
second_animal = Animal('adam', 35)
first_animal.change_color("red")
second_animal.change_color("red")
print(first_animal.color)
print(second_animal.color)

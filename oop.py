class Animal:
    def __init__(self, my_name):
        self.name = my_name

    def say_hi(self):
        print(self.name + " says: " + self.sound)


class Cat(Animal):
    sound = 'meow'

    def __init__(self, my_name, color='black'):
        super().__init__(my_name)
        self.color = color


class Dog(Animal):
    sound = 'woof'


cat = Cat('Angie')
cat2 = Cat('Bruno', 'white')
dog = Dog('Gus')

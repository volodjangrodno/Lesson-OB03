class Dog():

    def speak(self):
        return 'Woof!'


class Cat():

    def speak(self):
        return 'Meow!'


def animal_sound(animal):
    animal.speak()


my_dog = Dog()
my_dog.speak()

my_cat = Cat()
my_cat.speak()

animal_sound(my_dog)
animal_sound(my_cat)
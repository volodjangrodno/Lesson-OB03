# Домашнее задание

# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        return 'Птицы издают звуки - Чик-чирик, Кря-кря, Курлык-курлык'

    def eat(self, food="пшено"):

        return f'Птички клюют {food}'


class Mammal(Animal):
    def make_sound(self):
        return 'Кошачьи издают звуки - Мур-Мяу'

    def eat(self, food="молоком"):

        return f'Млекопитающие питаются {food}'


class Reptile(Animal):
    def make_sound(self):
        return 'Рептилии издают звуки - Клац-клац, Пшшшшш-пссссссс'

    def eat(self, food="мясо"):

        return f'Рептилии едят {food}'

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()




class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def remove_animal(self, animal):
        self.animals.remove(animal)
        print(f"Животное {animal.name} удалено из зоопарка")



    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк")

    def remove_employee(self, employee):
        self.employees.remove(employee)
        print(f"Сотрудник {employee.name} удален из зоопарка")

    def save_animals_to_file(self, filename):
        with open(filename, "animals.txt") as file:
            for animal in self.animals:
                file.write(f"{animal.name}, {animal.age}, {animal.make_sound()}, {animal.eat()}\n")

    def save_employees_to_file(self, filename):
        with open(filename, "employees.txt") as file:
            for employee in self.employees:
                file.write(f"{employee.name}, {employee.position}\n")

    def load_animals_from_file(self, filename):
        with open(filename, "animals.txt") as file:
            for line in file:
                name, age, sound, eat = line.strip().split(',')
                if sound == 'Птицы издают звуки - Чик-чирик, Кря-кря, Курлык-курлык':
                    animal = Bird(name, age)
                elif sound == 'Кошачьи издают звуки - Мур-Мяу':
                    animal = Mammal(name, age)
                elif sound == 'Рептилии издают звуки - Клац-клац, Пшшшшш-пссссссс':
                    animal = Reptile(name, age)
                animal.make_sound = sound
                animal.eat = eat
                self.add_animal(animal)

    def load_employees_from_file(self, filename):
        with open(filename, "employees.txt") as file:
            for line in file:
                name, position = line.strip().split(',')
                employee = ZooKeeper(name, position)
                self.add_employee(employee)


class ZooKeeper(Zoo):
    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position
    def feed_animal(self, animal):
        print(f"{self.position} {self.name} покормил животное {animal.name}")


class Veterinarian(Zoo):
    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.position = position
    def heal_animal(self, animal):

        print(f"{self.position} {self.name} вылечил животное {animal.name}")

animals = [Reptile("Крокодил Гена", 25), Bird("Попугай Гоша", 2), Mammal("Пантера Багира", 5)]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())

bird2 = Bird("Утёнок Дональд", 2)
mammal2 = Mammal("Котофей Матроскин", 3)
reptile2 = Reptile("Удав Каа", 25)

zoo = Zoo()
keeper1 = ZooKeeper("Василий Пупкин", "Охранник")
veterinarian1 = Veterinarian("Айболит", "Ветеринар")

zoo.add_animal(bird2)
zoo.add_animal(mammal2)
zoo.add_animal(reptile2)

zoo.add_employee(keeper1)
zoo.add_employee(veterinarian1)

keeper1.feed_animal(bird2)
veterinarian1.heal_animal(mammal2)

animal_sound(zoo.animals)

zoo.save_animals_to_file('animals.txt')
zoo.save_employees_to_file('employees.txt')

zoo.load_animals_from_file('animals.txt')
zoo.load_employees_from_file('employees.txt')

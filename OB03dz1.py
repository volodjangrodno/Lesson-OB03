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
        return 'Рептилии издают звуки - Клац-клац'

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
        print(f"Сотрудник добавлен в зоопарк")

    def remove_employee(self, employee):
        self.employees.remove(employee)
        print(f"Сотрудник удален из зоопарка")


class ZooKeeper(Zoo):
    def feed_animal(self, animal):
        print(f"Животное {animal.name} покормлено сотрудником")


class Veterinarian(Zoo):
    def heal_animal(self, animal):

        print(f"Животное {animal.name} вылечено ветеринаром")

animals = [Reptile("Крокодил Гена", 25), Bird("Попугай Гоша", 2), Mammal("Пантера Багира", 5)]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())

bird2 = Bird("Утёнок Дональд", 2)
mammal2 = Mammal("Котофей Матроскин", 3)
reptile2 = Reptile("Удав Каа", 25)

zoo = Zoo()
keeper1 = ZooKeeper()
veterinarian1 = Veterinarian()

zoo.add_animal(bird2)
zoo.add_animal(mammal2)
zoo.add_animal(reptile2)

zoo.add_employee(keeper1)
zoo.add_employee(veterinarian1)

keeper1.feed_animal(bird2)
veterinarian1.heal_animal(mammal2)

animal_sound(zoo.animals)


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
        existing_animals = set()
        try:
            with open(filename, "r") as file:
                for line in file:
                    existing_animals.add(line.strip())
        except FileNotFoundError:
            pass  # Файл еще не существует, продолжаем без ошибки

        with open(filename, "a") as file:
            for animal in self.animals:
                animal_info = f"{animal.name}, {animal.age}, {animal.make_sound()}, {animal.eat()}\n"
                if animal_info.strip() not in existing_animals:
                    file.write(animal_info)


    def save_employees_to_file(self, filename):
        existing_employees = set()
        try:
            with open(filename, "r") as file:
                for line in file:
                    existing_employees.add(line.strip())
        except FileNotFoundError:
            pass  # Файл еще не существует, продолжаем без ошибки

        with open(filename, "a") as file:
            for employee in self.employees:
                employee_info = f"{employee.name}, {employee.position}\n"
                if employee_info.strip() not in existing_employees:
                    file.write(employee_info)

    def load_animals_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split(', ', maxsplit=3)  # Разделяем строку на 4 части
                    if len(parts) == 4:
                        name, age, sound, eat = parts

                        if 'Птицы издают звуки' in sound:
                            animal = Bird(name, age, sound, eat)
                        elif 'Кошачьи издают звуки' in sound:
                            animal = Mammal(name, age, sound, eat)
                        elif 'Рептилии издают звуки' in sound:
                            animal = Reptile(name, age, sound, eat)
                        else:
                            print(f"Неизвестный тип животного в строке: {line}")
                            continue

                        self.add_animal(animal)
                        print(f"Животное {name} выгружено из файла")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке данных из {filename}: {e}")

    def load_employees_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    try:
                        name, position = line.strip().split(', ')
                        employee = ZooKeeper(name, position)
                        self.add_employee(employee)
                        print(f"Сотрудник {name} выгружен из файла")
                    except ValueError:
                        print(f"Ошибка формата данных в строке: {line}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при загрузке данных из {filename}: {e}")

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

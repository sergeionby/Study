print('''Task #1
1. Напишите класс собака (Dog) (можно другое животное на выбор)
2. Определите параметры собаки (порода, кличка, возраст)
3. Создайте конструктор с определенными выше параметрами
4. Определите методы собаки:
• инфо (выводит полную информацию о конкретной собаке,
например, «Дворняга Шарик 5 лет»)
• голос (выводит сообщение, например «Шарик сказал гав»)
• бежит (выводит сообщение, например «Шарик бежит»)
• ест (выводит сообщение, например «Шарик ест колбасу», колбаса – параметр метода)
5. Создайте 2 экземпляра класса.
6. Вызовите методы класса для каждого экземпляра.
''')
class Cat:
    def __init__(self, breed, nickname, age):
        self.breed = breed
        self.nickname = nickname
        self.age = age

    def display_info(self):
        print(f'Животному с именем {self.nickname} (порода {self.breed}) уже {self.age} лет')

    def display_voice(self):
        print(f'{self.nickname} услышала мяукание')

    def run(self):
        print(f'{self.nickname} убегает')

    def eating(self):
        print(f'{self.nickname} ест сухой корм')

    def habits(self, time, do):
        print(f'{self.nickname} постоянно {do} {time}.')

    def __del__(self):
        print(f'По причине плохого поведения {self.nickname} нашел новый дом')

cat_1 = Cat('Cornish-rex', 'Филя', 4)
cat_1.display_info()
cat_1.display_voice()
cat_1.run()
cat_1.eating()
cat_1.habits('спит', 'днём')
print()

cat_2 = Cat('британская голубая кошка', 'Кузя', 6)
cat_2.display_info()
cat_2.display_voice()
cat_2.run()
cat_2.eating()
print()

del cat_2

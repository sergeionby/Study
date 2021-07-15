print('''Task 2
*наследование*
1. Создать классы Школьник Студент Работник.
Общие атрибуты (имя, возраст, пол) определить в родительском классе Человек.
*полиморфизм*
2. У всех должен быть метод Info() выводящий полную информацию, например:
• «Мальчик Женя (8 лет) учится в школе.»
• «Ольга (18 лет) учится в БГУ»-- у Студента есть дополнительный параметр «ВУЗ»
• «Анатолий (29 лет) работает в АСБ «Беларусбанк»-- у Работника есть доп. параметр 
«организация»
3. Создать несколько экземпляров классов, вывести информацию о них.
*инкапсуляция*
4. Запретить прямое изменение атрибута возраст, при вводе возраста делать проверку на допустимые 
значения и выводить предупреждение (школьник не меньше 5 лет и не больше 18) и т.д.
''')

class man:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.sex = sex
        
class schoolchild(man):
    def set_age(self, age):
        if age in range(6,18):
            self._age = age
        else: 
            print('Под возраст школьника не подходит')

    def info(self):
        sex_corr = self.sex.capitalize()
        name_corr = self.name.capitalize()
        print(f'{sex_corr} {name_corr} ({self._age} лет) учится в школе')

class student(man):
    def __init__(self, name, age, sex, university):
        man.__init__(self, name, age, sex)
        self.university = university

    def info(self):
        name_corr = self.name.capitalize()
        print(f'{name_corr} ({self._age} лет) учится в ', self.university)

    def set_age(self, age):
        if age in range(19, 50):
            self._age = age
        else:
             print('Под возраст студента не подподает')

class worker(man):
    def __init__(self, name, age, sex, org):
        man.__init__(self, name, age, sex)
        self.org = org
   
    def info(self):
        name_corr = self.name.capitalize()
        print(f'{name_corr} ({self._age} лет) работает в {self.org}')
    
    def set_age(self, age):
        if age in range(19, 150):
            self._age = age
        else:
             print('Под возраст работника не подподает')
    

person_1 = schoolchild('Женя', 4, 'мальчик')
person_1.info()
person_1.set_age(4)

person_2 = student('ольга', 18, 'девушка','БГУ')
person_2.info()
person_2.set_age(17)

person_3 = worker('анатолий', 29, 'мужчина', 'АСБ "Беларусбанк"')
person_3.info()
person_3.set_age(5)

person_4 = worker('виолета', 30, 'женщина', 'БГУИР')
person_4.info()
person_4.set_age(40)
person_4.info()
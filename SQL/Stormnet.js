// Домашнее задания по SQL при обучении на курсах компании "Stormnet"
// https://www.it-courses.by/courses/testirovanie-po/

// Задание 1 

// На сайте w3schools.com на страницу Learn SQL
// http://www.w3schools.com/sql/default.asp
// Нажать кнопку Try it yourself,  далее в новом окне нажать на кнопку  Run SQL
// Запросы для таблицы Customers:

// 1. Вывести всех, что живет в Лондоне
SELECT * FROM Customers 
WHERE City = 'London';

// 2. Выбрать имена контактов и имена заказчиков, где адрес заканчивается на 23
SELECT CustomerName, ContactName FROM Customers
WHERE Address like '%23';

// 3. Выбрать уникальные города.
SELECT DISTINCT City FROM Customers;

// 4. Выбрать тех пользователей, у кого почтовый код начинается с 0 (нуль)
SELECT ContactName FROM Customers
WHERE PostalCode like '0%';

//5. Вывести клиентов не из США
SELECT ContactName FROM Customers
WHERE Country != 'USA';

// 6.Вывести всех, кто из Франции и отсортировать по убыванию по имени контакта
SELECT ContactName FROM Customers
WHERE Country = 'France'
ORDER BY ContactName DESC;

// 7. Вывести клиентов из Германии и США, ограничить выбор 10 записями
SELECT ContactName FROM Customers
WHERE Country IN ('USA', 'Germany')
LIMIT 10;




// Задание 2 

// На сайте w3schools.com на страницу Learn SQL
// http://www.w3schools.com/sql/default.asp
// Нажать кнопку Try it yourself,  далее в новом окне нажать на кнопку  Run SQL
// Запросы для таблицы Products:

// 1. Выбрать все продукты, начинающиеся на букву «М»
SELECT ProductName FROM Products
WHERE ProductName like 'M%';

// 2. Вывести характеристику упаковки (unit) для товара Steeleye Stout
SELECT unit FROM Products
WHERE ProductName = 'Steeleye Stout';

// 3. Вывести названия товаров, цена которых выше 22
SELECT productname FROM Products
WHERE Price > 22;

// 4. Вывести товары, в которых вес упаковки составляет 250 g
SELECT ProductName FROM Products
WHERE Unit like '%250 g%';

// 5. Вывести товары, упаковка которых состоит из «bottles»
SELECT ProductName FROM Products
WHERE Unit like '%bottles%';

// 6. Вывести товары, где SupplierID составляет 7 и отсортировать результаты по убыванию по цене
SELECT ProductName FROM Products
WHERE SupplierID=7
order by price DESC;


// Задание 3
// На веб-странице существует кнопка «Быстрый поиск», которая выделяет 
// из таблицы character в базе данных всех персонажей выше 45 уровня 
// (столбец level), расы dwarf (столбец race) и выводит результат на 
// страницу. Укажите, как будет выглядеть в данном случае SQL-запрос.

SELECT level, race 
FROM character
WHERE level > 45  and race like  ‘dwarf’;


// Задание 4

// На сайте w3schools.com на страницу Learn SQL
// http://www.w3schools.com/sql/default.asp
// Нажать кнопку Try it yourself,  далее в новом окне нажать на кнопку  Run SQL
// Запросы для таблицы Employees:

// 1. Вывести имя, фамилию и записи о сотруднике
SELECT FirstName, LastName, Notes  FROM Employees;

// 2. Вывести информацию по работникам старше 1960 года
SELECT *  FROM Employees
WHERE BirthDate between '1%' and '1960%';

// 3. Вывести  дату рождения сотрудников, чьи имена начинаются на букву «А
SELECT LastName, FirstName, BirthDate  FROM Employees
WHERE FirstName like 'A%';

// 4. Вывести имя, фамилию и дату рождения сотрудников, отсортировав по дате рождения по возрастанию
SELECT FirstName, LastName, BirthDate  FROM Employees
ORDER BY BirthDate ASC;



// Задание 5* (используем http://sqlfiddle.com/)
// Зайти на главную страницу SQL fiddle и создать свою таблицу. 
// Использовать команды Create, Insert into, Update, Delete
// Столбцы
// Name, Surname, Age, Login, Password, E-mail
// Значения
// ('Nick', 'Brown', '32', 'LogNick', '12pass', 'nick@gmail.com'),
// ('Mike', 'Tobler', '26', 'SunF', '12qwerty', 'sunF@mail.ru'),
// ('Kate', 'Brown', '28', 'Katitty', '4test*12', 'KateBrown@mail.ru'),
// ('Nick', 'Bonner', '21', 'FlQSt', '12qweq', 'BonNick@yandex.ru'),
// ('Tom', 'Boyer', '40', 'preSTOM', '4test*12', 'preSTOM@tut.by'),
// ('Alex', 'Lord', '26', 'nutt7', '2floppynut', 'lord@gmail.com');

CREATE TABLE DB (
  Name varchar(255), 
  Surname varchar(255), 
  Age varchar(255), 
  Login varchar(255), 
  Password varchar(255), 
  Email varchar(255))
  ;
  INSERT INTO DB (Name, Surname, Age, Login, Password, Email)
  VALUES 
('Nick', 'Brown', '32', 'LogNick', '12pass', 'nick@gmail.com'),
('Mike', 'Tobler', '26', 'SunF', '12qwerty', 'sunF@mail.ru'),
('Kate', 'Brown', '28', 'Katitty', '4test*12', 'KateBrown@mail.ru'),
('Nick', 'Bonner', '21', 'FlQSt', '12qweq', 'BonNick@yandex.ru'),
('Tom', 'Boyer', '40', 'preSTOM', '4test*12', 'preSTOM@tut.by'),
('Alex', 'Lord', '26', 'nutt7', '2floppynut', 'lord@gmail.com');


// 1. Вывести имена и емейл людей старше 30 лет.
SELECT Name, Email FROM DB
WHERE age>30;

// 2. Вывести логин и пароль пользователей , фамилия которых начинается на «В»
SELECT Login, Password FROM DB
WHERE Surname like 'B%';

// 3. Вывести пароли, которые заканчиваются на “12”
SELECT Password FROM DB
WHERE Password like '%12';

// 4. Вывести все записи, где email содержит nick
SELECT * FROM DB
WHERE Email like '%nick%';

// 5. Вывести уникальный возраст
SELECT DISTINCT Age FROM DB;

// 6. Вывести поля имя, логин, пароль, e-mail и отсортировать по убыванию по Name
SELECT Name, Login, Password, Email FROM DB
ORDER BY Name DESC;

// 7. Вывести всю информацию о Nick Bonner
SELECT* FROM DB
WHERE Name='Nick' and Surname='Bonner';

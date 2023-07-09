![изображение](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/assets/122168309/40a0a6ea-27d0-4416-a58e-e3df55afca87)# Домашнее задание к занятию «Работа с данными (DDL/DML)»

### Боробов Иван Сергеевич

---

Задание можно выполнить как в любом IDE, так и в командной строке.

### Задание 1
1.1. Поднимите чистый инстанс MySQL версии 8.0+. Можно использовать локальный сервер или контейнер Docker.

1.2. Создайте учётную запись sys_temp. 

1.3. Выполните запрос на получение списка пользователей в базе данных. (скриншот)

1.4. Дайте все права для пользователя sys_temp. 

1.5. Выполните запрос на получение списка прав для пользователя sys_temp. (скриншот)

1.6. Переподключитесь к базе данных от имени sys_temp.

Для смены типа аутентификации с sha2 используйте запрос: 
```sql
ALTER USER 'sys_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
1.6. По ссылке https://downloads.mysql.com/docs/sakila-db.zip скачайте дамп базы данных.

1.7. Восстановите дамп в базу данных.

1.8. При работе в IDE сформируйте ER-диаграмму получившейся базы данных. При работе в командной строке используйте команду для получения всех таблиц базы данных. (скриншот)

*Результатом работы должны быть скриншоты обозначенных заданий, а также простыня со всеми запросами.*

### Ответ:
1. Установка mysql
```
sudo apt update
sudo apt upgrade
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo apt install ./mysql-apt-config_0.8.22-1_all.deb
sudo apt update
sudo apt install mysql-server
systemctl status mysql

 mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2023-07-09 02:35:25 EDT; 1min 16s ago
       Docs: man:mysqld(8)
             http://dev.mysql.com/doc/refman/en/using-systemd.html
   Main PID: 5423 (mysqld)
     Status: "Server is operational"
      Tasks: 37 (limit: 4643)
     Memory: 366.4M
        CPU: 1.263s
     CGroup: /system.slice/mysql.service
             └─5423 /usr/sbin/mysqld
```

2. Проверяю списоу существующих пользователей
```
mysql -u root -p
SELECT User, Host FROM mysql.user; - полчил список всех пользователей
CREATE USER 'sys_temp'@'localhost' IDENTIFIED BY 'netology2023'; - создал пользователя sys_temp с паролем netology2023;
CREATE USER 'sys_temp'@'192.168.31.141' IDENTIFIED BY 'netology2023'; - создал пользователя sys_temp с паролем netology2023, где 192.168.31.141 - адрес клиента откуда будет подключаться DBeaver, в случаес, если планируеи подключаться не с машины отличной от сервер;

SHOW GRANTS FOR 'sys_temp'@'localhost'; - проверю права доступа
img
GRANT ALL PRIVILEGES ON *.* TO 'sys_temp'@'localhost'; - выдал полные права
GRANT ALL PRIVILEGES ON *.* TO 'sys_temp'@'192.168.31.141'; - выдал полные права, где 192.168.31.141 - адрес клиента откуда будет подключаться DBeaver, в случаес, если планируеи подключаться не с машины отличной от сервер;

SHOW GRANTS FOR 'sys_temp'@'localhost'; - проверю права доступа;
img
mysql -u sys_temp -p - подключился к БД под sys_temp
mysql> ALTER USER 'sys_temp'@'localhost' IDENTIFIED WITH mysql_native_password BY 'netology2023'; - смены типа аутентификации с sha2
```

### Задание 2
Составьте таблицу, используя любой текстовый редактор или Excel, в которой должно быть два столбца: в первом должны быть названия таблиц восстановленной базы, во втором названия первичных ключей этих таблиц. Пример: (скриншот/текст)
```
Название таблицы | Название первичного ключа
customer         | customer_id
```
### Ответ
```
Название таблицы      |  Название первичного ключа
actor                 |  actor_id
actor_info            | 
address               |  address_id
category              |  category_id
city                  |  city_id
country               |  country_id
customer              |  customer_id
customer_list         |
film                  |  film_id
film_actor            |
film_category         |
film_list             |
film_text             |
inventory             |  inventory_id
language              |  language_id
nicer_but_slower_film_list|
payment               |  payment_id
rental                |  rental_id
sales_by_film_category|
sales_by_store        |
staff                 |  staff_id
staff_list            |
store                 |  store_id


```



## Дополнительные задания (со звёздочкой*)
Эти задания дополнительные, то есть не обязательные к выполнению, и никак не повлияют на получение вами зачёта по этому домашнему заданию. Вы можете их выполнить, если хотите глубже шире разобраться в материале.

### Задание 3*
3.1. Уберите у пользователя sys_temp права на внесение, изменение и удаление данных из базы sakila.

3.2. Выполните запрос на получение списка прав для пользователя sys_temp. (скриншот)

*Результатом работы должны быть скриншоты обозначенных заданий, а также простыня со всеми запросами.*

### Ответ

```
mysql> GRANT ALL PRIVILEGES ON sakila.* TO 'sys_temp'@'192.168.31.141'; - выдал полные права на базу sakila
Query OK, 0 rows affected (0.01 sec)

mysql> REVOKE INSERT, DELETE, UPDATE, DROP ON sakila.* FROM sys_temp@192.168.31.141; - убрал права на базу sakila
Query OK, 0 rows affected (0.02 sec)

INSERT - вставлять данные в таблицу;
DELETE - удалять данные из таблицы;
UPDATE - обновлять данные в таблице;
DROP - удалять таблицы;
```

mysql> SHOW GRANTS FOR 'sys_temp'@'192.168.31.141';




# Домашнее задание к занятию  «Очереди RabbitMQ»

### Боробов Иван

[consumer.py](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/bf1975c9dfe476f076b975b74a677c5e549b45f2/CONF-11-04/consumer.py)
[producer.py](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/bf1975c9dfe476f076b975b74a677c5e549b45f2/CONF-11-04/producer.py)

---

### Задание 1. Установка RabbitMQ

Используя Vagrant или VirtualBox, создайте виртуальную машину и установите RabbitMQ.
Добавьте management plug-in и зайдите в веб-интерфейс.

*Итогом выполнения домашнего задания будет приложенный скриншот веб-интерфейса RabbitMQ.*

### Ответ:

![web babbitMQ](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-01.png)

---

### Задание 2. Отправка и получение сообщений

Используя приложенные скрипты, проведите тестовую отправку и получение сообщения.
Для отправки сообщений необходимо запустить скрипт producer.py.

Для работы скриптов вам необходимо установить Python версии 3 и библиотеку Pika.
Также в скриптах нужно указать IP-адрес машины, на которой запущен RabbitMQ, заменив localhost на нужный IP.

```shell script
$ pip install pika
```

Зайдите в веб-интерфейс, найдите очередь под названием hello и сделайте скриншот.
После чего запустите второй скрипт consumer.py и сделайте скриншот результата выполнения скрипта

*В качестве решения домашнего задания приложите оба скриншота, сделанных на этапе выполнения.*

Для закрепления материала можете попробовать модифицировать скрипты, чтобы поменять название очереди и отправляемое сообщение.

### Ответ:

![web_queue](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-02.png)
![cmd_consumer.py](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-03.png)

---

### Задание 3. Подготовка HA кластера

Используя Vagrant или VirtualBox, создайте вторую виртуальную машину и установите RabbitMQ.
Добавьте в файл hosts название и IP-адрес каждой машины, чтобы машины могли видеть друг друга по имени.

Пример содержимого hosts файла:
```shell script
$ cat /etc/hosts
192.168.0.10 rmq01
192.168.0.11 rmq02
```
После этого ваши машины могут пинговаться по имени.

Затем объедините две машины в кластер и создайте политику ha-all на все очереди.

*В качестве решения домашнего задания приложите скриншоты из веб-интерфейса с информацией о доступных нодах в кластере и включённой политикой.*

Также приложите вывод команды с двух нод:

```shell script
$ rabbitmqctl cluster_status
```

Для закрепления материала снова запустите скрипт producer.py и приложите скриншот выполнения команды на каждой из нод:

```shell script
$ rabbitmqadmin get queue='hello'
```

После чего попробуйте отключить одну из нод, желательно ту, к которой подключались из скрипта, затем поправьте параметры подключения в скрипте consumer.py на вторую ноду и запустите его.

*Приложите скриншот результата работы второго скрипта.*

### Ответ:

rabbitmqctl cluster_status  

![](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-04.png)

![](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-05.png)

rabbitmqadmin get queue='hello'  

![](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-06.png)

![](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/27c8f34befa42a7bd5810d13bcb81532ae0f40e3/IMG-11-04/11-04-07.png)

Проверка действующих политик  
rabbitmqctl list_policies  

![](https://github.com/Borobov/05-Data-storage-and-transmission-systems-/blob/34dd8c483108fdf67d46c42f2fbb3d21e9a405d8/IMG-11-04/11-04-08.png)

---



#!/usr/bin/env python
# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello_2023')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology 2023!')
connection.close()

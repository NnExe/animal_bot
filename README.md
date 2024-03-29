# Animal Bot
- [Введение](#введение)
- [Функционал проекта](#функционал-проекта)
- [Используемые технологии](#используемые-технологии)
- [Переменные окружения](#переменные-окружения)
- [Запуск приложения](#запуск-приложения)

## Введение
Проект animal_bot представляет из себя телеграм-бот для отправки изображений в ответ на введенную команду.

## Функционал проекта:
Пользователю доступны три команды: ```/start```, ```/newcat```, ```/newdog```. Команда ```/start``` запускает бот и отправляет приветствие пользователю с обращением по имени. Далее в ответ на запрос ```/newcat```или ```/newdog``` бот присылает случайное изображение соответствующего животного. Изображения берутся из апи, заданных переменными из раздела "Переменные окружения". В логах приложения уровня INFO выводится url изображения и имя пользователя, которому оно было отправлено.

## Используемые технологии
При создании и разворачивании приложения использовались следующие технологии:
- ```python 3.7```
- ```python-telegram-bot 13.12```
- ```requests 2.28.0```
- ```docker```

## Переменные окружения
В директории infra репозитория находится файл ```all.env```, содержащий следующие переменные окружения:\
```TOKEN``` - секретный токен для телеграмм-канала\
```CAT_URL``` - адрес апи для поиска ссылок на котиков, по умолчанию https://api.thecatapi.com/v1/images/search
```DOG_URL``` - адрес апи для поиска ссылок на собак, по умолчанию https://api.thedogapi.com/v1/images/search

## Запуск приложения
Для запуска приложения перейдите в директорию infra и введите 
```
docker-compose up
```

Инструкция по запуску телеграм-бота через Docker

1. pip freeze >> requirements.txt - создание файла, где хранятся все библиотеки использующиеся в программе ТГ-бота
2. sudo docker build . - создание докер-контейнера
3. sudo docker images - просмотр созданных докер-образов, необходимо скопировать IMAGE ID
4. sudo docker run -d -p 81:80 IMAGE ID - запуск докер-контейнера

Инструкция не завершена

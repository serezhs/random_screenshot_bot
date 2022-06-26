Запуск:

1. скопировать файлы
2. создать файл .env
3. в файле .env создать переменную TOKEN и сохранить в ней токен телеграм бота
4. создать образ из докерфайла
    docker build -t scr_bot .
5. создать и запустить контейнер
    docker run -d --name scr_bot scr_bot

для остановки контейнера можно использовать команду
    docker container stop scr_bot
чтобы запустить остановленный контейнер снова используйте команду
    docker container start scr_bot

для удаления контейнера используйте команду
    docker container rm scr_bot
а для удаления образа
    docker image rm scr_bot
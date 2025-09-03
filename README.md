# Проект_почтовой_рассылки_для_пользователей_Андрианов_М_С
Веб-приложение, позволяющее пользователям управлять списками рассылки для клиентов.


### Проект создан на основе фреймворка Django. Для запуска потребуется:
    - Склонировать архив
    ```
    git clone https://github.com/MaksoN12340987/Project_of_mailing_for_users_Andrianov_M_S.git Coursework_23
    ```
    - Перейти в папку с проектом
    ```
    cd ./Project_of_mailing_for_users_Andrianov_M_S/
    ```
    - Рекомендую распаковать изображения на беграунд, так восприятие
    проекта будет лучше
    ```
    unzip ./static/images/images.zip
    ``` *или через любую программу архиватор
    - Подготовить базу данных
    ```
    python manage.py migrate
    ```
    - Згрузить модели в базу данных
    ```
    python manage.py create_units

    python manage.py loaddata mailings/fixture/Newsletter.json --format json

    python manage.py loaddata mailings/fixture/AttemptSend.json --format json
    ```

    Все фикстуры заархивированны, если что-то не получается загрузить, сделайте:
    ```
    python manage.py mailing_clean
    python manage.py migrate auth zero
    ``` + очистите БД и попробуйте снова (можно загрузить последовательно 4ре фикстуры соблюдая завсимости)


----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
# Project_of_mailing_for_users_Andrianov_M_S
A Django web application that allows users to manage mailing lists for clients.

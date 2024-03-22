# HRspace-Backend
## Описание:
HRSpace - маркетплейс частных рекрутеров и кадровых агентств по подбору
сотрудника под ключ.

Проект состоит из бэкенд-приложения на Django и фронтенд-приложения на React.

[Схема базы данных](https://dbdiagram.io/d/HRspase-65ef0862b1f3d4062ca0f7fc) 

## Возможности проета:

## Запуск:

#### Создание БД и загрузка данных:

```bash
sudo docker compose exec -T backend python manage.py makemigrations users
sudo docker compose exec -T backend python manage.py makemigrations bids
sudo docker compose exec -T backend python manage.py migrate
sudo docker compose exec -T backend python manage.py collectstatic --no-input
sudo docker compose exec -T backend python manage.py load_ingredientsload_city
sudo docker compose exec -T backend python manage.py load_country
sudo docker compose exec -T backend python manage.py load_job_vacancy
sudo docker compose exec -T backend python manage.py load_sphere
```

## Технологии: 
[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,nginx,)](https://skillicons.dev)

## Cсылки на проект:

## Авторы:  

[Анастасия Богданова](https://github.com/Anastasia289/)   
[Елена Василькова](https://github.com/ElenaVasilkova)   
[Елена Юнникова](https://github.com/Edelveisx)

# HRspace-Backend
## Описание:
HRSpace - маркетплейс частных рекрутеров и кадровых агентств по подбору
сотрудника под ключ.

Проект состоит из бэкенд-приложения на Django и фронтенд-приложения на React.

[С проектом можно ознакомиться здесь ](https://hrspace.hopto.org/)   
[Схема базы данных](https://dbdiagram.io/d/HRspase-65ef0862b1f3d4062ca0f7fc)   
[Документация](https://disk.yandex.ru/d/wlfwzfvgij-AYA) 
## Возможности проета:


## Что сделано:

1. Созданы справочники и заполнены данными:

JobVacancy 
Sphere 
City 
ScheduleOption 
WorkFormat 
RegisterAsOption 
Country 
EmployeeCategory 
ExperienceOption 
EducationsOption
EmployeeSkill +
EmployeeAddSkill(данных нет)
TariffOption +
RecruiterTask +

2. Заявка Bid

3 Пользователи

Василий Пупкин
vasya
zxc102938


Джо Блэк
joe
mko091122

admin
111111

3.

## Запуск:

#### Загрузка словарей в базу данных:

```bash
docker exec docker_wrapper-django-1 python manage.py load_dict
```
# Запуск докер контейнеров для разработки проекта

Необходимо склонировать инфраструктуру для запуска контейнеров:

```
git clone git@github.com:Space-HR/docker_wrapper.git
```
или
```
git clone https://github.com/Space-HR/docker_wrapper.git
```

## 1. В папку 'docker_wrapper' склонировать backend

```
git clone git@github.com:Space-HR/hr-space-backend.git -b development_backend hr-space-backend 
```
или
```
git clone https://github.com/Space-HR/hr-space-backend.git -b develop hr-space-frontend
```

## 2. В папку 'docker_wrapper' склонировать frontend

```
git clone git@github.com:Space-HR/hr-space-frontend.git -b develop hr-space-frontend
```
или
```
git clone https://github.com/Space-HR/hr-space-frontend.git -b development_backend hr-space-backend 
```

## 3.  Скопируйте все из файла .env.example в файл .env и актуализируйте данные по необходимости

## 4. В папку 'docker_wrapper' запустить docker-compose.yml:

```
docker-compose up -d
```

## 5. Остановить:

```
docker-compose down
```

## 6. Пересобрать

```
docker-compose build --no-cache --pull
```


## Технологии: 
[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,nginx,)](https://skillicons.dev)

## Cсылки на проект:

## Авторы:  

[Анастасия Богданова](https://github.com/Anastasia289/)   
[Елена Василькова](https://github.com/ElenaVasilkova)   
[Елена Юнникова](https://github.com/Edelveisx)

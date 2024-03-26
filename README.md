# HRspace-Backend
## Описание:
HRSpace - маркетплейс частных рекрутеров и кадровых агентств по подбору
сотрудника под ключ.

Проект состоит из бэкенд-приложения на Django и фронтенд-приложения на React.

[С проектом можно ознакомиться здесь ](https://hrspace.hopto.org/)   
[Схема базы данных](https://dbdiagram.io/d/HRspase-65ef0862b1f3d4062ca0f7fc)   
[Документация](https://disk.yandex.ru/d/wlfwzfvgij-AYA) 
## Возможности проета:
Построена модель базы данных исходя из которой можно 
реализовать движение заявки с помощью смены статусов.

Статусы заявки:

    draft [note: в момент создания]

    moderation [note: после того как пользователь нажимает 'сохранить']

    published [note: после прихода ответа от платежного сервиса об оплате]

    at_work [note: после того как получен первый 'accepted' на заявку]

    closed [note: наброно нужное количество 'accepted' по резюме]

    canceled [note: по каким-то причинам работодатель решил удалить заявку]


Статусы сущности связывающей заявку и рекрутера
  
    invite [note: 'Приглашение от работодателя рекрутеру. Этот статус выставляет работодатель'] 
  
    response [note: 'Отклик к работодателю от рекрутера. Этот статус выставляет рекрутер'] 
  
    accepted [note: '1 работодатель принял response. или 2 Рекрутер принял invite'] 
    
    refused [note: '1 Работодатель отклонил response. или 2 Рекрутер отклонил invite'] 


Статусы сущности с резюме

    new [note: 'Отправлено на рассмотрение работаодателю'] 

    to_interview [note: 'Работодатель назначил интервью'] 

    accepted [note: 'Работодатель принял кандидатуру']

    canceled [note: 'Работодатель отклонил кандидатуру'] 
}

Всем рекрутерам должны показываться заявки у которых статус 'published' или 'at_work',
но по сущности связей заявки и рекрутера количество accepted, меньше, чем запрашивал работодатель рекрутеров

## Что сделано:

### Созданы справочники и заполнены данными:

1. **Должность**

* `api/v1/jobvacancy/` (**GET**): получить список всех должностей

**Пример запроса**

```
GET api/v1/jobvacancy/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Менеджер",
    }
]
``` 

* `api/v1/jobvacancy/{id}/` (**GET**): получить должность по id.

**Пример запроса**
``` 
GET api/jobvacancy/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Менеджер",
}
``` 
 
2. **Сфера деятельности**

* `api/v1/sphere/` (**GET**): получить список всех сфер деятельности

**Пример запроса**

```
GET api/v1/sphere/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Маркетинг",
    }
]
``` 

* `api/v1/sphere/{id}/` (**GET**): получить сферу деятельности по id.

**Пример запроса**
``` 
GET api/sphere/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Маркетинг",
}
``` 

3. **Города**

* `api/v1/city/` (**GET**): получить список всех городов

**Пример запроса**

```
GET api/v1/city/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Москва",
    }
]
``` 

* `api/v1/city/{id}/` (**GET**): получить город по id.

**Пример запроса**
``` 
GET api/city/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Москва",
}
``` 

4. **График работы**

* `api/v1/scheduleoption/` (**GET**): получить список всех видов графика работы

**Пример запроса**

```
GET api/v1/scheduleoption/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Сменный",
    }
]
``` 

* `api/v1/scheduleoption/{id}/` (**GET**): получить вид графика работы по id.

**Пример запроса**
``` 
GET api/scheduleoption/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Сменный",
}
``` 

5. **Форматы работы**

* `api/v1/workformat/` (**GET**): получить список всех видов формата работы

**Пример запроса**

```
GET api/v1/workformat/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "В офисе",
    }
]
``` 

* `api/v1/workformat/{id}/` (**GET**): получить вид формата работы по id.

**Пример запроса**
``` 
GET api/workformat/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "В офисе",
}
``` 
 
6. **Способы трудоустройства**

* `api/v1/registerasoption/` (**GET**): получить список всех способы трудоустройства

**Пример запроса**

```
GET api/v1/registerasoption/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "В офисе",
    }
]
``` 

* `api/v1/registerasoption/{id}/` (**GET**): получить способ трудоустройства по id.

**Пример запроса**
``` 
GET api/registerasoption/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "В офисе",
}
```
 
7. **Страны**

* `api/v1/country/` (**GET**): получить список всех стран

**Пример запроса**

```
GET api/v1/country/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Беларусь",
    }
]
``` 

* `api/v1/country/{id}/` (**GET**): получить страну по id.

**Пример запроса**
``` 
GET api/country/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Беларусь",
}
```
 
8. **Категории соискателя (дополнительные)**

* `api/v1/employeecategory/` (**GET**): получить список всех категорий соискателя

**Пример запроса**

```
GET api/v1/employeecategory/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Пенсионеры",
    }
]
``` 

* `api/v1/employeecategory/{id}/` (**GET**): получить категорию соискателя по id.

**Пример запроса**
``` 
GET api/employeecategory/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Пенсионеры",
}
```

9. **Опыт работы**

* `api/v1/experienceoption/` (**GET**): получить список всех диапозонов опыта работы

**Пример запроса**

```
GET api/v1/experienceoption/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Без опыта",
    }
]
``` 

* `api/v1/experienceoption/{id}/` (**GET**): получить диапозон опыта работы по id.

**Пример запроса**
``` 
GET api/experienceoption/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Без опыта",
}
```

10. **Образование**

* `api/v1/educationsoption/` (**GET**): получить список всех видов образования

**Пример запроса**

```
GET api/v1/educationsoption/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Высшее",
    }
]
``` 

* `api/v1/educationsoption/{id}/` (**GET**): получить вид образования по id.

**Пример запроса**
``` 
GET api/educationsoption/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Высшее",
}
```


11. **Навыки**

* `api/v1/employeeskill/` (**GET**): получить список всех навыков

**Пример запроса**

```
GET api/v1/employeeskill/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Python",
    }
]
``` 

* `api/v1/employeeskill/{id}/` (**GET**): получить навык по id.

**Пример запроса**
``` 
GET api/employeeskill/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Python",
}
```

EmployeeAddSkill(данных нет, еще не реализовано добавление)
12. **Навыки (индивидуальный справочник, куда можно добавить)**

* `api/v1/employeeaddskill/` (**GET**): получить список всех добавленных навыков

**Пример запроса**

```
GET api/v1/employeeaddskill/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Выращивать пингвинов",
    }
]

``` 

* `api/v1/employeeaddskill/{id}/` (**GET**): получить навык по id.

**Пример запроса**
``` 
GET api/employeeaddskill/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Выращивать пингвинов",
}
```
 
13. **Тарифы**

* `api/v1/tariffoption/` (**GET**): получить список всех тарифов

**Пример запроса**

```
GET api/v1/tariffoption/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 1,
        "name": "100% за выход сотрудника",
        "payment_for_employee_start_working": 100,
        "payment_for_employee_after_guarantee": 0,
        "guarantee_period": 0,
        "description": "Отличный вариант, чтобы на заявку откликнулись «звездные» рекрутеры с опытом."
        "units_of_measurement_warranty_period": "day"
    }
]

``` 

* `api/v1/tariffoption/{id}/` (**GET**): получить тариф по id.

**Пример запроса**
``` 
GET api/tariffoption/{id}/
Права доступа: Доступно без токена.
Response:
{
        "id": 1,
        "name": "100% за выход сотрудника",
        "payment_for_employee_start_working": 100,
        "payment_for_employee_after_guarantee": 0,
        "guarantee_period": 0,
        "description": "Отличный вариант, чтобы на заявку откликнулись «звездные» рекрутеры с опытом."
        "units_of_measurement_warranty_period": "day"
}
```

14**Задачи рекрутера**

* `api/v1/recruitertask/` (**GET**): получить список задач рекрутера

**Пример запроса**

```
GET api/v1/recruitertask/
Права доступа: Доступно без токена
Response:
[
    {
        "id": 0,
        "name": "Python",
    }
]
``` 

* `api/v1/recruitertask/{id}/` (**GET**): получить задачу рекрутера по id.

**Пример запроса**
``` 
GET api/recruitertask/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 0,
    "name": "Python",
}
```

### Завка создается, редактируется (нет пока смены статусов)
**Заявка**

* `api/v1/bid/` (**POST, GET**): получить список всех рецептов или создать новый.

**Пример запроса**
```
GET api/recipes/
Права доступа: Доступно c токеном
Response:
[
    {
        "id": 0,
        "employer": {
            "id": 0,
            "user": 0,
            "company": "string",
            "position": "string"
        },
        "title": "string",
        "job_vacancy": "string",
        "sphere": "string",
        "min_salary": 2147483647,
        "max_salary": 2147483647,
        "schedule": "string",
        "schedule_comment": "string",
        "work_formats": [
            "string"
        ],
        "register_as_set": [
            "string"
        ],
        "city": "string",
        "vhl": true,
        "working_conditions": "string",
        "employee_categories": [
            "string"
        ],
        "foreign_citizen": true,
        "foreign_countries": [
            "string"
        ],
        "employee_experience": "string",
        "employee_education": "string",
        "employee_skills": [
            "string"
        ],
        "employee_add_skills": [
            "string"
        ],
        "responsibilities_employee": "string",
        "qty_employees": 1,
        "payment_for_employee": 2147483647,
        "tariff": "string",
        "qty_recruiters": 32767,
        "employee_will_go_to_work_at": "2019-08-24",
        "expected_first_cv_date": "2019-08-24",
        "recruiter_tasks": [
            "string"
        ],
        "resume_after_interview": true,
        "not_private_person": true,
        "skills_recruiter": "string",
        "stop_list": "string",
        "created_at": "2019-08-24T14:15:22Z",
        "closed_at": "2019-08-24",
        "status": "draft",
        "recruiters": [
            {
                "id": 0,
                "recruiter": {
                    "id": 0,
                    "user": 0,
                    "top10": true,
                    "finished_cases": 2147483647,
                    "years_of_exp": 2147483647,
                    "about_me": "string"
                },
                "bid": "string",
                "status": "invite",
                "candidates": [
                    {
                        "id": 0,
                        "recruiter_to_bid": 0,
                        "file": "http://example.com",
                        "comment": "string",
                        "accepted_at": "2019-08-24T14:15:22Z",
                        "status": "new"
                    }
                ]
            }
        ]
    }
]
 
POST api/recipes/
Права доступа: Авторизованный пользователь
Request:
{
    "employer": 1,
    "title": "Нужен работник",
    "job_vacancy": 1,
    "sphere": 1,
    "min_salary": null,
    "max_salary": null,
    "schedule": null,
    "schedule_comment": "",
    "work_formats": [],
    "register_as_set": [],
    "city": null,
    "vhl": false,
    "working_conditions": "",
    "employee_categories": [],
    "foreign_citizen": false,
    "foreign_countries": [],
    "employee_experience": null,
    "employee_education": null,
    "employee_skills": [],
    "employee_add_skills": [
        {"name": "Linux"},
        {"name": "Android"}
    ],
    "responsibilities_employee": "",
    "qty_employees": 1,
    "payment_for_employee": 0,
    "tariff": 1,
    "qty_recruiters": 1,
    "employee_will_go_to_work_at": null,
    "expected_first_cv_date": null,
    "recruiter_tasks": [],
    "resume_after_interview": false,
    "not_private_person": true,
    "skills_recruiter": "",
    "stop_list": "",
    "created_at": "2024-03-25T22:47:45.783872+03:00",
    "closed_at": null,
    "status": "draft"
}

Response:
{
        "employer": 1,
        "title": "Нужен работник",
        "job_vacancy": 1,
        "sphere": 1,
        "min_salary": null,
        "max_salary": null,
        "schedule": null,
        "schedule_comment": "",
        "work_formats": [],
        "register_as_set": [],
        "city": null,
        "vhl": false,
        "working_conditions": "",
        "employee_categories": [],
        "foreign_citizen": false,
        "foreign_countries": [],
        "employee_experience": null,
        "employee_education": null,
        "employee_skills": [],
        "employee_add_skills": [
            {"name": "Linux"},
            {"name": "Android"}
        ],
        "responsibilities_employee": "",
        "qty_employees": 1,
        "payment_for_employee": 0,
        "tariff": 1,
        "qty_recruiters": 1,
        "employee_will_go_to_work_at": null,
        "expected_first_cv_date": null,
        "recruiter_tasks": [],
        "resume_after_interview": false,
        "not_private_person": true,
        "skills_recruiter": "",
        "stop_list": "",
        "created_at": "2024-03-25T22:47:45.783872+03:00",
        "closed_at": null,
        "status": "draft"
}
``` 


* `api/recipes/{id}/` (**GET, PATCH**): получить рецепт или частично изменить или удалить рецепт.

**Пример запроса**
``` 
GET api/recipes/{id}/
Права доступа: Доступно без токена.
Response:
{
    "employer": 1,
    "title": "Нужен работник",
    "job_vacancy": 1,
    "sphere": 1,
    "min_salary": null,
    "max_salary": null,
    "schedule": null,
    "schedule_comment": "",
    "work_formats": [],
    "register_as_set": [],
    "city": null,
    "vhl": false,
    "working_conditions": "",
    "employee_categories": [],
    "foreign_citizen": false,
    "foreign_countries": [],
    "employee_experience": null,
    "employee_education": null,
    "employee_skills": [],
    "employee_add_skills": [
        {"name": "Linux"},
        {"name": "Android"}
    ],
    "responsibilities_employee": "",
    "qty_employees": 1,
    "payment_for_employee": 0,
    "tariff": 1,
    "qty_recruiters": 1,
    "employee_will_go_to_work_at": null,
    "expected_first_cv_date": null,
    "recruiter_tasks": [],
    "resume_after_interview": false,
    "not_private_person": true,
    "skills_recruiter": "",
    "stop_list": "",
    "created_at": "2024-03-25T22:47:45.783872+03:00",
    "closed_at": null,
    "status": "draft"
}

PATCH api/recipes/{id}/
Права доступа: Автор рецепта.
Request:
{
        "employer": 1,
        "title": "Нужен работник",
        "job_vacancy": 1,
        "sphere": 1,
        "min_salary": null,
        "max_salary": null,
        "schedule": null,
        "schedule_comment": "",
        "work_formats": [],
        "register_as_set": [],
        "city": null,
        "vhl": false,
        "working_conditions": "",
        "employee_categories": [],
        "foreign_citizen": false,
        "foreign_countries": [],
        "employee_experience": null,
        "employee_education": null,
        "employee_skills": [],
        "employee_add_skills": [
            {"name": "Linux"},
            {"name": "Android"}
        ],
        "responsibilities_employee": "",
        "qty_employees": 1,
        "payment_for_employee": 0,
        "tariff": 1,
        "qty_recruiters": 1,
        "employee_will_go_to_work_at": null,
        "expected_first_cv_date": null,
        "recruiter_tasks": [],
        "resume_after_interview": false,
        "not_private_person": true,
        "skills_recruiter": "",
        "stop_list": "",
        "created_at": "2024-03-25T22:47:45.783872+03:00",
        "closed_at": null,
        "status": "draft"
}

Response:
{
        "employer": 1,
        "title": "Нужен работник",
        "job_vacancy": 1,
        "sphere": 1,
        "min_salary": null,
        "max_salary": null,
        "schedule": null,
        "schedule_comment": "",
        "work_formats": [],
        "register_as_set": [],
        "city": null,
        "vhl": false,
        "working_conditions": "",
        "employee_categories": [],
        "foreign_citizen": false,
        "foreign_countries": [],
        "employee_experience": null,
        "employee_education": null,
        "employee_skills": [],
        "employee_add_skills": [
            {"name": "Linux"},
            {"name": "Android"}
        ],
        "responsibilities_employee": "",
        "qty_employees": 1,
        "payment_for_employee": 0,
        "tariff": 1,
        "qty_recruiters": 1,
        "employee_will_go_to_work_at": null,
        "expected_first_cv_date": null,
        "recruiter_tasks": [],
        "resume_after_interview": false,
        "not_private_person": true,
        "skills_recruiter": "",
        "stop_list": "",
        "created_at": "2024-03-25T22:47:45.783872+03:00",
        "closed_at": null,
        "status": "draft"
}

``` 

### Модели пользователей:

Кастомный пользователь
```
GET api/v1/customuser/
 
[
    {
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "role": "employer",
        "password": "string"
    }
]

GET /api/v1/customuser/{id}
    {
        "username": "string",
        "first_name": "string",
        "last_name": "string",
        "role": "employer",
        "password": "string"
    }
``` 
Работодатель
``` 
GET api/v1/employer/
[
    {
        "id": 0,
        "user": 0,
        "company": "string",
        "position": "string"
    }
]
``` 
Рекрутер
``` 
GET api/v1/recruiter/
[
    {
        "id": 1,
        "user": {
            "id": 2,
            "username": "vasya",
            "first_name": "Василий",
            "last_name": "Пупкин",
            "full_name": "Василий Пупкин",
            "photo": null,
            "role": "employer",
            "created_at": "2024-03-26T10:22:00.902452+03:00"
        },
        "top10": true,
        "finished_cases": 10,
        "years_of_exp": 10,
        "about_me": "Мастер на все руки"
    },
]


``` 
### Пользователи

#### Василий Пупкин:

логин: vasya

пароль: zxc102938

#### Джо Блэк:

логин: joe

пароль: mko091122

#### Суперпользоаватель:

логин: admin 

пароль: 111111



## Запуск:

#### Загрузка словарей в базу данных:

Сейчас данные загружены через миграции, но в дальнейшем можно данные загрузить с помощью этой команды

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

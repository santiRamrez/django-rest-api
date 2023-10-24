
# Backend Readconnect - Prueba Microsystem

Hola! 😀

Me presento, mi nombre es Santiago Ramírez y si estas leyendo esto es porque estás por evaluar mi prueba técnica para  el cargo de Desarrollador Fullstack Semi Senior.

Este repositorio contiene el backend de la aplicación de libros Readconnect.
Recibí un dataset *no sql - o una colección de libros para ser más preciso* y me tocó hacer un poco de ETL para llenar la base de datos relacional con los libros.




## Tech Stack

**Lenguaje:** Python 3.11

**Framework:** Django 4.2 y Django Rest Api

**Database:** Sqlite



## Run Locally

Clone the project

```bash
  git clone https://github.com/santiRamrez/django-rest-api
```

Go to the project directory

```bash
  cd django-rest-api
```

Crete Python Virtual Enviroment (On Windows)

```bash
  py -m venv .venv
```

Activate the Virtual Environment (On Windows Powershell)

```bash
  ./venv/Scripts/activate.ps1
```

Install all the requeriments

```bash
  pip install -r requirements.txt
```

Go to the Django Project

```bash
  cd readconnect
```

Update the changes at the models of the Quickstart Application

```bash
  py manage.py makemigrations quickstart
```

Update the changes that the db.sqlite3 might not have. 

```bash
  py manage.py migrate
```

Run the local server

```bash
  py manage.py runserver
```

Check the endpoints using **http**

```bash
  http://127.0.0.1:8000/api/
```

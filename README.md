# Design-Lab

## Cloning the Repository

```bash
git clone https://github.com/AdireddiChL/Design-Lab.git
cd Design-Lab
```

## Installing the required packages

- if there is a virtual environment installed in the system follow the bellow commands
	``` bash
	python3 -m venv venv/
	source venv/bin/activate
	<!-- execute venv/Scripts/activate.bat in windows -->
	pip install -r requirements.txt
	```
---
- else install in global packages
	```bash
	pip install -r requirements.txt
	```

## Unzip the `data.zip` file

- Download [data.zip](https://drive.google.com/file/d/1H5HBHMcfxV4v6GsbOtJye3uBZJSTnUkm/view?usp=share_link) inside Design-Lab
- unzip the data.zip folder and place the data folder to apple/ngs/ manually or follow the below commands

```bash
unzip data.zip -d apple/ngs/
```
The final folder structure Should be like

```tree
+-- init.py
+-- apple
|	+-- init.py
|	+-- *.py
|	+-- ngs
|	|	+-- data
|	|	|	+-- *.json
|	|	|	+-- Handwritten_Math_Symbols
|	+-- static
|	+-- templates
+-- mysite
+-- manage.py
+-- README.md
+-- requirements.txt
+-- script.py
+-- venv
+-- data.zip
```

## Initiate the Database

- run the following commands to initiate the Database.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Populate the database

- run the following Django Shell Script to populate the database.

```bash
python manage.py shell < script.py
```

## Create a superuser

```bash
python manage.py createsuperuser
```

## Run the server

```bash
python manage.py runserver
```

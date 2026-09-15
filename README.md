# Calorie Counter Website

## Project Description

The Calorie Counter Website is a Django-based web application that helps users
track their daily food and calorie intake.

The application allows users to add food items together with their calorie
values, view the food items recorded for the current day, edit or delete food
records, calculate the total daily calorie intake, and reset the daily calorie
records.

The project was developed using Django and PostgreSQL, with Tailwind CSS used
to create a responsive and user-friendly interface.

## Project Objectives

The main objectives of this project are to:

- Build a functional web application using Django.
- Store application data using PostgreSQL.
- Allow users to record food items and their calorie values.
- Calculate the total number of calories consumed during the day.
- Provide Create, Read, Update and Delete (CRUD) functionality.
- Validate user input before saving information.
- Create a responsive interface using Tailwind CSS.
- Deploy the application online using Render.
- Follow basic Django security and deployment practices.

## Features

The application provides the following features:

### Add Food

Users can add a food item by entering:

- Food name
- Calorie count

### View Food Items

Users can view all food items recorded for the current day.

Each food record displays:

- Food name
- Calories
- Date added

### Daily Calorie Total

The application automatically calculates and displays the total calories
recorded for the current day.

### Edit Food

Users can edit an existing food record and update its:

- Food name
- Calorie count

### Delete Food

Users can remove an individual food record from the daily list.

### Reset Daily Calories

Users can reset the daily calorie count by removing all food records recorded
for the current day.

### Form Validation

The application validates user input to ensure that:

- A food name is provided.
- The food name is not empty.
- The calorie value is greater than zero.
- Invalid values are not saved to the database.

### Responsive Interface

The application uses Tailwind CSS to provide a clean and responsive interface
that can be used on different screen sizes.

## CRUD Operations

The application implements the four basic CRUD operations:

### Create

Users can create new food records using the Add Food form.

### Read

Users can view food records and the calculated daily calorie total.

### Update

Users can edit existing food records.

### Delete

Users can delete individual food records or reset all records for the
current day.


## Technologies Used

The project was developed using the following technologies:

- **Python 3.10**
- **Django 3.2**
- **PostgreSQL**
- **HTML**
- **Tailwind CSS**
- **Gunicorn**
- **WhiteNoise**
- **Git**
- **GitHub**
- **Render**

## Project Structure

```text
calorie_counter/
│
├── calorie_tracker/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── calorie_tracker/
│       ├── base.html
│       ├── food_list.html
│       ├── add_food.html
│       └── edit_food.html
│
├── build.sh
├── manage.py
├── render.yaml
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
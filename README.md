# Project Name

This project is built using Django, Bootstrap, and HTMX. 
Python ver I used: 3.11.6

## Table of Contents

- [Installation](#installation)
- [A bit about Django](#about-django)
- [File Structures](#file-structures)
- [License](#license)

## Installation
1. Download and install the latest version of Python [here](https://www.python.org/downloads/).

2. Clone this repository

3. Create a virtual environment:
    ```shell
    python -m venv venv
    ```

4. Activate virtual environment: 
    - Windows:
        ```shell
        .\venv\Scripts\activate
        ```
    - MacOS/Linux:
        ```shell
        source venv/bin/activate
        ```

5. Install the project dependencies:
    ```shell
    python -m pip install -r requirements.txt
    ```

6. Configure the database:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Start the development server:
    ```shell
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://127.0.0.1:8000/`

Note: Make sure to be connected to the internet, as because it uses the CDN for some stuffs.

## About Django
### What is Django?
**Definition:**  Django is a high-level, open-source web framework for the Python programming language that enables rapid development and clean, pragmatic design of web applications.

**Origin:** Developed by the Django Software Foundation (DSF) and initially released in 2005.

## Core Features and Characteristics
**1. Batteries-Included Philosophy**

- **Comprehensive Package:** Django comes with numerous built-in features such as authentication, URL routing, a templating engine, an ORM (Object-Relational Mapping), and more.

**2. Admin Interface:** Provides an automatically generated admin interface for managing application data.

**3. MVC Architecture (Model-View-Controller)**

**4. ORM (Object-Relational Mapping)**

- **Database Abstraction:** Allows developers to interact with the database using Python code instead of SQL queries.

- **Database Support:** Supports multiple databases, including PostgreSQL, MySQL, SQLite, and Oracle.


## File Structures
```
.
├── apps #Contains all the apps
│   ├── barang
│   │   ├── admin.py 
│   │   ├── apps.py
│   │   ├── forms.py #Contains all the forms
│   │   ├── __init__.py
│   │   ├── migrations
│   │   ├── models.py #Contains all the models
│   │   ├── tests.py
│   │   ├── urls.py #Contains all the urls
│   │   └── views.py #Contains all the views
│   └── home
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── db.sqlite3
├── fs_admin_panel
│   ├── asgi.py
│   ├── settings.py #The settings of Django
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── dialog.js
├── templates
│   ├── barang
│   │   ├── barang
│   │   │   ├── add-form.html
│   │   │   ├── index.html
│   │   │   ├── list-barang.html
│   │   │   └── update-form.html
│   │   ├── kategori
│   │   │   ├── add-form.html
│   │   │   ├── delete-form.html
│   │   │   ├── idk.html
│   │   │   ├── index.html
│   │   │   ├── list-kategori-barang.html
│   │   │   └── update-form.html
│   │   └── satuan_barang
│   │       ├── add-form.html
│   │       ├── index.html
│   │       ├── list-satuan-barang.html
│   │       └── update-form.html
│   ├── dashboard
│   │   ├── includes
│   │   │   ├── chart-1.html
│   │   │   ├── chart-2.html
│   │   │   ├── chart-3.html
│   │   │   ├── chart-4.html
│   │   │   └── jumlah_barang.html
│   │   └── index.html
│   ├── includes
│   │   ├── navbar.html
│   │   └── sidenav.html
│   └── layouts
│       └── base.html
```


## License

Information about the license for your project.


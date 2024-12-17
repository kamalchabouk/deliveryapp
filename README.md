"""under Process started 15 Dec 2024"""
"""Stoped working on it for on 17 Dec 2024. Will Continue Soon for more advanced topics"""
# Food Delivery App

This is a project where I am building an app that simulates the functionality of **Food Delivery App**. The goal is to create a professional and user-friendly platform for ordering food from local restaurants.


## Overview

The **LifeReno App** simulation is designed to replicate the core features and functionalities of the LifeReno app. It will provide users with the ability to:

- **Browse Services:** Access a variety of services available in the app.
- **Make Orders/Requests:** Users can book or request services as per their needs.
- **Track Orders:** Keep track of their requests and service status.

## Key Features

- **User-Friendly Interface:** An intuitive and responsive design to ensure ease of use.
- **Real-Time Updates:** Live tracking of services and orders.
- **Secure Payment System:** Ensures secure processing of payments for services.

## Technologies Used

- **Backend:** Django Framework (Python)
- #Not Started yet **Frontend:** HTML, CSS, JavaScript (with potential use of frameworks like React and Flutter!!!)
- **Database:** PostgreSQL
- **Version Control:** Git & GitHub

## Setup

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.x installed on your machine.
- Virtual environment tools like `venv` or `virtualenv`.
- PostgreSQL for database management.
- Git for version control.

---

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kamalchabouk/deliveryapp.git
   cd deliveryapp
   ```

2. **Set Up a Virtual Environment**

   Create and activate a virtual environment to isolate project dependencies.

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Required Dependencies**

   Install the dependencies listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   Ensure PostgreSQL is installed and running. Create a new database for the project:

   ```sql
   CREATE DATABASE deliveryapp;
   ```

   Update the `settings.py` file in the Django project to include your database credentials:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'deliveryapp',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run Migrations**

   Apply the initial database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**

   Create an admin user to access the Django Admin interface:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/` to see the app in action.

---

## Additional Notes

- **Environment Variables:** Use a `.env` file to store sensitive information like database credentials or API keys. Use the `python-decouple` library to manage environment variables.
- **Static Files:** Make sure to run `python manage.py collectstatic` when deploying the app.
- **Testing:** To run the tests, use the command `python manage.py test`.

---

Feel free to contribute to the project by creating pull requests or opening issues for suggestions and improvements!


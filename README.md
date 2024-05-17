## Project : Develop a secure back-end architecture using Django ORM

### Table of contents :
1. Project description/Scenario.
2. Compatible configurations.
3. Installing the program.
4. Features.
5. Authentication and permissions.
6. Running the program.
7. User Management via Django Admin Site.

## 1. Project description/Scenario :

This project was carried out as part of the Python Developer training offered by OpenClassrooms.

Epic Events, a renowned event consulting and management company known for its "epic parties,"
is facing an urgent situation following a cyberattack on the external provider 
we relied on for our CRM. This attack has compromised the integrity of some customer information,
making it imperative to act swiftly to restore our clients' trust.

To proactively address this challenge, Epic Events has decided to develop
a secure in-house CRM system. This initiative aims to reassure our clients about the safety
of their data and demonstrate our commitment to the professional management of their events.

To achieve this goal, I have been entrusted with designing the first version of the CRM. 
This custom solution will meet the specific needs of our company and help solidify our reputation
as a leading provider for exceptional events. 

## 2. Compatible configurations :

* Python 3
* Windows 10
* MacOS
* Linux

## 3. Installing the program :
This program uses the following Python libraries :

```
asgiref 3.7.2
backports.zoneinfo 0.2.1
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 3.2.0
cryptography 41.0.2
defusedxml 0.7.1
Django 4.2.2
django-allauth 0.54.0
django-phonenumber-field 7.1.0
django-rest-auth 0.9.5
django-rest-authtoken 2.1.4
djangorestframework 3.14.0
djangorestframework-simplejwt 5.2.2
idna 3.4
oauthlib 3.2.2
phonenumbers 8.13.15
psycopg2-binary 2.9.6
pycparser 2.21
PyJWT 2.7.0
python3-openid 3.2.0
pytz 2023.3
requests 2.31.0
requests-oauthlib 1.3.1
six 1.16.0
sqlparse 0.4.4
typing_extensions 4.7.0
urllib3 1.26.6

```

## 4. Features :

### Access to data through endpoints, which are divided into four categories : 

  * Authentication
  * Teams-Employees
  * Customers-Contracts
  * Contracts-Events

  For a detailed explanation of the API and its endpoints, refer to the [**documentation**](https://documenter.getpostman.com/view/25420128/2s946cfDj2).

## 5. Authentication and permissions :
    
  * The **authentication** for the back-end is provided by Django Rest Framework Authentication.
  * For the **authorization** and **access** part, various **permissions** have been implemented
  according to the status of the user making the request and in accordance with the specifications.

## 6. Running the program :

1. Open a terminal (e.g., Cygwin for Windows, the Terminal for Mac) or in an IDE (e.g., PyCharm).
2. Clone the repository into a local directory :
  > $<b> git clone repository path</b> 
3. Navigate to this folder in the terminal.
4. Create a virtual environment with :
  > $<b> python -m venv <nom de l'environnement></b> 
5. Activate the virtual environment via :
  > $ <b>source env/bin/activate</b>  (sur MacOS et Linux) 

  > $ <b>env\Scripts\activate.bat</b> (sur Windows)
6. Install the packages present in the requirements.txt file (this file is located in the project
folder with main.py) with:
  > $ <b>pip install -r requirements.txt</b> 
7. Run the development server with:
> $ <b>python manage.py runserver</b>
8. Visit the site at the following address and access the various endpoints:

      **http://127.0.0.1:8000/**

## 7. User Management via Django Admin Site :

1. Create a Super User with the following command :
 > $ <b>python manage.py createsuperuser </b> 
2. Log in with this user at this address :
 **http://127.0.0.1:8000/admin/**
3. Only this Super User will have full access to the application and the various CRUD operations.
When creating a new user, they can assign the user to one of the three available permission groups:

   * Management-Team
   * Sales-Team
   * Support-Team
---
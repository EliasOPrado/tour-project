# Tour Project

[![Build Status](https://travis-ci.org/EliasOPrado/tour-project.svg?branch=master)](https://travis-ci.org/EliasOPrado/tour-project)

<img src="static/images/readme_images/mockup.png" >

Project Milestone Four - Code Institute

The Tour Store app was developed and deployed by Elias Prado as the last project for the Code Institute Software Development diploma.
This website is to emulate a touristic retreat webpage that provides for tourists different places to retreat and relax.

## Table of contents
<!--ts-->

1. [UX](#UX)
    1. [User goals](#User-goals)
    2. [Design choices](#Design-choices)
    3. [Colors](#Colors)
    4. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Reset password](#Reset-password)
    2. [Tour store](#Tour-store)
        1. [Home page](#Home-page)
        2. [Retreats](#Retreats)
        3. [Retreat details](#Retreat-details)
    3. [Cart](#Cart)
    4. [Checkout](#Checkout)
    5. [Search](#Search)
    6. [404 page](#404-page)
    7. [Admin page](#Admin-page)
    8. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
      - You can find the [TESTING.md](TESTING.md) file here.
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
    3. [Add static files to AWS s3](#Add-static-files-to-AWS-s3)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)
    3. [Acknowledgment](#Acknowledgment)
 <!--te-->

# UX

## User goals
The target audience of Tour Project are:
- People who want to make a relax or spiritual trip.
- People who are looking for the best locations.
- Yoga practitioners who are looking for the best places to improve their spiritual, mind and body development.

User goals:
- Search for the retreat or destination by its keyword and receive a feedback by the website if it isn't available.
- Find information about the company such as address phone number and its mission.
- Finding the destination, the user can find details of it, such as text and picture based content related to the destination.
- The user can scroll on the retreat page and through different paginations.
- Also, be able to see a preview image of the destination, date and price on a card container.
- The user can also add comments to the destination they want.
- Add one or multiple trips to the shopping cart with the maximum ten people for each tour.
- Clicking on add he or she will be redirected to the cart page.
- If the user is not logged in they will be redirected to the login page before go to the cart page.
- Edit the shopping cart if required.
- Checkout using card payment.
- Once the payment is done a success message is sent below the navbar and disappear on three seconds after the user be redirected to the home page.

## Design choices
The Tour project website is a tour application that has its main customers, people who want to have a relax and spiritual retreat.
Therefore, the website design was designed to bring these characteristics to its users. In which all of its design details is aligned to its purpose.

### Fonts
- The font used in this project is [Roboto](https://fonts.google.com/specimen/Roboto#about) which is an user friendly mainly used by its creator Google to give a proper reading in different screen sizes.

### Colors
   - Cyan: ![#17a2b8](https://via.placeholder.com/15/17a2b8/000000?text=+) `#17a2b8`
   - Light-cyan: ![#D7FFFE](https://via.placeholder.com/15/D7FFFE/000000?text=+) `#D7FFFE`
   - Raven: ![#6c757d](https://via.placeholder.com/15/6c757d/000000?text=+) `#6c757d`
   - Dark-gray: ![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) `#343a40`
   - Green: ![#28a745](https://via.placeholder.com/15/28a745/000000?text=+) `#28a745`
   - White: ![#fff](https://via.placeholder.com/15/fff/000000?text=+) `#fff`
   - Selago: ![#FFFEFF](https://via.placeholder.com/15/FFFEFF/000000?text=+) `#FFFEFF`
   - Light: ![#f8f9fa](https://via.placeholder.com/15/f8f9fa/000000?text=+) `#f8f9fa`
   - These set of colors were chosen to bring a smooth experience to the users as same as to match with the purpose of the application.

#### Styling
  - Box shadow in card to give a depth idea and contrast with the background.
  - Scroll effects to give a better experience to users.
  - Skew-y effect on index page to break standard pattern with linear gradient using light-cyan and Selago colors.

### Wireframes
The wireframes developed for this project was only taken three types of devices, desktop, tablet and mobile.
In addition, the tool used to develop this wireframes was [Balsamiq](https://balsamiq.com/) giving the ability to a rapid design.
  - [Mobile devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/Mobile_wireframes.png)
  - [Tablet devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/iPad_wireframes.png)
  - [Desktop devices](https://tour-project.s3-eu-west-1.amazonaws.com/static/images/readme_images/Desktop_wireframes.png)

# Features

Tour Store website is composed by five different applications: `accounts`, `cart`, `checkout`, `search` and `tour_store`. Using MVC architecture from the Django framework, each application holds its own model, view and controller that interacts all together into the `main_tour_folder` which basically is the controller of the overall application.

## Accounts
 The accounts app holds the functionality of register, login, logout and the reset password.

### Register page
<p align="center">
<img src="/static/images/readme_images/register.png" width="40%">
</p>

  - An username, email and password is required to create an account.
  - Username must be unique.
  - Password should not be short, must contain at least 8 characters and should not be common.
  - As soon as the user creates its username they are redirected to home page.

### Login page
<p align="center">

<img src="/static/images/readme_images/login.png" width="40%">
</p>
  - The login page is a normal page that will ask for the name or email and the user password who already registered their account.

### Reset password
  - Step 1: at the login page, above of the button you can find the `forgot my password` link in which will lead to a form to add your account email.
  - Step 2: Add the email from the account you need to reset the password.
  - Step 3: You will receive an email with a link that will allow you to add a different password sending you to a reset password form.
  - Step 4: Add a new password and confirm it.
  - Step 5: Once the password is set you can login with the new password.

  <img src="/static/images/readme_images/passwordreset.png">

## Tour store

Tour store app holds all the main pages in which the user will navigate. Such as:

#### home page

  <img src="/static/images/readme_images/transparent_navbar.png">

  - On the home page the navbar is displayed transparent to give a good UI to the project. However, once the user scroll the page down it becomes white to better contrast from the rest of the page and not confuse the user.

    <img src="/static/images/readme_images/top_locations.png">

  - The top location brings a set of three different location or retreats in which users can click and be redirect to the destination page.

    <img src="/static/images/readme_images/testimonials.png">

  - On the testimonials section the three different characters is displayed as one of the Tour Project past customers. Giving their experience to the user and how many stars the service bring in term of value to their lives.

    <img src="/static/images/readme_images/aboutus.png">

  - The about us section (on the left side) details the experience of the business (in which is fictitious) and display a contact form (on the right side) for users to send any query about the business.

   <img src="/static/images/readme_images/footer.png">

  - On the footer section the user will have a copy message, links for retreats and login or logout and the business contact such as phone numbers, email and address. Also icons of different social medias.

### Retreats
<p align="center">
 <img src="/static/images/readme_images/retreats_page.png" width="40%">
 </p>

  - The retreats page will display all of the retreats.
  - However, the pagination system will only display three destinations per page to not overload the page if there are a large amount of items.

### Retreat details  
  - The page that gives the full detail about the retreat as well as the possibility to add it to cart.
  - In addition, the formatting functionality that can be applied by the website admin.
  - The user can also on the top right corner add the destination to cart.

## Cart

<img src="/static/images/readme_images/cart_image.png">

 The cart app gives the user the ability to `view`, `add` and `adjust` the cart as they wish. Including more or less retreats to their trip package.
  - Besides the destination the user will have a card that will allow them to add how many people will go to the trip.
  - `Important`: Since this project is to provide the user to add retreats to card, they will not be able to book the trip. Where in an actual case, once it's paid the booking should have done directly to the business management. Therefore, in the future a book system will be developed to provide a better experience to customers.

## Checkout

<p align="center">
<img src="/static/images/readme_images/checkout_image.png" width="40%">
</p>

  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.
  - In this application is developed and performed the forms users who are willing to buy any retreat, to plot their details into the checkout application forms and finalise the purchase.


## Search
  - Under the search application, a simple search functionality is used to find different destinations from the `Destinations` model by the tour title as the key word retrieved.
  - If a user adds one or multiple destinations that is in the database, it will be retrieved and shown on destination page.
  - If the tour title plotted on the search bar doesn't have in the data base, a message will be displayed instead, describing that destination is not yet added in the database.

## 404 page

<p align="center">
<img src="/static/images/readme_images/four.png" width="40%">
</p>

  - Simple page 404 for when an error occur and give the ability to not lost the user, sending them back to the home page.

## Admin page

<p align="center">
<img src="/static/images/readme_images/admin_login.png" width="40%">
</p>

  - The admin login page was changed by the name of the website.

<p align="center">
<img src="/static/images/readme_images/admin.png" width="40%">
</p>

  - The admin page was separated by three sections:
     - Authentication and Authorization, where the admin can see and manage the users on the website.
     - Checkout, where the admin can see the orders done by the customers.
     - Tour store, where the admin will be able to check and approve comments and see the contacts done by prospects.

<p align="center">
<img src="/static/images/readme_images/wysiwyg.png" width="40%">
</p>

  - The WYSIWYG (what you see is what you get) functionality was implemented as a functionality from a third party application called [Ckeditor](https://ckeditor.com/). Where the normal text editor was changed to add more features such as:
     - Alignment
     - Tables
     - Images
     - Styling
     - Add more html elements
     - And much more.


## Features Left To Implement
  1. Admin page graphs to display data from comments, sales and views.
  2. Booking system to automate sales.
  3. Add multiple images on retreat preview such as horizontal carousel.
  4. Add tutor section for each retreat.
  5. Add real location with maps at the bottom of each retreat detail page.
  6. Add star based review.

# Technologies

## Tools

  - [Atom](https://atom.io/) as an IDE to develop this project.
  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [AWS S3](https://aws.amazon.com/s3/) was used as a cloud service to host static files.
  - [Github](https://github.com/) to share and store code remotely.
  - [Git](https://git-scm.com/) was used to manage version control.
  - [CkEditor](https://ckeditor.com/docs/) was used to better format texts without the need to do within the code.
  - [Sqlite3](https://www.sqlite.org/index.html) a database provided by django for development.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production development.
  - [Travis CI](https://travis-ci.org/) for continuous integration and testing.
  - [Canva](https://www.canva.com/) was used to design images on the web.
  - [Balsamiq](https://balsamiq.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [FontAwesome](https://fontawesome.com/) for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) a template language for python used to bring logic into templates.
  - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python PostgreSQL adapter.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.
  - [AOS](https://michalsnik.github.io/aos/) used to bring animation on scroll.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.


# Testing

The testing information can be found in this separated [Testing](TESTING.md) file.


# Deployment

For the deployment you will need tool as:

  - An IDE such as [Atom](https://atom.io/) or [Visual Studio Code](https://code.visualstudio.com/).
  - Have installed in your machine [Python 3](https://www.python.org/downloads/) and [Git](https://git-scm.com/).

To continue on the process of deployment you should have accounts on the following services:

  - [Stripe](https://stripe.com/ie)
  - [AWS](https://aws.amazon.com/s3/)
  - [Gmail](https://gmail.com)

### Instructions
  1. Download a copy of this repository from the link https://github.com/EliasOPrado/tour-project as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/EliasOPrado/tour-project
      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.
  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
  4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
  5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
  6. Create an `env.py` file to store environment variable keys.

     ```
     import os

     os.environ.setdefault('SECRET_KEY', '<secrete key>')
     os.environ.setdefault('DATABASE_URL', '<postgres key>')

     """ STRIPE API Keys """
     os.environ.setdefault('STRIPE_PUBLISHABLE', '<stripe publishable key>')
     os.environ.setdefault('STRIPE_SECRET', '<stripe secret key>')

     """ AWS API Keys """
     os.environ.setdefault('AWS_ACCESS_KEY_ID', '<aws access key id>')
     os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<aws secret access key>')

     """ Email Keys """
     os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
     os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')
     ```
  7. Add a git ignore file to not submit sensitive data to Github repository.

     ```
     $ touch .gitignore
     ```
     - Then add the `env.py` to the `.gitignore` file.

     ```
     $ git update-index --assume-unchanged env.py
     ```
     - Depending where the the `env.py` is locate the path will change.

  8. Migrate the models to crete a database template.

      ```
      $ python manage.py migrate
      ```
  9. In this step you will need to create a super user to have access to the admin page.

      ```
      $ python manage.py createsuperuser
      ```
  10. So, after you do all the steps to create a super user you can now run the server.

      ```
      $ python manage.py runserver
      ```
  11. After the server is running locally add the `/admin` path at the end of the url link. It might look like this if you are not running another application.

      ```
      http://127.0.0.1:8000/admin
      ```

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
  4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
  5. Create a file named `Procfile` and add the following config.
     ```
     web: gunicorn main_tour_folder.wsgi
     ```
 6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
 7. In your `Heroku`account click new and create new app.
 9. Select your region and create a name for your project.
10. In your `Heroku` settings click `reveal config vars`.
11. Add the following config variables:

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_ADDRESS| `<your email address>`  |
| EMAIL_PASSWORD | `<your email password>` |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLISHABLE| `<your stripe publishable key>`  |
| STRIPE_SECRET| `<your stripe secret key>`  |
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |

12. Add a development (postgres) database:
  ```
  $ heroku addons:add heroku-postgresql:dev
    heroku addons:add heroku-postgresql:dev
    Adding heroku-postgresql on deploy_django... done, v13 (free)
    Attached as HEROKU_POSTGRESQL_COPPER_URL
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pgbackups:restore.
    Use `heroku addons:docs heroku-postgresql` to view documentation.

  $ heroku pg:promote HEROKU_POSTGRESQL_COPPER_URL
    Promoting HEROKU_POSTGRESQL_COPPER_URL to DATABASE_URL... done
   ```
13. After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a test-app-to-deploy`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.

### Add static files to AWS s3

1. If there is a need to add your static files to AWS S3 you can follow [this stutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

# Credits

## Media
  - The photos and video used in the project were downloaded from [Pexels](https://www.pexels.com/) and [Pixabay](https://pixabay.com/). Platforms that provides no-copyright media and free downloads.

## Code
  - This application was developed using [StartBootstrap](https://startbootstrap.com/templates/) templates and [snippets](https://startbootstrap.com/snippets/). But during the development good part of the original template and snippets were modified.
  - The 404 page snippet was acquired from [Bootsnipp](https://bootsnipp.com/snippets/).
  - The transparent navigation bar was acquired from [Bootstrapious](https://bootstrapious.com/p/transparent-navbar)
  - The `accounts`, `cart` and `checkout` apps were recycled from the [Code Institute](https://github.com/Code-Institute-Org) lessons but modified to fit with the project purpose.

## Acknowledgment
  - I received inspiration for this project from the [Retreat Guru](https://retreat.guru/) website.

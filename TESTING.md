# Tour Project - Testing

[Main README file](Readme.md)
[Live website](https://tour-application.herokuapp.com/)

## Table of contents

1. [Django TestCase](#Django-TestCase)
    1. [Test config for this project](#Test-config-for-this-project)
    1. [Command used to trigger the tests](#Command-used-to-trigger-the-tests)
2. [Travis-CI](#Travis-CI)
3. [Manual testing](#Manual-testing)
      1. [Tour store App](#Tour-store-App)
      1. [Home page](#Home-page)
      1. [Destination page](#Destination-page)
      1. [Travis-CI](#Travis-CI)
4. [Accounts app](#Accounts-app)
    1. [Register page](#Register-page)
    1. [Login page](#Login-page)
    1. [Reset password pages](#Reset-password-pages)
5. [Cart app](#Cart-app)
6. [Checkout](#Checkout)
7. [Web testing](#Web-testing)
    1. [Mobile](#Mobile)
    2. [Tablet](#Tablet)
    3. [Laptop](#Laptop)
    4. [Screen](#Screen)
8. [Validation services](#Validation-services)


## Django TestCase

I used TestCase for the testing of the majority of the views, models, urls and forms. However, there are some views and models that I could not test due to the complexity and limited time to apply them. The apps that I could not test the views and models was the `cart` and `checkout` apps.

Another point to mention is that the tests should be added in local database as I did not learned how to apply them into the production database.
Instead you should configurate the local database to run the tests.

### Test config for this project

The configuration for this project is to run with two types of databases Postgres and Sqlite3 (local):

```
# Comment the first db to run the test
# Production db

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Local db
    print("Postgres URL not found, using sqlite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```

So to run the test and check the output, you need to remove or comment the first database (Postgres) and run the command to see the test output

### Command used to trigger the tests
  - `$ python manage.py test`

  - Output:

```
----------------------------------------------------------------------
Ran 37 tests in 10.288s

OK
Destroying test database for alias 'default'...
```

## Travis-CI

In this project was used travis for continuous integration service. In which a test is done every time the project is deployed to github.

## Manual testing

### Tour store App

#### Home page
  1. Check navbar links to see whether they are sending to the real url.
  2. Add keyword on the `search` bar and check if it brings the result asked or a feedback message.
  3. Click on the destination cards on the second container to see if they are leading to the corresponding page.
  4. On the contact form add the name, email, subject and message checking if it will be submitted.
      1. During the test of the contact form these errors were found:
        1. The form was submitted but the fields weren't cleared, I had to add a `redirect()` method to redirect to clear the form.
  5. Check if all the links on footer are working proper.

#### Destination page
  1. Check if links of buttons and images are leading to the proper page or breaking the page.
  2. Check if the pagination is working fine, leading to the corresponding page.

#### Destination details page
  1. At the home page there are three ways to go to the destinaion details page.
      1. At the navbar on retreats link.
      2. On one of the three or four containers with the tour title.
      3. Searching for a specific detail on the search form.
  2. In the destination detail, testing the comment form.
      1. Add your name, email and comment.
      2. Click submit.
      3. Wait for a message for awaiting moderation.
         1. Error found: The `if` conditional container was inside of the same comment card container. Making it to break the responsiveness.
         2. To solve this I removed the `if` conditional container with the message to outside of the comment card container.
  3. Testing the add to cart.
      1. Under the Number of people form chose how many people with max 10 people.
      2. Click the add button.
      3. The add button will redirect to the cart page and add the amount of people choosed to cart icon on navbar.

#### 404 page
  1.  On Home page url `https://tour-application.herokuapp.com/random` add a random name at the end and check if the 404 page is working.

### Accounts app

#### Register page
  1. At the home page click on register.
  2. On the register page add your name, email address and password twice.
  3. If password only use letters it will not work, digits and symbols must be applied.
  4. If the register page be successful the register page will redirect to the home page with a message the user is registered or logged in.

#### Login page
  1. Add your user name or email and password.
  2. If the username or email and password works well the user will be redirected to the home page already logged in.

#### Reset password pages
  1. At the login page click on the `forgot my password` link.
  2. Add your email address linked to the account.
  3. Receiving the email address click on the link to reset the email.
  4. Add new password twice.
  5. Click on the login page to be authorised.

### Cart app
  1. On the destination detail page click on add to cart.
  2. Click on the bin icon to remove or decrease the item from cart if needed.
  3. Click on the button checkout to be redirected to login if you are not logged in or checkout if you already is logged.

### Checkout
 following the step 3 of the cart app, add the following details:

  1. Full name, phone number, country, postcode, town or city, street address 1 and 2 and county.
  2. For the credit card number you should add `4242424242424242`, any cvv and a correspondent data in the future.
  3. Click on the submit payment button.
  4. If the payment went through you will be redirected to the destinations page and receive a message you payment was successful.
  5. If the payment doesn't go through you will receive a message the card was not accepted.

## Web testing

The devices the application was tested were:

### Mobile
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 4
  - iPhone 5 SE
  - iPhone 6, 7 and 8
  - iPhone 6, 7 and 8 Plus (real device)
  - iPhone X

### Tablet
  - iPad
  - iPad Pro

### Laptop
  - Macbook

### Screen
  - Sony 42"

For the web testing I used Chrome dev tools and Safari web tools to find bugs, errors and test new styles for HTML, CSS and JavaScript.

## Validation services
  - [W3C Markup validation](https://validator.w3.org/)
  - [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
  - [JS Hint](https://jshint.com/)

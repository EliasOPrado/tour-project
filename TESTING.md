# Tour Project - Testing

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

### Home page

    1. Check navbar links to see whether they are sending to the real url.
    2. Add keyword on the search bar and check if it brings the result asked or a feedback message.
    3. Click on the destination cards on the second container to see if they are leading to the corresponding page.
    4. On the contact form add the name, email, subject and message checking if it will be submitted.
       1. During the test of the contact form these errors were found:
          1. The form was submitted but the fields weren't cleared, I had to add a `redirect()` method to redirect to clear the form.
    5. Check if all the links on footer are working proper.

### Destination page

    1. Check if links of buttons and images are leading to the proper page or breaking the page.
    2. Check if the pagination is working fine, leading to the corresponding page.

### Destination details page

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

### 404 page

    1.  

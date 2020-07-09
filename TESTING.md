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

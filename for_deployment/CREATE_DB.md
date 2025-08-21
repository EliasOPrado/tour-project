## Create Production Database
1. Switch to the PostgreSQL superuser
sudo -u postgres psql

2. Inside psql, run:
-- Create the database
CREATE DATABASE tour_project;

-- Create the user
CREATE USER elias WITH PASSWORD 'minhasenha1234';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE tour_project TO elias;

-- (Optional) Make user owner
ALTER DATABASE tour_project OWNER TO elias;

3. Exit psql
\q

4. Run Django migrations to set up tables

From your project folder:

python manage.py migrate

5. (Optional) Create Django superuser
python manage.py createsuperuser

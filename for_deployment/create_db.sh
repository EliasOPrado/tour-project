#!/bin/bash

# ------------------------------
# Variables (update if needed)
# ------------------------------
DB_NAME="tour_store"
DB_USER="elias"
DB_PASSWORD="minhasenha1234"
DB_HOST="localhost"
DB_PORT="5432"

# ------------------------------
# Create PostgreSQL user if it doesn't exist
# ------------------------------
echo "Checking if user $DB_USER exists..."
USER_EXISTS=$(psql -U postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'")

if [ "$USER_EXISTS" = "1" ]; then
    echo "User $DB_USER already exists."
else
    echo "Creating user $DB_USER..."
    psql -U postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
fi

# ------------------------------
# Create database if it doesn't exist
# ------------------------------
echo "Checking if database $DB_NAME exists..."
DB_EXISTS=$(psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'")

if [ "$DB_EXISTS" = "1" ]; then
    echo "Database $DB_NAME already exists."
else
    echo "Creating database $DB_NAME owned by $DB_USER..."
    psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
fi

# ------------------------------
# Grant privileges
# ------------------------------
echo "Granting all privileges on $DB_NAME to $DB_USER..."
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

echo "✅ Database $DB_NAME setup completed!"

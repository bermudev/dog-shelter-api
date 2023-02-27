# Dog Shelter API built with Flask and Python

## What does the API do?

Here's a short list explaining what the updated version of the API does:

- Allows users to register for an account and authenticate themselves using user and password. Some endpoints are protected after authentication and administration permissions.
- Allows users to manage dogs by adding, retrieving, updating, and deleting dogs, as well as adding, retrieving, updating, and deleting information about their adoption status, vaccinations, and health status.
- Provides API documentation in Swagger using Flask-Smorest.
- Provides informative error messages in case of failed requests.
- Uses SQLite as the database management system to store and manage the data.

## Flask resources and technologies used

Some of the Flask tools used for the creation of these APIs are:

- **Flask-Smorest** for automatic API documentation, defining serialization and data validation schemes, and for simplified resource definition.
- **Flask-SQLAlchemy** to define database models, create database connections and execute SQL queries.
- **Flask-JWT** for authentication and authorization based on JSON Web Tokens (JWT).

## Database design

This is going to be the final design of the project database, I have expanded the original idea and modified some fields with the suggestions of some dog-loving friends. It does not include the user part for login.

![Database design](https://i.imgur.com/iYKokHv.png)

## Endpoints

The API has the following endpoints for each table, those marked with 🔒 require valid authentication and DELETE methods need admin rights:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /api/user/{id} | Retrieve details of a specific user by ID |
| POST | /api/register/ | Add a new user to the shelter database |
| POST | /api/login/ | Login to the API using the username and password |
| POST 🔒 | /api/logout/ | Logout from the API |
| POST 🔒 | /api/refresh/ | Get a new token from the API |
| DELETE 🔒 | /api/dogs/{id} | Delete an user from the shelter database |

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /api/dogs/ | Retrieve a list of all dogs available for adoption |
| GET | /api/dogs/{id} | Retrieve details of a specific dog by ID |
| POST 🔒 | /api/dogs/ | Add a new dog to the shelter database |
| DELETE 🔒 | /api/dogs/{id} | Remove a specific dog from the shelter database |

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /api/vaccines | Retrieve a list of all vaccines for a specific dog |
| GET | /api/vaccines/{id} | Retrieve details of a specific vaccine for a specific dog |
| POST 🔒 | /api/vaccines | Add a new vaccine for a specific dog |
| DELETE 🔒 | /api/vaccines/{id} | Remove a specific vaccine for a specific dog |


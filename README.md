# Capstone Project
#### Welcome to our Capstone Api Project

### Getting Started
You need to install python latest version:
  + [Python 3.8.6](https://www.python.org/) 
  
### Heroku 
    This project will run as a live application at this URL:
    https://hello-world-elbek.herokuapp.com/movies
        
  
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` 
## In this API you can do some METHODS:

- __Actors__ `/movies`
    + GET
    + POST
    + DELETE
    + PATCH
- __Movies__ `/actors`
    + GET
    + POST
    + DELETE
    + PATCH
    
# _Movies_ `/movies`    
### GET `methods=['GET']`

- **Usage**:
    + Used to access all movies without any permissions using cURL or .http file
- **Request Arguments**:
    + Permission `get:movies` or Role 'At least Assistant'         
- **Returns**
    + It return Jsonified movie details:
        + success - To know the status of process
        + movies - returns paginated movies
        + len_movies - calculate length of movies
- **Example**:
    ```
    curl http://127.0.0.1:5000/movies
    ```
- **Response**:
    ```
    {
        "len_movies": 5, 
        "movies": [
            {
              "genre": "Action", 
              "id": 1, 
              "release_date": "2017.01.01", 
              "title": "Divergent"
            }, 
            {
              "genre": "Fantasy", 
              "id": 2, 
              "release_date": "2019.02.05", 
              "title": "Avengers:EndGame"
            }, 
            {
              "genre": "Action", 
              "id": 3, 
              "release_date": "2016.05.06", 
              "title": "Captain America. Winter Soldier"
            }, 
            {
              "genre": "Fantasy, Adventure", 
              "id": 4, 
              "release_date": "2015.05.15", 
              "title": "Lara Croft"
            }, 
            {
              "genre": "Fantasy", 
              "id": 5, 
              "release_date": "2020.06.22", 
              "title": "John"
            }
        ], 
        "success": true
    }
    ```
### POST `methods=['POST']`
- **Usage**:
    + Used to add new movie to database
- **Request Arguments**:
    + title
    + genre
    + release date  
        + Permission `post:movies` or Role  
- **Returns**
    + success - To know the status of process
    + message - The Movie is successfully created
- **Example**:
    ```
        curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" 
       -d '{ "genre": "Horror", "release_date": "2021.11.11", "title": "Hobbit"}'   
    ```
  OR
    ```.http request
    POST http://127.0.0.1:5000/movies
    Content-Type: application/json

    {"title": "Hobbit", "genre": "Horror", "release_date": "2021.11.11"} 
    ```
- **Response**:
    ```bash
        {
            "message": "The Movie is successfully created",
            "success": true
        }
    ```

### PATCH `methods=['PATCH']`
- **Usage**:
    + Used to patch movie
- **Request Arguments**:
    + title(optional)
    + genre(optional)
    + release date(optional)
        + Permission or Role    
- **Returns**
    + success - To know the status of process
    + message - The Movie Successfully updated!
- **Example**:
    ```
    curl http://127.0.0.1:5000/movies/5 -X PATCH -H "Content-type: application/json" -d '{"title": "Harry Potter"}'      
    ```  
    OR
    ```http request
    PATCH http://127.0.0.1:5000/movies/5
    Content-Type: application/json

    {"title": "Harry Potter"}
    ```  
- **Response**:
    ```
    "message": "The Movie is successfully updated",
    "success": true
    ```
### DELETE `methods=['DELETE']`
- **Usage**:
    + Used to delete movie from table
- **Request Arguments**:
    + Permission `delete:movies` or Role
- **Returns**:
    + success - To know the status of process
    + message - The Movie Successfully deleted!
- **Example**:
    ```
    DELETE http://127.0.0.1:5000/movies/3
    Content-Type: application/json
    ```         
- **Response**   
    ```
    "message": "The Movie is successfully deleted",
    "success": true
    ```

# _Actors_ `/actors`
### GET `methods=['GET']`

- **Usage**:
    + Used to access all actors without any permissions using cURL or .http file
- **Request arguments**    
    + Permission `get:actors` or Role
- **Returns**
    + It return Jsonified actor details:
        + success - To know the status of process
        + actors - returns paginated actors
        + len_actors - calculate length of actors
- **Example**:
    ```
    curl http://127.0.0.1:5000/actors
    ```
- **Response**:
    ```
    {
        "actors": [
            {
              "age": "24", 
              "gender": "Famale", 
              "id": 1, 
              "name": "Emma Watson", 
              "role": "Friend Harry"
            }, 
            {
              "age": "32", 
              "gender": "Male", 
              "id": 2, 
              "name": "Daniel Radcliffe", 
              "role": "Harry Potter"
            }, 
            {
              "age": "47", 
              "gender": "Male", 
              "id": 3, 
              "name": "Jim Carrey", 
              "role": "The Mask"
            }, 
            {
              "age": "52", 
              "gender": "Male", 
              "id": 4, 
              "name": "Robert Downey Jr", 
              "role": "Iron Man"
            }, 
            {
              "age": "48", 
              "gender": "Male", 
              "id": 5, 
              "name": "Johnny Depp", 
              "role": "Captain"
            }
        ], 
        "len_actors": 5, 
        "success": true
    }
    ```
### POST `methods=['POST']`
- **Usage**:
    + Used to add new actor to database
- **Request Arguments**:
    + name
    + age
    + role
    + gender  
        + Permission `post:actors` or role   
- **Returns**
    + success - To know the status of process
    + message - The Actor is successfully created
- **Example**:
    ```
        curl -X POST http://localhost:5000/actors -H "Content-Type: application/json" 
       -d '{"name": "Brad Pitt", "age": "51", "role": "Mr.Smith", "gender": "Male"}'   
    ```
  OR
    ```.http request
    POST http://127.0.0.1:5000/actors
    Content-Type: application/json

    {"name": "Brad Pitt", "age": "51", "role": "Mr.Smith", "gender": "Male"} 
    ```
- **Response**:
    ```bash
        {
            "message": "The Actor is successfully created",
            "success": true
        }
    ```

### PATCH `methods=['PATCH']`
- **Usage**:
    + Used to patch actor
- **Request Arguments**:
    + name(optional)
    + age(optional)
    + role(optional)
    + gender(optional)
        + Permission or Role    
- **Returns**
    + success - To know the status of process
    + message - The Actor Successfully updated!
- **Example**:
    ```
    curl http://127.0.0.1:5000/actors/2 -X PATCH -H "Content-type: application/json" -d '{"name": "Ozodbek Nazarbekov"}'      
    ```  
    OR
    ```http request
    PATCH http://127.0.0.1:5000/actors/2
    Content-Type: application/json

    {"name": "Ozodbek Nazarbekov"}
    ```  
- **Response**:
    ```
    "message": "The Actor is successfully updated",
    "success": true
    ```
### DELETE `methods=['DELETE']`
- **Usage**:
    + Used to delete actors from table
- **Request Arguments**:
    + Permission `delete:actors` or Role
- **Returns**:
    + success - To know the status of process
    + message - The Actor Successfully deleted!
- **Example**:
    ```
    DELETE http://127.0.0.1:5000/actors/3
    Content-Type: application/json
    ```         
- **Response**   
    ```
    "message": "The Actor is successfully deleted",
    "success": true
    ```
  
# Errors Handlers

- There are 5 types of "Error Handlers" in this API
    + 400 - Bad Request
    + 404 - Not Found
    + 422 - Unprocessable Request
    + 500 - Method Not Allowed
    + 200 - OK
    

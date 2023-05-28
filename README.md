## [SportsGames BACKEND](https://github.com/Jyustin/tri3NATMdevsBackend)
Runtime link: https://tri3dev.duckdns.org/

### GETTING STARTED

- Cloning the Backend Repository for Transferability

```bash
mkdir ~/vscode; cd ~/vscode

git clone [https://github.com/Jyustin/tri3NATMdevsBackend.git]
cd tri3NATMdevsBackend
```

### Run Server or run VSCode

- Run nix shell (virtual environment)

```bash
nix-shell ./env
```

- Run from Terminal without VSCode

    - Run python from command line and check server
    ```bash
    python main.py
    ```

- Prepare VSCode and run
    
    - From Terminal run VSCode
    ```bash
    code .
    ```

### SportsGames: Why Backend?
> SportsGames is meant to be a **full stack project**. For data to be dynamically updated onto the frontend in realtime, a backend framework is necessary. 
> Our group chose to use Flask as our backend framework due to its ease of access and comfortable use in all varieties of projects. 


### Framework Organization

**/api**: This is used for the API files. The files in here are in a Python format and are used to create API blueprints to be built in the main.py file.

**/instance**: This is where the DB file is located, in the **/volumes** subfolder. The DB file contains SQLite Data for generated tables, specifically for the NBA statistics feature of the SportsGames project. This is where all of the player statistics are included.

**/model**: This is where all the model Python files are stored. This includes all of the setters and getters for the data properties and defines the functions which update the data to the SQLite DB file.

**/quotedata**: This is specialized for one of the five pages. This contains the JSON-formatted data for the quotes and the Python file primarily utilizing Pandas for sorting purposes.

**/static**: This does not do much. This is for animations on the backend framework. Disregard unless backend visual personalization is necessary.

**/templates**: Again, this does not serve much of a purpose other than backend visual personalization. Disregard.


### Root Directory Solitary Files

**init.py**: This initializes the DB file (SQLite) and sets its default location when data is updated in the DB.

**docker-compose.yml**: This is an incredibly important part of the deployment process. This opens a unique port for the backend and allows for the frontend framework to actively fetch data from the deployed Flask backend site.

**main.py**: This is a CRUCIAL PART of the backend framework. This imports the initialized functions which allow for the database to be built. Furthermore, this is very important for **testing purposes**. When the framework is not deployed, running "python3 main.py" in the root directory allows for the Flask server to be run locally on your machine.

**requirements.txt**: This specifies the versions of the necessary Flask packages. This may need to be updated from time to time based on Flask functionality. Stay alert for changes.

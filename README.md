# ya-tube-3

## Creating a repository
1. Create a repository for yourself, using this template.
  Press the "Use this template" button and select the "Create a new repository" option.
  ![image](https://user-images.githubusercontent.com/14962819/235599080-2819c72b-3161-48fe-926d-91c289941c20.png)
  
2. Fill in the **Repository name** and **Description** fields and click the "Create repository from template" button.
  ![image](https://github.com/tripleten-com/Wordicum-3/assets/120686503/029f2e5a-2718-4d34-90ed-e673c218e7ec)

## How to work with the repository
To start the task, you need to copy the URL of your repository and clone it. (Please note that you are cloning your own repository, not the original template!)
  ![image](https://user-images.githubusercontent.com/14962819/235600053-de6be309-56d5-4c5f-adc3-d466887962f6.png)
  
### Create a virtual environment

1. Launch the Visual Studio Code editor, and through the "*File" / "Open Directory"* menu, open the *Dev/wordicum-3/* folder.
2. Launch the terminal in VS Code and make sure you work from the *wordicum-3/* directory. If you use Windows, make sure Git Bash runs in the terminal, and not through anything else, like PowerShell. Run this command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
The virtual environment will be deployed in the *wordicum-3/* directory. The `venv` folder will appear there too and will store all the project dependencies. The file structure will look like this:

```
Dev/
 └── ya-tube-3/
     ├── tests/             TripleTen tests for the project
     ├── venv/              Virtual environment directory
     ├── ya-tube-3/         <-- Project directory
     |   ├── ...            <-- Django project structure
     |   └── manage.py      
     ├── .gitignore         List of files and folders hidden from Git tracking
     ├── db.json            <-- Fixtures for the database 
     ├── LICENSE            License   
     ├── pytest.ini         TripleTen tests configuration
     ├── README.md          Project description
     └── requirements.txt   Project dependency list
```

### Activation of the virtual environment
In the terminal, navigate to the root directory of the *Dev/wordicum-3/* project and execute this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Now all commands in the terminal will be preceded by the `(venv)` string.

💡 All further commands in the terminal should be executed with the virtual environment activated.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

###  Install the dependencies from the *requirements.txt* file
While in the *Dev/wordicum-3/* folder, execute this command:

```bash
pip install -r requirements.txt
```

#### End of support for dependencies

The LTS versions of dependencies have been chosen.
For Django, version 3.2 was selected. Its extended support
[ends](https://endoflife.date/django) on April 1, 2024.

### Using migrations

    
In the directory with the "manage.py" file, run this command:

```bash
python manage.py migrate
```

### Running the project in dev mode

    
In the directory with the "manage.py" file, run this command:

```bash
python manage.py runserver
```

In response, Django will report that the server is running and the project is available at the address [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


### Local test launch
Having finished the task, launch the local tests. In the terminal, navigate to the root directory of the *Dev/wordicum-3/* project and execute this command:
```shell
pytest
```
If all the test cases are successful, the project will be considered completed. Otherwise, you will have to fix the parts that haven't passed the tests and launch them once again.

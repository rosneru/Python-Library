# Web scraping examples
## About

This directory is the place for experiments with web scrapers.

## Install dependencies

### Set up a Virtual Environment
Open a cmd in your Windows user directory.

Create the directory .virtualenvs and enter it.

Now create the virtual envrionment:

    virtualenv scraping_env


### Activate the virtual environment
Now each time you want to use the environment call
    
    c:\Users\uwero\.virtualenvs\scraping_env\Scripts\activate.bat

Where *uwero* has to be replaced by your Windows login.


#### Deactivate the virtual environment
Just type in the python bash which prompts the current virtual environment:

    Deactivate

### Activate the environment in VSCode

The new Python environment has to be set up in VSCode.

So in VSCode, open the Command Palette (Ctrl+Shift+P).

Type: *Select Python Interpreter*

In the combobox you see all Python interpreters, also the ones in the
virtual environments. Select the newly created one.

### Install package Beautiful soap

    pip3 install beautifulsoup4

Additionally you might want to install some html parsers

    pip3 install lxml
    pip3 install html5lib


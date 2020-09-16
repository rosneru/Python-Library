# Websockets tutorial

## Setup a virtualenv with PEP8

[Source](https://dev.to/j0nimost/setting-up-pep8-and-pylint-on-vs-code-34h)

PEP8 defines Python coding standards; from variable declaration to
formatting of classes. (...) this allows you to nicely format your
python code.

To install the package ensure you are in your project folder and
virtualenv is enabled, if not run the following lines in your folder
directory

    $ virtualenv ~/.virtualenvs/env
    $ source ~/.virtualenvs/env/bin/activate

Then install PEP8

    $ pip install pep8

Now let's checkout Pylint, this tool checks whether we follow PEP8
standards and returns errors where we fail to follow. Furthermore, this
tool also does error checking due to syntax errors. To install pylint
run the following code;

    $ pip install pylint

Since we now have the two needed tools we can now open vs code

    $ code .

Once we open our vs code editor; we can select our preferred
interpreter, just press *Ctrl + Shift + P*

Now just select your Python/Virtual env.

Next we finally activate linting on Vs code. Follow the following steps:

1. File > Preferences > Settings > Workspace Settings > Python Configuration
2. Click *Edit in settings.json*



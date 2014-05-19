Sprout Project
===============

For Mac/Linux:
--------------

1. cd into sprout-backend
2. create a virtualenv for the project from PyCharm > Preferences > Project Interpreter > Python Interpreters.
3. activate your new virtualenv in the PyCharm terminal
4. run terminal command `sudo pip install -r requirements/dev.txt`
	-- enter your password for the computer
5. create a Django run configuration in PyCharm
6. cd into sprout-frontend
7. run terminal command `npm install`
8. run terminal command `bower install`
	-- if your terminal complains about bower not being installed, run `npm install -g bower` and then run `bower install`
9. create a Node.js run configuration in PyCharm



For Windows:
------------

**You must be using git-bash for the following setup.**

1. cd into sprout-backend
2. create a virtualenv for the project from PyCharm > Preferences > Project Interpreter > Python Interpreters.
3. activate your new virtualenv in the git-bash terminal.
	-- to do this, note the path that your new virtualenv was created in and source the activate script. It will be something like `source C:/Users/*your_username*/.virtualenvs/sprout/Scripts/activate`
4. run terminal command `pip install -r requirements/dev.txt`
5. create a Django run configuration in PyCharm
6. cd into sprout-frontend
7. run terminal command `npm install`
	-- npm install may complain after it's done doing its thing on Windows. Ignoring it is fine because step 8 will make sure that it will complete the install.
8. run terminal command `bower install`
	-- if your terminal complains about bower not being installed, run `npm install -g bower` and then run `bower install`
9. create a Node.js run configuration in PyCharm


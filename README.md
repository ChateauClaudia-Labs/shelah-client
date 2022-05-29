# shelah-client

Client-side program to interact with a Shelah server.

# File structure

This GIT repository is broken into multiple Python projects, each with a dedicated Python build configuration (a `setup.cfg` file).

Python projects appear as folders right below the folder for this repo. They include:

* `shelah-cli`: A CLI application that connects to a Shelah server to invoke its capabilities.


# Creating a development environment

It is suggested that a Conda virtual environment be created, and then installing the `shelah-client` programs.
For example, in the root folder for the `shelah-client` repo, run a command like

`conda create -n shelah-client-env`

to create the virtual environment `shelah-client-env`.

Then do 

`conda activate shelah-client-env`

to activate the new virtual environment, and to do a number of local installations:

`conda install pip` so that pip is local to the environment. That way development installs will be local to the environment.

 The for the applications of interest, do a (development) install. For example, for the `shelah_cli` Python application, do

`pip install -e shelah_cli[test]`. This in turn will bring any dependencies that the application has, including test dependencies to the environment.

# Running tests

Tests are run using pytest.

If you have a development environment that was built as per above, then your test dependencies are already in place,
and you can run the tests from the root folder for the repo by doing 

`pytest test`

If you are not in a development environment, then you need to make sure that paths are configured right so that
pytest finds the applications  (i.e., top Python modules) for this repo (such as `shelah_cli`).

# Running DevOps pipelines

You must have an installation of `ccl-chassis` with its `devops/bin` folder in the path.
# suapon


## Description
Academic institutions listing website


## Set up
This guide assumes you have a python environment already set up.
It is recommended you set up a virtual environment.
This guide uses virtualenv. To install: `python -m pip install --user virtualenv`

The user guide can be found here: [`https://virtualenv.pypa.io/en/latest/user_guide.html`]()

Create a new postgresql database

## Run

1. Copy `env_sample` to `.env`. Update any of the values if required
2. On a new terminal, cd into the project folder `cd suapon`
3. run `python manage.py migrate`
4. Run `python manage.py createsuperuser`. Provide the required information to have an admin user created
5. Open the app on [`http://localhost:8000/admin`]() (provided the port was not changed in **step 1**. Use the credentials in **step 4** to log in


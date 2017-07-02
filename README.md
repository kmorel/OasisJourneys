## Instalation

To create the SQLite database file that will serve the underlying data, run

  $ python manage.py migrate

You may want to create an admin account to manage the data through the web.
If so, run

  $ python manage.py createsuperuser


## Development

To run a test development server, execute this in the top directory.

  $ python manage.py runserver

If making a change to the database configuration (i.e. the schema), run

  $ python manage.py makemigrations OasisMembers

After that you can call the migrate command (given in the installation)
which is

  $ python manage.py migrate

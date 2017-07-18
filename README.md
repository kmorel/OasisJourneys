## Instalation

To create the SQLite database file that will serve the underlying data, run

```
python manage.py migrate
```

You may want to create an admin account to manage the data through the web.
If so, run

```
python manage.py createsuperuser
```


## Development

To build a database populated with some test data, first call the migrate
command as above and then use the loaddata command to populate it with the
provided json data.

```
python manage.py migrate
python manage.py loaddata testing/testdata.json
```

If you make some changes to the data that you want to capture (and check
into the repository) use the dumpdata command.

```
python manage.py dumpdata OasisMembers --indent 2 > testing/testdata.json
```

To run a test development server, execute this in the top directory.

```
python manage.py runserver
```

If making a change to the database configuration (i.e. the schema), run

```
python manage.py makemigrations OasisMembers
```

After that you can call the migrate command (given in the installation)
which is

```
python manage.py migrate
```

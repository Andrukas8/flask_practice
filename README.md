# flask_practice
A code along project while taking Falsk course

```set FLASK_APP=market.py``` - sets python file to be the app;

```$env:FLASK_APP="market.py"``` - sets python file to be the app if command above did not work;

```$env:FLASK_DEBUG=1``` - turns on the debug mode in order to have the app in the browser update automatically and not resturt the server (need to turn it off before deployment);

```flask run``` - starts the Flask app on local machine;

```pip install flask-sqlalchemy```

Adding Items to the database in Python shell:
```>>> from market import Item```
```>>> item1 = Item(name="IPhone 10", price=500, barcode="948305726382", description="this is a description")```

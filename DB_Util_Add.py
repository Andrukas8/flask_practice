from market import app, db
from market.models import Item, User

app.app_context().push()

# i1 = Item(name="Iphone 10", price=500, barcode="672981678098", description="this is a description1")
# db.session.add(i1)

# i2 = Item(name="Laptop", price=600, barcode="672984761098", description="this is a description2")
# db.session.add(i2)

# u1 = User(username="jsc", password_hash="djiweoi3j4t3i", email_address="jsc@gmail.com")
# db.session.add(u1)

# db.session.commit()

# Assigning owner of the Iphone 10
#db.session.rollback()
item1 = Item.query.filter_by(name="Iphone 10")
item1.owner = 1 #User.query.filter_by(username="jsc").first().id

db.session.add(item1)
db.session.commit()

# run this file to add items to the database
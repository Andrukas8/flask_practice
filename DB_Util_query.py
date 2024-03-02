from market import app
from market.models import Item, User
app.app_context().push()
# Item.query.all()
# User.query.all()

# Copy and paste into >> Python shell to run

# or run this file

items = Item.query.all()
for item in items:
    print(item.id, item.name, item.barcode, item.price, item.description)

print("------------------------")

users = User.query.all()
for user in users:
    print(user.username, user.password_hash, user.items)


# filtering:
# for item in Item.query.filter_by(price=500):
#     print(item.name, item.price)
    

from market.routes import app
from market import db

app.app_context().push()
db.create_all()

# Run this script to create a database
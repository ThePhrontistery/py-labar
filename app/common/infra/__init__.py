# File: app/Common/infra/__init__.py

# Import the database session factory and the base class for models here.
# This allows other parts of your application to import these directly
# from the infra package instead of having to import them from the database module.
from .database import SessionLocal, Base, init_db

# Optionally, you can also import your models here if you want them to be accessible
# from infra. However, this could lead to circular imports if your models themselves
# import infra components, so be cautious with this.
# from .models import User, AnotherModel

# If there are any other infrastructure components you'd like to be easily accessible,
# you can import them here as well.

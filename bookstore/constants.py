import os

SECRET_KEY = os.getenv("SECRET_KEY", "4e9350f4-76c9-4c2d-9eaf-dd68ed7ac31a")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

from app import app 
from routes import routes
# config.py (or wherever you set DB path)
import os
DB_PATH = os.getenv("DB_PATH", "/var/data/agrotech.db")  # Render Disk mount


from firebase import Firebase
import os
from dotenv import load_dotenv
load_dotenv()
config = {
  "apiKey": os.environ.get("API_KEY"),
  "authDomain": os.environ.get("AUTH_DOMAIN"),
  "databaseURL": os.environ.get("DATABASE_URL"),
  "storageBucket": os.environ.get("STORAGE_BUCKET"),
  "serviceAccount": "./adminsdk.json"
}

firebase = Firebase(config)


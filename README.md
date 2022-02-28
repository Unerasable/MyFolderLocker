# MyFolderLocker

## How to use

To use this you will need to clone this repository then make a [firebase project](https://firebase.google.com) and enable Real Time Database, Auth(Make sure you enable the email option) and Storage. Make a file called `.env` and put these in it:
```
API_KEY=<your api key>
AUTH_DOMAIN=<your auth domain>
DATABASE_URL=<your database url>
STORAGE_BUCKET=<your storage bucket>
```
After that, get the service account from your **project settings** and then run the file and you'll be able to create an account, and then you will be able to lock your folders using that!
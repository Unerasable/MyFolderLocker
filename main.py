from firebase import Firebase
from firebase_init import firebase
import os
import requests
import shutil

storage = firebase.storage()
auth = firebase.auth()
db=firebase.database()

accexists = input("Do you have an account? (y/n)")
if accexists == "y":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    #authenticate the user
    user = auth.sign_in_with_email_and_password(f"{email}", f"{password}")
elif accexists == "n":
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    #create a new user
    user = auth.create_user_with_email_and_password(f"{email}", f"{password}")
else:
    print("Error")
#get the user's id
token=auth.current_user['localId']
while True:
    try:
        print("""Choose one option:
        1. Upload a file
        2. Download a file
        3. Quit
        """)
        upldnl = input()
        if upldnl == "1":
            folder = input("Path of the folder you want to lock: ")
            name = input("What would you like to name this folder: ")
            file_names=''
            for files in os.listdir(folder):
                storage.child(f"{token}/{name}/{files}").put(f"{folder}/{files}")
                file_names+=f"{files},"
                print(f"{files} uploaded!")
            data = {
                    "files": f"{file_names}",
                    "fileloc": f"{folder}"
            }
            db.child(f"{token}").child(f"{name}").set(data)
            print("Would you like to delete this folder? (y/n)")
            del_folder = input()
            if del_folder == "y":
                shutil.rmtree(folder)
                print("Folder deleted!")
            elif del_folder == "n":
                print("Folder not deleted!")
            else:
                print("Please choose a valid option!")
        elif upldnl == "2":
            name = input("What is the name of the folder you want to download: ")
            filenames = db.child(f"{token}").child(name).child("files").get()
            filenames = str(filenames.val()).split(",")
            fileloc = db.child(f"{token}").child(name).child("fileloc").get()
            os.mkdir(fileloc.val())
            for files in filenames:
                if files == None or files == "" or files == " ":
                    print("f")
                else:
                    url = storage.child(f"{token}/{name}/{files}").get_url(None)
                    r = requests.get(url) 
                    with open(f"{fileloc.val()}/{files}",'wb') as f:
                        f.write(r.content)
            print(f"{name} downloaded!")
        elif upldnl == "3":
            quit()
        else:
            print("Invalid option")
    except KeyboardInterrupt:
        print("Exiting...")
        quit()
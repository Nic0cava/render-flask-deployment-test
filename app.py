
#! HOW TO DEPLOY A FLASK APP STEP-BY-STEP

#! STEP 1:
# Your installs
# pip install Flask
# pip install gunicorn #! --> the package needed to run the app on render

#! STEP 2:
# You will need to make a requirements.txt for all your installs
# pip freeze > requirements.txt #! --> creates the requirements.txt file with all currently installed packages

#! STEP 3:
# Create a git repository on GitHub

#! STEP 4:
# create a .gitignore file, specify files you want git to ignore, such as the venv folder

#! STEP 5:
# Upload files to GitHub
# git init
# git add .
# git commit -m "commit message"
# git branch -M main
# git remote add origin <github_repository_url>
# git push -u origin main

#! STEP 6:
# Go to render.com and sign in
# Go to Web Service
# Connect your git repository from GitHub to Render
# Follow the steps of deployment

from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return "<h1>Nico's Flask App</h1>"

if __name__=="__main__":
    app.run()

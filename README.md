# Reflex Training
>This is a repo to train myself on using the Reflex library, Version Control through Git and Github

## Features
Once the project is finished #Todo 

## Installation 
This project is done on Windows 10 through the WSL environments 

```shell
#--------- STEP 1: initiate .venv, .git, .gitignore 
python3.12 -m venv .venv 
source .venv/bin/activate        # activate (venv)

git init 
touch .gitignore                 # Add the files to be ignored inside 

#--------- STEP 2: Install reflex 
pip install reflex 

#--------- STEP 3: Create requirements.txt & a README.md
pip freeze > requirements.txt 
touch README.md

#--------- STEP 3: Initiate reflex 
reflex init 

>> Which template would you like to use? (0): 
>> 0 # BLANK TEMPLATE 


#--------- STEP 4: Initial commit in the main local repo 
git add .                       # Add all the files to the staging area 

git commit -m "Initial commit: blank reflex project"

 
#--------- STEP 5: Link the project to a remote repo on github 
git remote add origin <SSH_url>
git remote -vv 

#--------- STEP 6: Push the inital commit to the main repo & set the upstream
git push --set-upstream origin main

git status                            # Check the working directory and staging area status
git branch -vv                        # Show local branches and their tracking branches
```
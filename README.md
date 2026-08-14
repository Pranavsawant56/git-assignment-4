Flask To-Do App — Git Assignment 4

Simple Flask + MongoDB To-Do app for practicing Git branching, merging, reset, and rebase.

Repo: https://github.com/Pranavsawant56/git-assignment-4

Setup
bash
git clone git@github.com:Pranavsawant56/git-assignment-4.git
cd git-assignment-4
pip install -r requirements.txt

Add a .env file with MONGO_URI=your_connection_string, then run:

bash
python app.py
API
Method	Route	Description
GET	/	Loads To-Do form
POST	/submittodoitem	Saves item to MongoDB (needs itemName, itemDescription)
Git Workflow Practiced
Feature branch → merge to main
Branch with JSON update → conflict resolved
Two parallel branches (frontend + backend) → merged
3 sequential commits (ID, UUID, Hash)
git reset --soft + git rebase
Security

.env is git-ignored. Debug mode off. Input validation on API.

Author

Pranav Sawant
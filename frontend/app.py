from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
import json

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
collection = db["mycollection"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.todo('/todo')
def todo():
    return render_template('to-do.html')


@app.route('/api', methods=['POST'])
def api():
    try:
        form_data = dict(request.form)

        # Read existing data
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        # Add new form data
        data.append(form_data)

        # Save updated data
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return "✅ Data submitted successfully!"

    except Exception as e:
        return f"❌ Error: {e}"
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        form_data =dict(request.form)
        collection.insert_one(form_data)
        return:"Todo submited successfully "
    except Exception as e :
        return f" Error:{e}"
   


if __name__ == '__main__':
    app.run(debug=True) 
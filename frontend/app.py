from flask import Flask ,render_template,request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["mycollection"]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('to-do.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)
        return "✅ Data submitted successfully!"

    except Exception as e:
        return f"❌ Error: {e}"


if __name__ == '__main__':
    app.run(debug =True)    
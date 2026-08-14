from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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


if __name__ == '__main__':
    app.run(debug=True) 
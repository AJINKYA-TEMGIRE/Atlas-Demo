from flask import Flask, render_template, request
from pymongo import MongoClient
import urllib.parse

# Properly escape the username and password
username = "Ajinkya"
password = "Ajinkya@0835"
escaped_username = urllib.parse.quote_plus(username)
escaped_password = urllib.parse.quote_plus(password)

# MongoDB URI with properly escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.ohwbqre.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    # Connect to MongoDB
    client = MongoClient(uri)

    # Access database and collection
    database = client["Sakshi-Database"]
    collection = database["Contact"]

    # Get form data
    username = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Create document to insert
    document = {
        "User Name": username,
        "Email": email,
        "Phone": phone,
        "Message": message
    }

    # Insert document into collection
    collection.insert_one(document)

    # Close connection to MongoDB
    client.close()

    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000 , debug = True)

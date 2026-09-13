from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", title="My Home Page")


@app.route("/items")
def items():
    my_items = [
        {
            "name": "Joe's Pizza",
            "address": "123 Main St, New York, NY",
            "phone": "+1 (555) 111-2222",
            "rating": 4.5
        },
        {
            "name": "Sakura Sushi",
            "address": "456 Oak Ave, Los Angeles, CA",
            "phone": "+1 (555) 333-4444",
            "rating": 4.8
        },
        {
            "name": "Le Petit Café",
            "address": "789 Elm Blvd, Chicago, IL",
            "phone": "+1 (555) 555-6666",
            "rating": 4.2
        }
    ]
    
    return render_template("items.html", items=my_items)

if __name__ == "__main__":
    app.run(debug=True)
    
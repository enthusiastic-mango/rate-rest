from flask import Flask, render_template, abort

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

@app.route("/item/<int:item_id>")
def item_detail(item_id):
    my_items = [
        {"name": "Joe's Pizza", "address": "123 Main St, New York, NY", "phone": "+1 (555) 111-2222", "rating": 4.5},
        {"name": "Sakura Sushi", "address": "456 Oak Ave, Los Angeles, CA", "phone": "+1 (555) 333-4444", "rating": 4.8},
        {"name": "Le Petit Café", "address": "789 Elm Blvd, Chicago, IL", "phone": "+1 (555) 555-6666", "rating": 4.2}
    ]
    
    if item_id < 1 or item_id > len(my_items):
        abort(404)  # If invalid, show a 404 Error page
        
    # Python lists start at index 0, but our URLs start at 1. 
    # So we subtract 1 to get the correct item.
    selected_item = my_items[item_id - 1]
    
    # Pass ONLY the selected item to the new template
    return render_template("item-detail.html", item=selected_item)

if __name__ == "__main__":
    app.run(debug=True)
    
from flask import Flask, render_template, abort

class WebManager:
    def __init__(self):
        self._app = Flask(__name__)
        
        self.my_items = [
            {"name": "Joe's Pizza", "address": "123 Main St", "phone": "111", "rating": 4.5},
            {"name": "Sakura Sushi", "address": "456 Oak Ave", "phone": "333", "rating": 4.8},
            {"name": "Le Petit Café", "address": "789 Elm Blvd", "phone": "555", "rating": 4.2}
        ]
        
        self._setup_routes()

    def _setup_routes(self)->None:
        self._app.add_url_rule("/", view_func=self._home)
        self._app.add_url_rule("/home", view_func=self._home)
        self._app.add_url_rule("/items", view_func=self._items)
        self._app.add_url_rule("/item/<int:item_id>", view_func=self._item_detail)


    def _home(self):
        return render_template("home.html", title="My Home Page")

    def _items(self):
        return render_template("items.html", items=self.my_items)

    def _item_detail(self, item_id):
        if item_id < 1 or item_id > len(self.my_items):
            abort(404)
            
        selected_item = self.my_items[item_id - 1]
        return render_template("item-detail.html", item=selected_item)

    def run(self):
        self._app.run(debug=True)

if __name__ == "__main__":
    web_app = WebManager()
    web_app.run()
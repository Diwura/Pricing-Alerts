from models.item  import Item

url = "https://www.johnlewis.com/apple-iphone-11-ios-6-1-inch-4g-lte-sim-free-64gb/p4519032"
tag_name = "p"
query = {"class":"price price--large"}

ipad = Item(url, tag_name, query)
ipad.save_to_mongo()

items_loaded =Item.all()
print(items_loaded)
print(items_loaded[0].load_price())

'''
from flask import Flask
from learning import learning_blueprint

app = Flask(__name__)
app.register_blueprint(learning_blueprint)


if __name__ == '__main__':
    app.run()

'''
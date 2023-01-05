from flask import Flask, request 

app = Flask(__name__) #creating the app and other many things including being able to run the app 

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():  #when we access this adress we re then goign to run this fuction or Flask is going to run this function 
    return {"stores": stores} #and is going to return this data

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []} #creating the dictionary that represents our new store (the name is comming from json)
    stores.append(new_store)   #adding our store to our list
    return new_store, 201   #if our return is None we get an error. And because we created this store, we want to create a status code 
                            #200 means "okay"; 201 means "okay i've accepted the date here and i'm gonna create the store.

@app.post("/store/<string:name>/item") #we're going to use that with a POST request to create an item
def create_item(name):
    request_data = request.get_json()
    for store in stores: #going through the stores list
        if store["name"] == name: #and checking if the name matches the name that came in the URL, which is "My Store"
            new_item = {"name": request_data["name"], "price": request_data["price"]} #creating new item
            store["items"].append(new_item) #adding the new item
            return new_item, 201 #that is what the client will receive
    return {"message": "Store not found"}, 404 #this return statement will be reached if the store doesnt exist
    
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"messas": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import StoreModel

from schemas import StoresSchema

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoresSchema)
    def get(self, store_id):
        store = StoreModel.get_or_404(store_id)
        return store



    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted"}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoresSchema(many=True)) #it will turn everything into a list of stores
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoresSchema)
    @blp.response(200, StoresSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)  #adding the store
            db.session.commit()   #writing the data into the database
        except IntegrityError:
            abort(
                400,
                message="A store with that name alredy exists."
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        
        return store  
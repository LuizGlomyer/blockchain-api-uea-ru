from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import AccessSchema
from blockchain.main import Connection

from utils.utils import receipt_deserializer
from utils.logger import Logger, UserInteractions

blp = Blueprint("View", "view", description="Visualizing system data")
blockchain = Connection()
logger = Logger("view")


@blp.route("/view/data/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_DATA)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/view/ticket-list/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_TICKET_LIST)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    

@blp.route("/view/ticket-history/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_TICKET_HISTORY)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
    
  
@blp.route("/view/food-menu/")
class View(MethodView):
    @blp.arguments(AccessSchema)
    @blp.response(200)
    def post(self, item_data):
        receipt = logger.log(item_data, UserInteractions.VIEW_FOOD_MENU)
        deserialized_receipt = receipt_deserializer(receipt)
        
        return {"sentData": item_data, "receipt": deserialized_receipt, "status": deserialized_receipt["status"]}
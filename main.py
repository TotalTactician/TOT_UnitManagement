from flask import Flask, g , request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId 

def create_app():
    app = Flask(__name__)

    client = MongoClient()
    db = client.get_database('TOT-units')
    app.db = db.get_collection('units')

    @app.route("/api/units/<faction>")
    def getAllUnits(faction):
        unitsResult = list(app.db.find({"faction": faction}))
        if unitsResult == None:
            return "You done fucked up"
        for unit in unitsResult:
            unit['_id'] = str(unit['_id'])
        return jsonify(unitsResult)

    @app.route("/api/unit/<id>")
    def getUnit(id):
        try:
            print(id)
            objId = ObjectId(id)
            print (objId)
            unit = app.db.find_one({"_id": objId})
            print(unit)
        except:
            return "This aint no ID fool"
        
        if unit == None:
            return "You done fucked up"
        unit['_id'] = str(unit['_id'])
        return jsonify(unit)

    return app
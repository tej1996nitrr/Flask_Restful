from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import  JWT,jwt_required
from security import authenticate,identity

app=Flask(__name__)
app.secret_key = 'flask'
api =Api(app)

#jwt = JWT(app,authenticate,identity)
items=[]
#no need to jsonify, flask restful does it. so we pass dict only
class Item(Resource):
    #@jwt_required()
    def get(self,name):
        item=next(filter(lambda x:x['name']==name,items),None)
        #next gives first item matched by the filter
        #if no item found retrn None



        # for i in items:
        #     if i['name']==name:
        #         return i

        return {'item':item},200 if item else 404  # 404 for not found

    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None):

            return {'message':"An item already exist '{}'".format(name)},400 #bad request
        data=request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item ,201    #201 is code for created

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item,'/item/<string:name>')













if __name__=="__main__":
    app.run(debug=True)

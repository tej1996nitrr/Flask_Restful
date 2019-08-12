from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api =Api(app)

items=[]
#no need to jsonify, flask restful does it. so we pass dict only
class Item(Resource):
    def get(self,name):
        item=next(filter(lambda x:x['name']==name,items),None)
        #next gives first item matched by the filter
        #if no item found retrn None



        # for i in items:
        #     if i['name']==name:
        #         return i
        return {'item':item},200 if item else 404  # 404 for not fond

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

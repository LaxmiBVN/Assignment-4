# -*- coding: utf-8 -*- 
from flask import Flask
from flask_restful import Resource, Api
from flask import request,Response
import json
import urllib
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Calc(Resource):
    def get(self,op1,op2,op):
          
        if op == '+':
            return {"answer" : op1 + op2}

        elif op == '-':
            return {"answer" : op1 - op2}

        elif op == '*':
            return {"answer" : op1 * op2}

        elif op == '%':
            return {"answer" : "Some"}
        else:
            return {""}
            
class apiRSDL(Resource):
    def get(self):
        rsdl = request.args.get('rsdl')
        if(rsdl == ""):
            
            y = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><rsdl><description>A simple calculator which performs addition, subtraction, multiplication and division operations. Each of these operations will accept, as input, integers representing the operands and a string representing the operator. For every operation, the parameters op1 and op2, representing the numbers for which the arithmetic operation is performed and op representing the operator to calculate the desired operation result are taken as input . The API services offered by this application are named op1, op2, and op, and will be accessible at /api/op1, /api/op2, and /api/op. Each of them takes the above values as GET parameters only, and will yield a JSON-formatted dictionary result containing a decimal field: answer. This field contains the result of the requested arithmetic operation. Along with this, there is an external web service integrated into the current service. The service is USD to Euro currency converter which gives the live rate of USD in terms of Euro. This value is processed to give the Euro value of the USD value given by the user</description><version major="1" minor="0" build="0" revision="12" /><links><link rel="get" href="/op1/op2/op"><request><url><parameters_set><parameter type="xs:int" required="true"><name>op1</name><value>Value of the first operand</value></parameter><parameter type="xs:int" required="true"><name>op2</name><value>Value of the second operand</value></parameter><parameter type="xs:string" required="true"><name>op</name><value>Value of the operator</value></parameter></parameters_set></url></request><response><type>JSON containing result</type></response></link></links></rsdl>'
            
            
            return Response(y, mimetype='text/xml')        #print(BeautifulSoup(x, "xml").prettify())         
        return Response("404 Page not found", mimetype='text/plain') 

class Convertor(Resource):
    def get(self,amount):
        url = "http://www.apilayer.net/api/live?access_key=cb3be058415e5cc8904650fe4a1d78a1&currencies=usd,eur"
        f = urllib.urlopen(url);
        data = json.loads(f.read())
        converted = amount * data['quotes']['USDEUR']
        return {"converted" : converted}
        
api.add_resource(HelloWorld, '/')
api.add_resource(Calc,"/<int:op1>/<int:op2>/<string:op>")
api.add_resource(apiRSDL, '/api')
api.add_resource(Convertor, '/currencyConverter/<int:amount>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

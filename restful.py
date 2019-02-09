from flask import Flask, jsonify, request
app = Flask(__name__) #define app using FLask

languages = [{'name' : 'Javascript'}, {'name':'Python'}, {'name':'Ruby'}]


## GET
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [x for x in languages if x['name'] == name]
    return jsonify({'language': langs[0]})

## POST
## pass {"name":"java1"}
@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name': request.json['name']}

    languages.append(language)
    return jsonify({'languages': languages})


## PUT: update
## pass 127.0.0.1:8080/lang/java1
## JSON {"name":"Oitroioi"}
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [x for x in languages if x['name'] ==  name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language' : langs[0]})

## DELETE
## pass 127.0.0.1:8080/lang/Javascript
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    langs = [ x for x in languages if x['name'] == name ]
    languages.remove(langs[0])
    return jsonify({'languages' : languages })

if __name__ == '__main__':
    app.run(debug=True,port=8080)
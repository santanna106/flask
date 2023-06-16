from flask import Flask,request,jsonify
import os
from joblib import load

app = Flask(__name__)

@app.route('/')
def index():
    if 'query' not in request.args:
        return jsonify({"prediction":None,"message":"sendme a text"})

    query = request.args.get("query")
    model = load("model.joblib")
    labels = ['Linguagens e Frameworks','Plataformas','Ferramentas']

    predict = model.predict([query])
    prediction = labels[predict[0]]

    return jsonify({"prediction":prediction})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

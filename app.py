from flask import Flask,request,jsonify
from flask_restful import Resource, Api
import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

api = Api(app)


class HrKPI(Resource):
 
    def post(self):
        data=request.json
        nilai={'no_of_trainings': [data['no_of_trainings']], 'previous_year_rating': [data['previous_year_rating']],'length_of_service': [data['length_of_service']],'awards_won?':[data['awards_won?']],'avg_training_score':[data['avg_training_score']],'is_promoted':[data['is_promoted']]}
        print(nilai)
        list = []
        hasil = pd.DataFrame(nilai)
        prediction =model.predict(hasil)
        output = prediction[0]
        #from numpy to string
        hasilOutput=str(output)
        list.append({'kpi':hasilOutput})
        return jsonify(list)
     
api.add_resource(HrKPI, '/api/hrkpi')

if __name__ == '__main__':
    app.run(debug=True)
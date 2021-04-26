from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIxMDQyMDE4MzYiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMEEyQzlZIiwiaWQiOiJJQk1pZC01NTAwMEEyQzlZIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNDhmMTU3YWYtOGYzMi00MjcwLTljM2UtNDgxOTFmOTUzZTU1IiwiaWRlbnRpZmllciI6IjU1MDAwQTJDOVkiLCJnaXZlbl9uYW1lIjoiTW9oYW1lZCIsImZhbWlseV9uYW1lIjoiSGFzaGVtIiwibmFtZSI6Ik1vaGFtZWQgSGFzaGVtIiwiZW1haWwiOiJ3b3JrQGRhZGJlcmcuY29tIiwic3ViIjoid29ya0BkYWRiZXJnLmNvbSIsImF1dGhuIjp7InN1YiI6IndvcmtAZGFkYmVyZy5jb20iLCJpYW1faWQiOiJpYW0tNTUwMDBBMkM5WSIsIm5hbWUiOiJNb2hhbWVkIEhhc2hlbSIsImdpdmVuX25hbWUiOiJNb2hhbWVkIiwiZmFtaWx5X25hbWUiOiJIYXNoZW0iLCJlbWFpbCI6IndvcmtAZGFkYmVyZy5jb20ifSwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiOWE0NDhhMjk4NWRlNDY2M2FjMzYxZDFjNjVhODgzZDkiLCJmcm96ZW4iOnRydWV9LCJpYXQiOjE2MTk0Njc5MjEsImV4cCI6MTYxOTQ3MTUyMSwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9vaWRjL3Rva2VuIiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.nMM03C_evydHFWAKpTL1iZwNvFdhP0CtuNOCdKNs9_6JpfmPbowPi-sj0owKaEwhG-YoTDfldJ9DgTv3ZLdLbOa5Y20l59_qBd8t--wTja_2RfM5OBTOC9pNc3oEBCaNF36f0a8jRafs6VXZWlpzSvDBJt5v4P6Xz1LwhbbRyjpn-rZ3m0ifWXKjsNAEXpOeqr0KvMkuVtyliYt7-lPVv_VYYXcX0L-e3MP9XJiXtQNdsKLrMVYzClmHwboIV37pIueIgdCpL4GF5bWxC0nJV-bFiuMICM3f0-6DOAWIJvwPQHAlDpoChVrCrCF57WXfrVLVP0y-kmkeItzCLl9P1w"}

        if(form.bmi.data == None): 
          python_object = []
        else:
          python_object = [form.age.data, form.sex.data, float(form.bmi.data),
            form.children.data, form.smoker.data, form.region.data]
        #Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["age", "sex", "bmi",
          "children", "smoker", "region"], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d82ffe7b-55fc-4c62-a16c-0f99c063cd84/predictions?version=2020-09-01", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0][key]
        
        roundedCharge = round(bc[0][0],2)

  
        form.abc = roundedCharge # this returns the response back to the front page
        return render_template('index.html', form=form)

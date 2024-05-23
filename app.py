from flask import Flask, request, jsonify, render_template
import os
from cnnClassifier.pipeline.prediction import PredictionPipeline
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage

os.putenv('LANG','en-US.UTF-8')
os.putenv('LC_ALL','en-US.UTF-8')


app = Flask(__name__)
cors = CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)
        
        
@app.route('/' ,methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')       
        
@app.route('/train',methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")

    return "Training done successfully!"


@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)



if __name__ == '__main__':
    clApp = ClientApp()
    app.run(debug=True)

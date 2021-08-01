from flask import Flask, render_template, request
import pickle
from sklearn.ensemble import RandomForestClassifier



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
       stepcount = request.form['stepcount']
       mood = request.form['mood']
       caloriesburned = request.form['caloriesburned']
       hoursofsleep = request.form['hoursofsleep']
       weightkg = request.form['weightkg']
        

       data = [[float(stepcount),float(mood),float(caloriesburned),float(hoursofsleep),float(weightkg)]]

       rnd = pickle.load(open('random.pkl','rb'))
       prediction = rnd.predict(data)[0]
 
       if (prediction==1):
          result='Active'
       else:
          result='Inactive'
    return render_template('index2.html',output="Fitness level is  :{}".format(result) )














if __name__ == '__main__':
    app.run()
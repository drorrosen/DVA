from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    message = request.form['message']
    try:
        zipcode = int(message)
        print(zipcode)

        df = pd.read_csv("zipcode_data_with_labels.csv")

        my_prediction = df.loc[df['zipcodes'] == zipcode, 'avg_hier_labels']

        if len(my_prediction) == 0:
            my_prediction = "None"
        else:
            my_prediction = my_prediction.values[0]


        return render_template('result.html', prediction=my_prediction)

    except ValueError:
        my_prediction = "Text"
        return render_template('result.html', prediction=my_prediction)



if __name__ == '__main__':
    app.run(port=5000)

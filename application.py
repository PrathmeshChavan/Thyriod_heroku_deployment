from flask import Flask , render_template , request
import pickle
import numpy as np

application = Flask(__name__)
model=pickle.load(open("model.pkl" , 'rb'))

@application.route('/')
def index():
    return render_template("index.html")


@application.route('/predict', methods=["GET" , "POST"])
def predict():
    TT4 = float(request.form['TT4'])
    FTI = float(request.form['FTI'])
    sex = float(request.form['sex'])
    on_thyroxine = float(request.form['on_thyroxine'])
    T3 = float(request.form['T3'])
    query_hyperthyroid = float(request.form['query_hyperthyroid'])
    psych = float(request.form['psych'])
    sick = float(request.form['sick'])
    tumor = float(request.form['tumor'])
    pregnant = float(request.form['pregnant'])
            
    pred_agrs = [TT4,FTI,sex,on_thyroxine,T3,query_hyperthyroid,psych,sick,tumor,pregnant]
                        
            
    pred_agrs_arr = np.array(pred_agrs)
    pred_agrs_arr = pred_agrs_arr.reshape(1 , -1)
            
    model_pred = model.predict(pred_agrs_arr)
    model_pred = round(float(model_pred))
    return render_template('predict.html' , prediction = model_pred)


if __name__ == "__main__":  
    application.run(debug=True)








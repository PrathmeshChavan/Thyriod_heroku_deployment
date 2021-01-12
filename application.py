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
    #-----------------T4------------------------
    TT4 = float(request.form['TT4'])
    #-----------------FTI------------------------
    FTI = float(request.form['FTI'])
    #-----------------SEX------------------------
    sex = (request.form['sex'])
    if(sex=="Male"):
        sex=0
    else:
        sex=1
    #-----------------on_thyroxine------------------------
    on_thyroxine = (request.form['on_thyroxine'])
    if(on_thyroxine=="Yes"):
        on_thyroxine=1
    else:
        on_thyroxine=0
     #-----------------T3------------------------       
    T3 = float(request.form['T3'])
   #-----------------query_hyperthyroid------------------------
    query_hyperthyroid = (request.form['query_hyperthyroid'])
    if(query_hyperthyroid=="Yes"):
        query_hyperthyroid=1
    else:
        query_hyperthyroid=0
    #-----------------psych------------------------           
    psych = (request.form['psych'])
    if(psych=="Yes"):
        psych=1
    else:
        psych=0
    #-----------------sick----------------------------        
    sick = (request.form['sick'])
    if(sick=="Yes"):
        sick=1
    else:
        sick=0
    #-----------------tumor--------------------------
    tumor = (request.form['tumor'])
    if(tumor=="Yes"):
        tumor=1
    else:
        tumor=0
    #-----------------pregnant--------------------------       
    pregnant = (request.form['pregnant'])
    if(pregnant=="Yes"):
        pregnant=1
    else:
        pregnant=0
            
    pred_agrs = [TT4,FTI,sex,on_thyroxine,T3,query_hyperthyroid,psych,sick,tumor,pregnant]
                        
            
    pred_agrs_arr = np.array(pred_agrs)
    pred_agrs_arr = pred_agrs_arr.reshape(1 , -1)
            
    model_pred = model.predict(pred_agrs_arr)
    model_pred = round(float(model_pred))
    
    if model_pred == 0:
        return render_template('predict.html' , prediction = "You Dont Have A Thyriod")
    else:
        return render_template('predict.html' , prediction = "You Have A Thyriod")

if __name__ == "__main__":  
    application.run(debug=True)








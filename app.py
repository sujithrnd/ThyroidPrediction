from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,Predictionpipeline



app=Flask(__name__)


#http://127.0.0.1:5000/ browser udocker imagesrl

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        #val=request.form.get('hours-per-week')
        #print('#####@@@@###hours-per-week::::',val)
        
        data=CustomData(
           
            age=int(request.form.get('age')),
            TSH = float(request.form.get('TSH')), 
            T3 = float(request.form.get('T3')),
            TT4 = float(request.form.get('TT4')),
            T4U = float(request.form.get('T4U')),
            sex = request.form.get('sex'),
            on_thyroxine = request.form.get('on_thyroxine'),
            query_on_thyroxine = request.form.get('query_on_thyroxine'),
            on_antithyroid_medication= request.form.get('on_antithyroid_medication'),
            sick = request.form.get('sick'),
            pregnant =(request.form.get('pregnant')),
            thyroid_surgery =(request.form.get('thyroid_surgery')),
            I131_treatment =request.form.get('I131_treatment'),
            query_hypothyroid =request.form.get('query_hypothyroid'),
            query_hyperthyroid =request.form.get('query_hyperthyroid'),
            
            lithium =request.form.get('lithium'),
            goitre =request.form.get('goitre'),
            tumor =request.form.get('tumor'),
            hypopituitary =request.form.get('hypopituitary'),
            psych =request.form.get('psych'),
            TSH_measured =request.form.get('TSH_measured'),
            T3_measured =request.form.get('T3_measured'),
            TT4_measured =request.form.get('TT4_measured'),
            T4U_measured =request.form.get('T4U_measured')
                          

        )
        print(request.form.get('age'))
        print(request.form.get('TSH'))
        print(request.form.get('T3'))
        print(request.form.get('TT4'))
        print(request.form.get('T4U'))
        print(request.form.get('sex'))
        print(request.form.get('on_thyroxine'))
        print(request.form.get('query_on_thyroxine'))
        print(request.form.get('on_antithyroid_medication'))
        print(request.form.get('sick'))
        print(request.form.get('pregnant'))
        print(request.form.get('thyroid_surgery'))
        print(request.form.get('I131_treatment'))
        print(request.form.get('query_hypothyroid'))
        print(request.form.get('query_hyperthyroid'))
                
        print(request.form.get('lithium'))
        print(request.form.get('goitre'))
        print(request.form.get('tumor'))
        print(request.form.get('hypopituitary'))
        print(request.form.get('psych'))
        print('TSH_measured:::',request.form.get('TSH_measured'))
        print(request.form.get('T3_measured'))
        print(request.form.get('TT4_measured'))
        print(request.form.get('T4U_measured'))                    

      
        
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=Predictionpipeline()
        print('To predict method --',final_new_data.head())
        pred=predict_pipeline.predict(final_new_data)
        print('PREDICTion ',pred[0])
        results=round(pred[0],2)
        print('type of results ->',results)
        thyro_status='Positive'
        if results==0.0:
            thyro_status='Negative'



        #return render_template('result.html',final_result=results)
        return render_template('result.html',final_result=thyro_status)






if __name__=="__main__":
    app.run(host='0.0.0.0',port=9999,debug=True)


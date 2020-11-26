from flask import Flask, render_template,request,redirect,url_for,flash
app = Flask(__name__)
import pickle
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()
app.secret_key='don\'t tell anyone'
@app.route('/', methods=["GET","POST"])
def main_page():
    return render_template('index.html')
@app.route('/test', methods=["GET","POST"])
def test_page():
    if request.method == "POST":
        myDict = request.form
        while True:
            try:
                age = int(myDict['age'])
                break
            except ValueError:
                render_template('SAT.HTML')
        sex = int(myDict['sex'])
        cp = int(myDict['cp'])
        while True:
            try:
                trestbps = int(myDict['trestbps'])
                break
            except ValueError:
                render_template('SAT.HTML')
        while True:
            try:
                chol = int(myDict['chol'])
                break
            except ValueError:
                render_template('SAT.HTML')
        fbs = int(myDict['fbs'])
        restecg = int(myDict['restecg'])
        while True:
            try:
                thalach = int(myDict['thalach'])
                break
            except ValueError:
                render_template('SAT.HTML')
        exang = int(myDict['exang'])
        while True:
            try:
                oldpeak = int(myDict['oldpeak'])
                break
            except ValueError:
                render_template('SAT.HTML')
        slope = int(myDict['slope'])
        while True:
            try:
                ca = int(myDict['ca'])
                break
            except ValueError:
                render_template('SAT.HTML')
        thal=int(myDict['thal'])
        inputFeatures = [age,sex,cp,trestbps,chol, fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        infProb = clf.predict([inputFeatures])
        print(infProb)
        if infProb==[1]:
            s = "You may have problem in heart"
            return render_template('result.html',inf=s)
        elif infProb==[0]:
            s = "You don't have any problem"
            return render_template('result.html', inf=s)
    return render_template('SAT.html')
@app.route('/about', methods=["GET","POST"])
def about_page():
    return render_template('about.html')
@app.route('/helpline', methods=["GET","POST"])
def helpline_page():
    return render_template('helpline.html')


if __name__ == "__main__":
    app.run(debug = True)
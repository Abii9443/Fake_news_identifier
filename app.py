# from urllib import request

from flask import Flask, render_template,request
from sklearn.pipeline import Pipeline
import joblib
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import feature as fp
import PyPDF2
app = Flask(__name__)
loaded_model = joblib.load('news.sav')

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
@app.route("/upload",methods=["POST"])
def upload():
    if request.method == 'POST':
        file_obj = request.files['upload']
        pdfReader = PyPDF2.PdfFileReader(file_obj)

        pageObj = pdfReader.getPage(0)

        sentence = (pageObj.extractText())
        # print(sentence)
        result= fp.manual_testing(sentence)

    return render_template("sucess.html",result=result)

if __name__ == '__main__':
    app.run()

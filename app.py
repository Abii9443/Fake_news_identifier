# from urllib import request

from flask import Flask, render_template,request,make_response
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
def download_data(num):

    if num == 2:
        response = make_response(open('news_2.pdf', 'rb').read())

        return response
    # if num == 3:
    #     response = make_response(open('news_3.pdf', 'rb').read())
    #     response.headers['Content-Type'] = 'pdf'
    #     response.headers["Content-Disposition"] = "attachment; filename=data-3.pdf"
    #     return response
    # if num == '4':
    #     response = make_response(open('news_4.pdf', 'rb').read())
    #     response.headers['Content-Type'] = 'pdf'
    #     response.headers["Content-Disposition"] = "attachment; filename=data-4.pdf"
    #     return response

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
    # if request.form['news1'] == '1':
    #     download(1)
    return render_template("sucess.html", result=result)
@app.route("/download",methods=["POST"])
def download():
    if request.method == 'POST':
        data1=request.form.get('news1')
        data2=request.form.get('news2')
        data3=request.form.get('news3')
        data4=request.form.get('news4')
        if(data1=='1'):
            response = make_response(open('news_1.pdf', 'rb').read())
            response.headers['Content-Type'] = 'pdf'
            response.headers["Content-Disposition"] = "attachment; filename=data-1.pdf"
            return response
        if(data2=='2'):
            response = make_response(open('news_2.pdf', 'rb').read())
            response.headers['Content-Type'] = 'pdf'
            response.headers["Content-Disposition"] = "attachment; filename=data-2.pdf"
            return response
        if(data3=='3'):
            response = make_response(open('news_3.pdf', 'rb').read())
            response.headers['Content-Type'] = 'pdf'
            response.headers["Content-Disposition"] = "attachment; filename=data-3.pdf"
            return response
        if(data4=='4'):
            response = make_response(open('news_4.pdf', 'rb').read())
            response.headers['Content-Type'] = 'pdf'
            response.headers["Content-Disposition"] = "attachment; filename=data-4.pdf"
            return response



if __name__ == '__main__':
    app.run()

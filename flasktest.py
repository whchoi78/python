from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

#웹 서버 생성
app = Flask(__name__)
@app.route("/")
def weather():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저기온: {}</br>".format(location.select_one("tmn").string)
        output += "최고기온: {}</br>".format(location.select_one("tmx").string)
        output += "<hr/>"
    return output







'''
from flask import Flask
app = Flask(__name__)

@app.route("/") #decorator
def hello():
    return "<h1>hello oncourse</h1>"
    '''
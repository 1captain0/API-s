from flask import Flask, render_template, Markup
import http.client
import json
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET"])
def search():
    myTeam = request.args.get('teamName')
    conn = http.client.HTTPSConnection("free-football-soccer-videos.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com",
        'x-rapidapi-key': "xxxx"
    }

    conn.request("GET", "/", headers=headers)

    res = conn.getresponse()
    data = res.read().decode('utf-8')
    json_obj = json.loads(data)
    match_list = []
    embed_links = []

    for d in json_obj:
        match_list.append(d['title'])
        embed_links.append(d['embed'])

    match_data = dict(zip(match_list,embed_links))
    flag = False
    for key, value in match_data.items():
         if key.find(myTeam)!=-1:
            flag = True
            link = Markup(value)
            teams = key

    if flag:
        return link
    else:
        return "<p> Video not found</p>"


   
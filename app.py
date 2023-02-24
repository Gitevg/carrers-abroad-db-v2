from flask import Flask, render_template, jsonify 

app = Flask(__name__)

JOBS = [
 {
   'id':1,
   'title':"Data Analyst",
   'location':"New York",
   'salary':'$ 150 000'
 },
  {
   'id':2,
   'title':"Data Scientist",
   'location':"Adelaida",
   'salary':'$ 140 000'
 },
  {
   'id':3,
   'title':"Frontend Engineer",
   'location':"Remote",
   'salary':'$ 120 000'
 },
  {
   'id':4,
   'title':"Backend Engineer",
   'location':"Remote",
   'salary':'$ 140 000'
 }
  
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)


@app.route("/jobs")
  
def list_jobs():
  return jsonify(JOBS)


if  __name__ == "__main__":
    app.run('0.0.0.0',debug=True)

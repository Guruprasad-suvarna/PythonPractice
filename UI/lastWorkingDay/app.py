
import calendar
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculateYear', methods=['GET','POST'])
def calculateYear():
  if request.method == "POST":
    strYear = request.form['year']
    print(strYear)
    year = int(strYear)
    last_working_day=[]
    for i in range(1, 13):
      lastDay = calendar.monthrange(year, i)[1]
      weekday = calendar.weekday(year, i, lastDay)
      if weekday == 5:
        last_working_day.append(f"{i}/{lastDay-1}/{year}")
      elif weekday == 6:
        last_working_day.append(f"{i}/{lastDay-2}/{year}")
      else:
        last_working_day.append(f"{i}/{lastDay}/{year}")

    print(last_working_day)
    return render_template('result.html', output=last_working_day)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request,redirect, url_for
import calendar

app = Flask(__name__)

@app.route('/success/<year>')

def success(year):
  return f'The selected year {year}'

@app.route('/input', methods=['POST', 'GET'])
def input():
    if request.method == 'POST':
       inp = request.form['yr']
       return redirect(url_for('success', year = inp))
    else:
       inp= request.args.get('yr')
       return redirect(url_for('success', year = inp))
  

if __name__ == '__main__':
   app.run(debug=True)
   
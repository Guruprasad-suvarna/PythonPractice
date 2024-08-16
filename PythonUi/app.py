# from flask import Flask, render_template, request,redirect, url_for
# import calendar

# app = Flask(__name__)

# @app.route('/login', methods=['GET', 'POST'])
# def result():
#     if request.method == 'POST':
#        inp = request.form["year"]
#        return redirect(url_for('success', year = yr))
#     elif request.method == 'POST':
#        year = int(request.form['year'])
#        output = ''

#        for i in range(1, 13):
#             lastDay = calendar.monthrange(year, i)[1]
#             weekday = calendar.weekday(year, i, lastDay)
#             if weekday == 5:
#                output += f"{i}/{lastDay-1}/{year})"
#             elif weekday == 6:
#                output += f"{i}/{lastDay-2}/{year})"
#             else:
#                output += f"{i}/{lastDay}/{year})"
#     return render_template('input.html', year=year, output=output)

# if __name__ == '__main__':
#    app.run(debug=True)
   
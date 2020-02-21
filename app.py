from flask import Flask, render_template, request
import sample
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      a = int(result.get("n1"))
      b = int(result.get("n2"))
      # print(type(a),type(b))
      # print(a,b)
      sample.allot(a,b)
      return render_template("result.html",result = result)


if __name__ == '__main__':
   app.run(debug = True)
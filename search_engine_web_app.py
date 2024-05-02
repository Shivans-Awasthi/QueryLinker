

from flask import Flask, render_template, request
import search
app = Flask(__name__)

@app.route('/')
def query():
   	return render_template('query_page.html',result={})

@app.route('/searchengine',methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = search.main_search(request.form['Name'])
		return render_template("query_page.html",result=result)

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=8000, debug=True)
	
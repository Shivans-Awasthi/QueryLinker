

from flask import Flask, render_template, request
import search
app = Flask(__name__)

@app.route('/')
def query():
   	return render_template('query_page.html',result={})

@app.route('/searchengine',methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
		topic = request.form['Name']
		result = search.main_search(topic)
		return render_template("query_page.html",result=result,topic=topic)

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=8000, debug=True)
	
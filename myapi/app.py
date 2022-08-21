from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
	return "Hello from devops by Rahi"
if __name__=="__main__":
	app.run()

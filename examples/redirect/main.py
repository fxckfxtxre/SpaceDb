import spacedb
import flask
import string
import random

app = flask.Flask(__name__)
port = 2312
db = spacedb.Storage("url", ["id", "url"], encoding="json")


def create_id():
    while True:
        id = ""
        for i in range(5):
            id += random.choice(list(string.ascii_letters))

        if db.unique(id=id):
            return id

@app.route("/new")
def new():
    url = flask.request.args.get("url")
    if url:
        if db.unique(url=url):
            id = create_id()

            db.add(id=id, url=url)

            return flask.jsonify({"url": f"http://localhost:{port}/{id}"})

        else:
            data = db.search(url=url)

            if data:
                return flask.jsonify({"url": f"http://localhost:{port}/{data['id']}"})
            else:
                return flask.jsonify({"error": True}), 500
    else:
        return flask.jsonify({"error": True}), 404

@app.route("/<id>")
def go(id):
    data = db.search(id=id)

    if data:
        return flask.redirect(data["url"])
    else:
        return flask.jsonify({"error": True}), 404


if __name__ == "__main__":
    app.run(port=port)

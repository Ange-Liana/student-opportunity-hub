from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from services.jsearch import search_jobs

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("query")

    if not query:
        return render_template(
            "index.html",
            error="Please enter a job title or keyword."
        )

    results = search_jobs(query)

    return render_template(
        "index.html",
        jobs=results,
        query=query
    )


# Temporary route to inspect API response
@app.route("/api/search")
def api_search():
    query = request.args.get("query")

    if not query:
        return jsonify({
            "error": "Please provide a search query."
        }), 400

    results = search_jobs(query)

    return jsonify(results)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

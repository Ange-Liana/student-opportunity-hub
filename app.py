from flask import Flask, render_template, request, abort, session, redirect, url_for
from dotenv import load_dotenv

from services.jsearch import search_jobs

load_dotenv()

app = Flask(__name__)

app.secret_key = "student-opportunity-hub-secret-key"


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

    jobs, error = search_jobs(query)

    saved_links = [
        job["apply_link"]
        for job in session.get("saved_jobs", [])
    ]

    return render_template(
        "index.html",
        jobs=jobs,
        query=query,
        error=error,
        saved_links=saved_links
    )


@app.route("/details/<int:index>")
def details(index):

    query = request.args.get("query")

    if not query:
        abort(404)

    jobs, error = search_jobs(query)

    if error:
        return render_template(
            "index.html",
            error=error
        )

    if index >= len(jobs):
        abort(404)

    return render_template(
        "details.html",
        job=jobs[index],
        query=query
    )


@app.route("/save/<int:index>")
def save_job(index):

    query = request.args.get("query")

    jobs, error = search_jobs(query)

    if error:
        return render_template(
            "index.html",
            error=error
        )

    if index >= len(jobs):
        abort(404)

    saved = session.get("saved_jobs", [])

    job = jobs[index]

    already_saved = any(
        saved_job["apply_link"] == job["apply_link"]
        for saved_job in saved
    )

    if not already_saved:
        saved.append(job)

    session["saved_jobs"] = saved

    return redirect(
        url_for(
            "search",
            query=query
        )
    )


@app.route("/saved")
def saved_jobs():

    jobs = session.get(
        "saved_jobs",
        []
    )

    return render_template(
        "saved.html",
        jobs=jobs
    )


@app.route("/remove_saved/<int:index>")
def remove_saved_job(index):

    saved = session.get(
        "saved_jobs",
        []
    )

    if 0 <= index < len(saved):
        saved.pop(index)

    session["saved_jobs"] = saved

    return redirect(
        url_for("saved_jobs")
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
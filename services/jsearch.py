import os
import requests


API_URL = "https://jsearch.p.rapidapi.com/search-v2"


def search_jobs(query):
    headers = {
        "x-rapidapi-key": os.getenv("JSEARCH_API_KEY"),
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    params = {
        "query": query,
        "num_pages": "1",
        "country": "us",
        "date_posted": "all"
    }

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        jobs_data = data.get("data", {}).get("jobs", [])

        jobs = []

        for job in jobs_data:
            jobs.append({
                "title": job.get("job_title", "No title available"),
                "company": job.get("employer_name", "Company not specified"),
                "location": job.get("job_location", "Location not specified"),
                "description": job.get(
                    "job_description",
                    "No description available"
                ),
                "apply_link": job.get("job_apply_link", "#"),
                "remote": job.get("job_is_remote", False)
            })

        return jobs

    except requests.exceptions.Timeout:
        return {
            "error": "The job search service took too long to respond."
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }

    except ValueError:
        return {
            "error": "Invalid response received from the API."
        }

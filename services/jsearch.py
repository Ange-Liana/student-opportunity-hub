import os
import requests

API_URL = "https://jsearch.p.rapidapi.com/search-v2"


def search_jobs(query):
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        "x-rapidapi-key": os.getenv("JSEARCH_API_KEY")
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

        jobs = data.get("data", {}).get("jobs", [])

        formatted_jobs = []

        for job in jobs:
            formatted_jobs.append(
                {
                    "title": job.get("job_title", "No title"),
                    "company": job.get("employer_name", "Unknown"),
                    "location": job.get("job_location", "Not specified"),
                    "description": job.get(
                        "job_description",
                        "No description available."
                    ),
                    "apply_link": job.get("job_apply_link", "#"),
                    "logo": job.get("employer_logo", "")
                }
            )

        return formatted_jobs, None

    except requests.exceptions.Timeout:
        return [], "The Job Search API took too long to respond."

    except requests.exceptions.ConnectionError:
        return [], "Unable to connect to the Job Search API."

    except requests.exceptions.HTTPError:
        return [], "The Job Search API returned an error."

    except requests.exceptions.RequestException:
        return [], "An unexpected API error occurred."
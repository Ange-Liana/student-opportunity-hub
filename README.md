Title: Student Opportunity Hub


Demo Video: https://www.loom.com/share/5cd582a3c82f404aa62b9dc44029e7fd


 Live Deployment

Load Balancer: http://32.192.79.10



Web01: http://54.227.137.95



Web02: http://13.221.90.222

 





Student Opportunity Hub is a Flask-based web application designed to help students and recent graduates discover internships, graduate programmes, remote jobs, and professional career opportunities through a single, easy-to-use platform.



The application integrates the JSearch API through RapidAPI to retrieve real-time job listings from multiple online sources. Users can search for opportunities, view detailed job information, save interesting positions for later, and revisit their saved opportunities during the same browsing session.



Beyond application development, this project demonstrates a complete production deployment using Gunicorn, Nginx, and HAProxy across multiple Ubuntu servers, providing improved scalability, reliability, and high availability.





**Project Overview**



Finding internships and graduate opportunities often requires searching across multiple job platforms, making the process repetitive and time-consuming.



Student Opportunity Hub simplifies this process by allowing users to search thousands of publicly available job opportunities from one interface. Instead of visiting numerous websites individually, users can quickly discover relevant opportunities, compare results, and save positions they wish to revisit later.



The project combines modern web development with real-world deployment practices by integrating an external API, implementing server-side application logic, and deploying the application across two production web servers behind a load balancer.







&#x20;**Key Features**



&#x20;**Job Search**



\- Search internships, graduate programmes, remote jobs, and full-time positions.

\- Retrieve real-time job listings using the JSearch API.

\- Display company name, location, company logo, job description, and application link.

\- View complete information for each opportunity on a dedicated details page.



&#x20;User Experience



\- Save opportunities for later viewing.

\- View all saved opportunities on a dedicated page.

\- Remove saved opportunities.

\- Prevent duplicate saved entries.

\- Responsive interface suitable for desktop and mobile devices.



&#x20;Reliability



\- Graceful handling of invalid searches.

\- User-friendly API error messages.

\- Session-based storage for saved opportunities.

\- Clear separation between presentation, business logic, and API integration.



Deployment



\- Flask application served by Gunicorn.

\- Nginx configured as a reverse proxy.

\- HAProxy configured for round-robin load balancing.

\- Deployed across two Ubuntu web servers for improved availability and fault tolerance.





**Technologies Used**



&#x20;**Backend**



\- Python 3

\- Flask

\- Gunicorn



Frontend



\- HTML5

\- CSS3

\- JavaScript



Python Packages



\- Flask

\- Requests

\- python-dotenv

\- Gunicorn



Deployment



\- Ubuntu Linux

\- Nginx

\- HAProxy

\- systemd



External API



\- RapidAPI

\- JSearch API



&#x20;Version Control



\- Git

\- GitHub







&#x20;**Project Structure**



student-opportunity-hub/

│

├── app.py

├── requirements.txt

├── services/

│   └── jsearch.py

├── templates/

│   ├── index.html

│   ├── details.html

│   └── saved.html

├── static/

│   ├── style.css

│   └── script.js

├── .gitignore

├── .env

└── README.md





&#x20;**Application Workflow**





&#x20;                   User

&#x20;                     │

&#x20;                     ▼

&#x20;           Student Opportunity Hub

&#x20;                     │

&#x20;                     ▼

&#x20;               Flask Application

&#x20;                     │

&#x20;                     ▼

&#x20;         JSearch API (RapidAPI)

&#x20;                     │

&#x20;                     ▼

&#x20;           Available Job Listings

&#x20;                     │

&#x20;         ┌───────────┼────────────┐

&#x20;         │           │            │

&#x20;         ▼           ▼            ▼

&#x20;     View Details   Apply      Save Job

&#x20;                                  │

&#x20;                                  ▼

&#x20;                       Saved Opportunities





The application receives a search query from the user, sends a request to the JSearch API, processes the returned data, and displays the available opportunities. Users can then view additional information, apply through the original job source, or save opportunities for future reference during the current session.









Local Installation



Clone the repository.



bash

git clone https://github.com/Ange-Liana/student-opportunity-hub.git

cd student-opportunity-hub





Create and activate a virtual environment.



bash

python3 -m venv venv

source venv/bin/activate





Install the required dependencies.



bash

pip install -r requirements.txt



Environment Variables



Create a .env file in the project root directory and add your RapidAPI credentials.



.env

RAPIDAPI\_KEY=your\_api\_key

RAPIDAPI\_HOST=jsearch.p.rapidapi.com





The .env file is excluded from version control using `.gitignore` to ensure sensitive information is not exposed publicly.





&#x20;Running the Application



Start the Flask application.



bash

python app.py





The application will be available at: http://127.0.0.1:5000





Production Deployment



The application was deployed across two Ubuntu web servers to provide redundancy and improve availability.



&#x20;Web01



\- Cloned the project repository.

\- Installed Python dependencies.

\- Configured the environment variables.

\- Created a Gunicorn systemd service.

\- Configured Nginx as a reverse proxy.

\- Verified that the application was accessible over HTTP.



&#x20;Web02



\- Repeated the same deployment process used on Web01.

\- Confirmed that the application behaved identically to Web01.





&#x20;Gunicorn Configuration



Gunicorn was used as the WSGI application server responsible for running the Flask application.



A systemd service was created to ensure the application starts automatically whenever the server boots and restarts if it unexpectedly stops.



This provides a more reliable production environment than running the Flask development server.



&#x20;Nginx Configuration



Nginx was configured as a reverse proxy.



Its responsibilities include:



\- Receiving incoming HTTP requests.

\- Forwarding requests to Gunicorn.

\- Serving the application to users.

\- Returning an `X-Served-By` response header identifying the backend server handling each request.





&#x20;HAProxy Load Balancer



HAProxy was deployed on the load balancer server.



It was configured using the Round Robin algorithm to distribute incoming requests evenly between Web01 and Web02.



Architecture:



&#x20;                   Users

&#x20;                     │

&#x20;                     ▼

&#x20;               HAProxy Load Balancer

&#x20;                 /               \\

&#x20;                /                 \\

&#x20;               ▼                   ▼

&#x20;         Web01 Server         Web02 Server

&#x20;       Nginx + Gunicorn     Nginx + Gunicorn

&#x20;                │                   │

&#x20;                └─────────┬─────────┘

&#x20;                          ▼

&#x20;                   Flask Application

&#x20;                          │

&#x20;                          ▼

&#x20;                JSearch API (RapidAPI)





&#x20;Load Balancer Verification



The deployment was verified by:



\- Confirming both web servers served the application correctly.

\- Accessing the application through the load balancer.

\- Refreshing multiple times to verify requests alternated between Web01 and Web02 using the `X-Served-By` response header.

\- Confirming that users could access the application without knowing which backend server processed the request.





&#x20;Error Handling



The application includes error handling for several common situations.



\- Empty search queries.

\- Invalid search requests.

\- API request failures.

\- Network-related API errors.

\- No opportunities returned for a search.

\- Invalid job detail requests.

\- Prevention of duplicate saved opportunities.



Whenever possible, meaningful messages are displayed instead of exposing application errors to the user.





&#x20;API Documentation and Attribution



This project uses the JSearch API provided through RapidAPI.



Official documentation:



https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch



RapidAPI:



https://rapidapi.com/



All credit for the job listing data belongs to the JSearch API developers and RapidAPI.





&#x20;Challenges Encountered



Several challenges were encountered during development and deployment.



&#x20;Limited API Request Quota



The free RapidAPI subscription provides a limited number of requests. During development, frequent testing quickly consumed the available quota.



Solution:



\- Reduced unnecessary API requests.

\- Reused previous search results whenever possible during testing.

\- Performed deployment testing carefully to minimise API usage.



&#x20;Multi-Server Deployment



Deploying the application across two independent web servers required keeping both servers synchronised whenever changes were made.



Solution:



\- Used Git to pull updates on both servers.

\- Restarted Gunicorn after each deployment.

\- Verified functionality individually before testing through the load balancer.



&#x20;Load Balancer Configuration



Ensuring traffic was correctly distributed between both servers required careful HAProxy configuration and verification.



Solution:



\- Configured HAProxy using the Round Robin algorithm.

\- Tested multiple requests to confirm alternating responses from Web01 and Web02.





&#x20;Future Improvements



Possible future enhancements include:



\- User authentication and accounts.

\- Database integration for permanent saved opportunities.

\- Advanced filtering by country, company, salary, and job type.

\- Pagination for search results.

\- Job recommendation system.

\- Response caching to reduce API requests.

\- Docker containerisation.

\- CI/CD pipeline for automated deployment.

\- HTTPS using SSL/TLS certificates.







&#x20;API Credentials



RapidAPI credentials are intentionally excluded from this repository for security reasons.



The required API credentials should be provided separately to the project reviewer as instructed in the assignment.





&#x20;Developer: BATSINDE Ange Liana



GitHub: https://github.com/Ange-Liana



Note: This project was developed for academic purposes (my summative) 




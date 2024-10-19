

https://github.com/user-attachments/assets/002529cf-30e2-4d9a-80cd-74a435b77758


#react and django landing page
This project is a Single Page Application (SPA) built using React for the frontend and Django for the backend. It leverages API integration through Axios and session management to create a smooth user experience. The application also features a contact form with email validation through a One-Time Password (OTP) system for enhanced security.

##Features
- **Single Page Application (SPA):** Built with React, the app dynamically loads content without requiring full page refreshes.
- **Backend with Django:** The backend is powered by Django, exposing a RESTful API to handle requests from the frontend.
- **Axios Integration:** Axios is used for making API requests between the React frontend and Django backend.
- **Session Management:** User sessions are handled using Django's session framework, ensuring secure and persistent user authentication.
- **Contact Form with Email Validation:** The application includes a contact form where users must validate their email address through an OTP sent to their inbox. This ensures that only verified users can submit the form.

##Tech Stack

###Frontend
React: A JavaScript library for building user interfaces, especially SPAs.
Axios: A promise-based HTTP client used to make requests to the Django API.
###Backend
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST Framework (DRF): For building REST APIs to communicate with the React frontend.
Other Technologies
Session Management: Handled using Django's built-in session framework.
Email Validation: Implemented through the contact form using Django’s email system to send a One-Time Password (OTP) for email verification.

##Installation & Setup
####1.Clone the repository:
bash
Copy code
git clone https://github.com/fatemetayebi/react-and-django-landing-page.git
cd react-and-django-landing-page
####2.Install the required dependencies:

###Backend (Django)
bash
Copy code
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

###Frontend (React)
bash
Copy code
cd landing-page
npm install
npm start
Configure environment variables for both the frontend and backend, including API endpoints and email settings for OTP functionality.

Ensure both backend and frontend are running:

Backend: http://127.0.0.1:8000/
Frontend: http://localhost:3000
##How It Works
Frontend (React): The SPA interacts with the Django backend using Axios to make API requests. The user can navigate between pages without full page reloads.
Backend (Django): The backend API handles session management and user authentication, while also managing requests to send OTPs for email validation.
Contact Form with OTP Validation: The user fills out a contact form. When they submit their email, an OTP is sent to the given email address. The user must input the OTP to validate the email before the form is successfully submitted.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with any suggested changes or improvements.



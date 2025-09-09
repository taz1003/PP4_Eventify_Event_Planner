# Eventify Events Webapp

![Responsive Mockup](static/images/eventify-responsive.png)

[view the project repository on GitHub here](https://github.com/taz1003/PP4_Eventify_Event_Planner)

[view the deployed project here](https://eventify-event-planner-bfbfdef4c538.herokuapp.com/)

[view the project MVC framework/kanban board here](https://github.com/users/taz1003/projects/3/views/1)

## Table of Contents

- Project overview
- Agile methodology
- Key Features
- Technology Stack
- Installation
- Configuration
- Usage
- Admin Features
- Testing
- Major Error Handling
- Deployment
- License
- Credits
- Acknowledgement

## Project Overview

This project is part of the five milestone projects within the Full Stack Developer course offered by Code Institute. It is the fourth project in this course and represents my understanding of HTML, CSS, JavaScript, Python as well as many different application packages like Django, Cloudinary, SQL etc.

Eventify is a robust, full-featured event management platform built with Django that empowers users to create, discover, organize, and participate in events of all types. The application serves as a centralized hub for event coordination, providing both event creators and attendees with powerful tools to enhance their experience.
Eventify transforms how communities connect through events, providing a seamless bridge between event creators and participants while ensuring a smooth, engaging user experience from discovery through participation.
The application provides:

- User authentication and authorization
- Event creation and management
- Attendance tracking with status options
- Commenting system
- Date-based event filtering
- User profiles with event history
- Dedicated page containing information about the developer
- Collaboration form

### Event Creation & Management

- **Intuitive Event Setup:** Users can easily create events with comprehensive details including title, description, date/time, location, and featured images
- **Rich Text Editing:** Utilizing Django Summernote for enhanced event descriptions with formatting capabilities
- **Smart Slug Generation:** Automatic URL-friendly slugs based on event titles for clean, shareable links
- **Media Integration:** Cloudinary support for reliable image hosting and management

### Event Discovery & Exploration

- **Smart Filtering System:** Browse events by date range (upcoming, past, or all events)
- **Pagination:** Organized browsing experience with paginated results for large event collections
- **Visual Presentation:** Attractive card-based layout with event images, dates, and key information
- **Location Awareness:** Events include location data to help users find nearby activities

### Attendance Management

- **Multi-status RSVP System:** Users can indicate their attendance status with three options:

    1. Attending - Confirmed participation
    2. Maybe - Tentative attendance
    3. Can't Attend - Regretfully declining

- **Real-time Status Updates:** Instant reflection of attendance choices

- **Participation Analytics:** Visual indicators showing how many people are attending each event

- **Attendance History:** Personal track record of event participation in user profiles

### Interactive Engagement

- **Comment System:** Users can share thoughts and questions on event pages by posting comments
- **Comment Moderation:** Approval system for the admin to maintain content quality
- **Edit/Delete Functionality:** Users have control over their own contributions
- **Real-time Interactions:** Dynamic engagement between event organizers and attendees

### User Interface

- **Comprehensive Profiles:** Personal dashboards showing created events and attendance history across all status categories
- **Authentication System:** Secure registration and login using Django Allauth
- **Personalized Content:** Users see events relevant to their interests and participation history
- **Account Management:** Password change functionality from the Profile page

### Admin Interface

**From admin panel I can:**

- see/delete all the users and their emails (not passwords).
- check each user's permissions (staff status/superuser), active status, last login times etc.
- see/edit/delete all the events
- approve/delete comments by users
- change/delete attendance status of users

### Modern Design & UX

- **Responsive Design:** Fully functional across desktop, tablet, and mobile devices
- **Bootstrap Framework:** Clean, professional interface with consistent styling
- **Intuitive Navigation:** User-friendly menu system and clear information architecture
- **Visual Feedback:** Alert systems, modals and status indicators for user actions

## Agile methodology - Development

### User Stories

    - Using GitHub Kanban Board as the MVC framework
    the whole project was done through step by step process.

    [View the framework here](https://github.com/users/taz1003/projects/3/views/1)

![Kanban-board-MVC](static/images/event-agile.png)

## Key Features

### Homepage

- The landing page contains a navbar, events list that are paginated and a footer with all the social links
- The events are listed based on their occuring date
- There are 3 buttons for Upcoming, Past and All Events that automatically sort the events for the user

![Homepage](static/images/eventify-homepage-one.png)
![Homepage-2](static/images/eventify-homepage-two.png)

### Event Details and Creation Page

- Users can create, edit, and delete events

![Event-detail](static/images/eventify-detail.png)
![Create-event](static/images/eventify-create.png)

- Rich text descriptions with Summernote editor
- Image uploads via Cloudinary during event creation
- Automatic slug generation during event creation
- Date and location information requirement during event creation
- The event creation form does not let users leave blank fields.

![Event Creation Requirement](static/images/event-create-required.png)

- Event details contain image, location, date-time, exerpt and description
- Edit and Delete event buttons for the organizer
- A safety/assurance modal is shown for the user when delete event button is clicked

![Delete Event](Static/images/event-delete-modal.png)

- Three-tier attendance system (Attending/Maybe/Not Attending) that also shows the attendance count

![Attendance](static/images/attendance.png)

- Commenting with CRUD functionality alongside admin-approval workflow
- Users can't publish blank comments
- Dedicated comment-edit page
- A safety/assurance modal is shown for the user when delete button is clicked

![Comment Edit](static/images/edit-comment.png)

![Comment required](static/images/comment-required.png)

![Comment approval](static/images/comment-approval.png)

![Comment delete modal](static/images/delete-comment-modal.png)

### Profile Page

- User profiles showing created and attended events along with username

![Event-profile](static/images/eventify-profile.png)

- Password change functionality

![Password requirement](static/images/password-change-required.png)

### About Page

![About](static/images/eventify-about.png)

- Dedicated page about the information of the developer of this app
- Collaboration form for the users with automated emailing system
- Willing users can fill the collaboration form and after clinking on `Send` an automated
email will be sent to the developer
- Notification for the user after the email has been sent to the developer

![Collaboration Form Requirement](static/images/collab-form-required.png)

![Collaboration email sent notification](static/images/collab-sent-notif.png)

![Collaboration Email](static/images/email-recieved.png)

### SignUp, Login and Logout page

- **I intentionally kept email as optional due to one of my target users being younger students and poeple without access to emails but still willing to create events for their peers and communities**
- **As such I decided to remove `Forgot Your Password` functionality since this requires emails or phone numbers**

![Login Page](static/images/eventify-login.png)

- New users have restricted access as they can't create events, post comments etc.
- If they click on Profile link, they are redirected to the signUp page
- Logged in users after clicking on Logout are sent to a confirmation page to make sure accidental logout don't happen
- Users cannot have the same usernames and emails
- Users also cannot leave any of the form element on these pages blank as they are required

![User exists](static/images/user-exists.png)

![SignUp Page](static/images/eventify-signup.png)

![Signout Confirmation Page](static/images/signout-page.png)

### Admin Panel

- Summernote integration for rich text editing
- Advanced filtering and searching
- Bulk comment approval
- Attendance status management
- Account management
- Event management

![Admin-panel](static/images/eventify-admin.png)

## Technology Stack

### Backend

- Python 3.13.3
- Django 5.0
- Django Allauth (Authentication)
- Django Crispy Forms (Form styling)
- Django Summernote (Rich text editing)
- PostgreSQL (Production)
- SQLite (Development)
- Cloudinary (Image storage)
- EmailJS (Automatic email service)

### Frontend

- HTML5, CSS3, JavaScript
- Bootstrap 5
- Font Awesome (Icons)
- jQuery (DOM manipulation)

### Deployments

- GitHub
- Heroku
- WhiteNoise (Static files)
- dj-database-url (Database configuration)

## Installation

### Prerequisites

- Python
- pip
- PostgreSQL
- Cloudinary account

### Setup Instructions

- Clone Repository
- Create and activate a virtual environment
- Install dependencies: `pip install -r requirements.txt`
- Set up environment variables:
    - **Create a .env file in the root directory with:**
        - `SECRET_KEY=your_django_secret_key`
        - `DATABASE_URL=your_database_url`
        - `CLOUDINARY_URL=your_cloudinary_url`
- Run migrations: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Run the development server: `python manage.py runserver`

## Configuration

### Required Settings

- Configure DATABASES in settings.py environment
- Set up Cloudinary credentials in the .env file
- Update allowed hosts for production domain

### Optional Settings

- Customize event display limits
- Adjust pagination settings
- Modify comment admin-approval workflow

## Usage

### For Event Organizers / Users

- Create an account or log in
- Click "Create Event" to add your event details
- Manage your events through the profile page
- Monitor attendee responses

### For Users

- Browse events using filters
- Set your attendance status
- Leave comments on events
- Track your events in your profile

### For Admin

- Access the admin panel at /admin
- Moderate comments and events
- Manage user accounts
- View system analytics

## Admin Features

- Rich text editing for event descriptions
- Bulk actions for comment approval
- Advanced filtering options
- Quick edit functionality
- Date-based hierarchy navigation

## Testing

- See [testing.md](testing.md) document for all the Tests done for this project
# Blogg
This is a Django Rest Framework (DRF) application that allows users to create, read, update, and delete (CRUD) posts, as well as block and unblock other users.

## Table of Contents
## Features

- Users can create, read, update, and delete posts.
- Users can block and unblock other users.
- API endpoints follow RESTful conventions.
- Authentication using Django's built-in User model.
- Custom permissions to control access based on ownership and superuser privileges.
- Email notifications to users upon creating a new post.
- Nested serializer to include author's username and email when retrieving a single post.

## Requirements

- Python (>=3.6)
- Django (>=2.2)
- Django Rest Framework (>=3.11)
- A working email configuration in your Django project for email notifications.

## Installation

1. Clone the repository:
   git clone https://github.com/Kolliakshata/Blogg.git
   cd blog_project


Install the required packages using pip:
pip install -r requirements.txt

Configure your Django project settings, including database settings and email configuration.
Run database migrations:
python manage.py makemigrations
python manage.py migrate

Start the development server:
python manage.py runserver

Usage
Access the API at http://localhost:8000/api/.
Use authentication to interact with the API.

API Endpoints
GET /api/posts/: Returns a list of all posts.
POST /api/posts/: Creates a new post owned by the authenticated user.
GET /api/posts/<int:pk>/: Returns a single post by ID.
PUT /api/posts/<int:pk>/: Updates a single post owned by the authenticated user.
DELETE /api/posts/<int:pk>/: Deletes a single post owned by the authenticated user (soft delete).

Additional Endpoints for User Blocking:
GET /api/get-blocked-users/: Returns a list of users whom you have blocked.
POST /api/block-user/: Allows one user to block another user.
DELETE /api/unblock-user/: Allows one user to unblock another user.
Advanced Permissions
Superusers have full access to all posts and can update or delete any post regardless of ownership.
Non-superuser regular users can only CRUD their own posts.
Advanced Serializers
A nested serializer is used to include the author's username and email when retrieving a single post. The author's full details are not displayed on the list of all posts.
Email Notifications
Whenever a new post is created, an email notification is sent to the author, notifying them of the creation. Ensure you have configured email settings in your project.
Configuration
Customize the application as needed for your project. Update settings, serializers, and permissions based on your requirements.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the standard Git and GitHub workflow:

Fork the repository.
Create a new branch for your feature or bug fix: git checkout -b your-feature-branch
Make your changes and test thoroughly.
Commit your changes: git commit -m "Your descriptive commit message"
Push to your fork: git push origin your-feature-branch
Open a pull request to the main repository.

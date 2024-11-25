# Task Manager App

A simple Django-based task management app with Google authentication and admin invite features.

## Features
- Google Login for user authentication.
- Users can create, view, edit, and delete tasks.
- Admin can invite new users by email.
- Admin panel to manage Google OAuth keys and admin invites.

## Installation

### Prerequisites

- Python 3.x
- Django 5.x
- Django Allauth for Google Login
- A Gmail account for email sending (or other SMTP provider)

### Step-by-Step Installation

1. **Clone the repository:**

   Clone the project to your local machine:
   ```bash
   git clone https://github.com/srushtilohiya/TaskManager.git

2. **Navigate to the project directory:**
    ```bash
    cd YOUR_REPOSITORY_NAME  # e.g cd TaskManager

3. **Create a virtual environment:**
   It's best to use a virtual environment to avoid conflicts with other projects:
    ```bash
    python -m venv venv

4. **Activate the virtual environment:**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   
5. **Migrate the database:**
   Run the migrations to set up the database schema:
   ```bash
   python manage.py migrate

6. **Create a superuser (admin user):**
   To access the admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser

7. **Run the development server:**
   Finally, start the development server:
   ```bash
   python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the app.


## Using the Application

### Accessing Task Management
- **Tasks Page**: View all tasks, create new ones, or edit existing ones at:  
  [http://127.0.0.1:8000/tasks/](http://127.0.0.1:8000/tasks/)
- **Create a Task**:  
  [http://127.0.0.1:8000/tasks/create/](http://127.0.0.1:8000/tasks/create/)
- **Edit a Task**: Accessible by clicking "Edit" next to a task on the tasks page.

---

### User Invitations
- **Invite Users**: Invite users to collaborate on tasks with specific roles:  
  [http://127.0.0.1:8000/tasks/invite/](http://127.0.0.1:8000/tasks/invite/)

---

### Admin Panel Features

#### Key Features
- **User Management**:
  - Add, update, or delete users.
- **Task Oversight**:
  - View and manage all tasks created by any user.
- **Invite Users via Admin Panel**:
  - Add users and assign them tasks through the admin interface.

---

### Steps to Invite Users from the Admin Panel
1. **Log In to Admin Panel**:  
   Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with the superuser credentials.

2. **Access the Invitations Section**:
   - In the admin dashboard, locate the **Tasks** section.
   - Select the **Invitations** model.

3. **Create a New Invitation**:
   - Click **Add Invitation**.
   - Fill in the following details:
     - **Email**: Enter the user’s email address.
   - Save the invitation.

4. **Monitor Invitations**:
   - Use the admin interface to track the status of sent invitations.
   - Resend or revoke invitations if needed.

---

## Project Structure

```plaintext
TaskManager/
│
├── TaskManager/            # Main project folder
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL configuration
│   ├── wsgi.py             # WSGI entry point
│   └── asgi.py             # ASGI entry point
│
├── tasks/                  # Application folder
│   ├── templates/          # HTML templates
│   ├── models.py           # Database models
│   ├── views.py            # Views for handling requests
│   ├── urls.py             # App-specific routes
│   └── utils.py            # Utility functions
│
├── db.sqlite3              # SQLite database (local use)
├── manage.py               # Django CLI utility
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not included in the repo)

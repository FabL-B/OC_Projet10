# Django SoftDesk Project

## Description

SoftDesk is a Django application for managing projects, users, and tickets associated with those projects. Users can collaborate on projects, create tickets to report issues or request features, and track their progress.

## Features

### Non-logged-in user
- Sign up
- Log in

### Logged-in user
- Create a new project
- Add contributors to a project
- Create tickets linked to a project
- Update or delete tickets
- Manage contributors for a project
- Create comments for a ticket
- View accessible projects and their tickets

## Project Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/FabL-B/OC_Projet10
    cd softdesk
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # Linux/Mac
    env\Scripts\activate  # Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Load test data**:
    ```bash
    python manage.py loaddata fixtures/users.json
    ```

6. **Superuser credentials**:
   - **Username**: `admin`
   - **Password**: `mdpadmin`

7. **Test users**:
   - **Usernames**: `user1`, `user2`
   - **Password**: `mdpusertest`

8. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

9. **Access the application**:
    ```bash
    http://127.0.0.1:8000
    ```

10. **Admin interface**:
    ```bash
    http://127.0.0.1:8000/admin
    ```

## Endpoints

### Authentication
- `POST /signup/` : Register a new user
- `POST /login/` : Log in a user
- `POST /logout/` : Log out a user

### Projects
- `GET /projects/` : List all projects accessible by the user
- `POST /projects/` : Create a new project
- `GET /projects/{project_id}/` : Retrieve details of a specific project
- `PUT /projects/{project_id}/` : Update a project
- `DELETE /projects/{project_id}/` : Delete a project

### Contributors
- `GET /projects/{project_id}/contributors/` : List contributors of a project
- `POST /projects/{project_id}/contributors/` : Add a contributor
- `DELETE /projects/{project_id}/contributors/{contributor_id}/` : Remove a contributor

### Issues
- `GET /projects/{project_id}/issues/` : List all issues of a project
- `POST /projects/{project_id}/issues/` : Create a new issue
- `GET /projects/{project_id}/issues/{issue_id}/` : Retrieve details of a specific issue
- `PUT /projects/{project_id}/issues/{issue_id}/` : Update an issue
- `DELETE /projects/{project_id}/issues/{issue_id}/` : Delete an issue

### Comments
- `GET /projects/{project_id}/issues/{issue_id}/comments/` : List comments for an issue
- `POST /projects/{project_id}/issues/{issue_id}/comments/` : Create a comment
- `GET /projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` : Retrieve details of a specific comment
- `PUT /projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` : Update a comment
- `DELETE /projects/{project_id}/issues/{issue_id}/comments/{comment_id}/` : Delete a comment

# Django To-Do List API

The **Django To-Do List API** provides an easy way to manage tasks with features like creating, viewing, updating, and deleting to-do items. It supports **Basic Authentication** to ensure secure access to the API.

## Features

- Create a new to-do item.
- View all to-do items or a specific item by ID.
- Update an existing to-do item.
- Delete a to-do item.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework (DRF)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/django-todo-list.git
   cd django-todo-list
    ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
    ```
3. Run migrations:
   ```bash
   python manage.py migrate
    ```
4. Create a superuser for accessing the Django admin:
   ```bash
   python manage.py createsuperuser
    ```
5. Start the server:
   ```bash
   python manage.py runserver
    ```
   
# Authentication
All endpoints require Basic Authentication. Add your username and password when testing with Postman or 
any other client.

# API Endpoints

## 1. Create a To-Do Item
**Endpoints :** ```POST /api/todo/create/```

**Description :** Creates a new task.

**Request Body:**
```json
    {
        "title": "Buy groceries",
        "description": "Buy milk, bread, and eggs",
        "due_date": "2024-12-10",
        "tags": [{"name": "shopping"}, {"name": "urgent"}],
        "status": "OPEN"
    }
```

**Response:**
```json
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Buy milk, bread, and eggs",
        "timestamp": "2024-12-03T12:00:00Z",
        "due_date": "2024-12-10",
        "tags": [{"name": "shopping"}, {"name": "urgent"}],
        "status": "OPEN"
    }
```
## 2. Get All To-Do Items
**Endpoints :** ```GET /api/todo/```

**Description :** Fetches all tasks.

**Response:**
```json
    [
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Buy milk, bread, and eggs",
            "timestamp": "2024-12-03T12:00:00Z",
            "due_date": "2024-12-10",
            "tags": [{"name": "shopping"}, {"name": "urgent"}],
            "status": "OPEN"
        }
    ]
```

## 3. Get a Specific To-Do Item
**Endpoints :** ```GET /api/todo/{id}/```

**Description :** Fetches details of a specific task.

**Response:**
```json
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Buy milk, bread, and eggs",
        "timestamp": "2024-12-03T12:00:00Z",
        "due_date": "2024-12-10",
        "tags": [{"name": "shopping"}, {"name": "urgent"}],
        "status": "OPEN"
    }
```

## 4. Update a To-Do Item
**Endpoints :** ```PUT /api/todo/{id}/update/```

**Description :** Updates details of a specific task.

**Request Body:**
```json
    {
        "title": "Buy groceries",
        "description": "Buy milk, bread, and eggs",
        "due_date": "2024-12-10",
        "tags": [{"name": "shopping"}, {"name": "urgent"}],
        "status": "OPEN"
    }
```

**Response:**
```json
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Buy milk, bread, and eggs",
        "timestamp": "2024-12-03T12:00:00Z",
        "due_date": "2024-12-10",
        "tags": [{"name": "shopping"}, {"name": "urgent"}],
        "status": "OPEN"
    }
```
## 5. Delete a To-Do Item 
**Endpoints :** ```DELETE /api/todo/{id}/delete/```

**Description :** Deletes a task by its ID.

**Response:**
```json
    {
        "message": "To-do item deleted successfully."
    }
```

# Postman Collection JSON 
```json
    {
        "info": {
            "_postman_id": "todo-api-collection-1234",
            "name": "Todo API Collection",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [
            {
                "name": "Create Todo",
                "request": {
                    "method": "POST",
                    "url": {
                        "raw": "http://localhost:8000/api/todo/create/",
                        "protocol": "http",
                        "host": [
                            "localhost"
                        ],
                        "port": "8000",
                        "path": [
                            "api",
                            "todo",
                            "create"
                        ]
                    },
                    "body": {
                        "mode": "raw",
                        "raw": "{\n    \"title\": \"Buy groceries\",\n    \"description\": \"Buy milk, bread, and eggs\",\n    \"due_date\": \"2024-12-10\",\n    \"tags\": [\n        {\n            \"name\": \"shopping\"\n        },\n        {\n            \"name\": \"urgent\"\n        }\n    ],\n    \"status\": \"OPEN\"\n}"
                    },
                    "headers": [
                        {
                            "key": "Content-Type",
                            "value": "application/json"
                        }
                    ]
                }
            },
            {
                "name": "Get All Todos",
                "request": {
                    "method": "GET",
                    "url": {
                        "raw": "http://localhost:8000/api/todo/",
                        "protocol": "http",
                        "host": [
                            "localhost"
                        ],
                        "port": "8000",
                        "path": [
                            "api",
                            "todo"
                        ]
                    }
                }
            },
            {
                "name": "Get Todo by ID",
                "request": {
                    "method": "GET",
                    "url": {
                        "raw": "http://localhost:8000/api/todo/:id/",
                        "protocol": "http",
                        "host": [
                            "localhost"
                        ],
                        "port": "8000",
                        "path": [
                            "api",
                            "todo",
                            ":id"
                        ]
                    }
                }
            },
            {
                "name": "Update Todo by ID",
                "request": {
                    "method": "PUT",
                    "url": {
                        "raw": "http://localhost:8000/api/todo/:id/update/",
                        "protocol": "http",
                        "host": [
                            "localhost"
                        ],
                        "port": "8000",
                        "path": [
                            "api",
                            "todo",
                            ":id",
                            "update"
                        ]
                    },
                    "body": {
                        "mode": "raw",
                        "raw": "{\n    \"title\": \"Buy groceries and fruits\",\n    \"description\": \"Buy milk, bread, eggs, apples, and bananas\",\n    \"due_date\": \"2024-12-15\",\n    \"tags\": [\n        {\n            \"name\": \"shopping\"\n        },\n        {\n            \"name\": \"urgent\"\n        },\n        {\n            \"name\": \"groceries\"\n        }\n    ],\n    \"status\": \"WORKING\"\n}"
                    },
                    "headers": [
                        {
                            "key": "Content-Type",
                            "value": "application/json"
                        }
                    ]
                }
            },
            {
                "name": "Delete Todo by ID",
                "request": {
                    "method": "DELETE",
                    "url": {
                        "raw": "http://localhost:8000/api/todo/:id/delete/",
                        "protocol": "http",
                        "host": [
                            "localhost"
                        ],
                        "port": "8000",
                        "path": [
                            "api",
                            "todo",
                            ":id",
                            "delete"
                        ]
                    }
                }
            }
        ]
    } 
```


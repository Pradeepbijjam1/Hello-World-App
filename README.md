# Django Hello World App

This is a simple Django web app that provides a Hello World JSON response and an HTML page with a "Hello World!" message.

## Getting Started

Follow these instructions to run the web app on you IDE.

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.8 or higher)
- [Django](https://www.djangoproject.com/download/) (install using `pip install django`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/HelloWorldDjango.git
   cd HelloWorldDjango
```
2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
```
3. **Activate the virtual environment:**
```bash
venv\Scripts\activate
```
4. **Install the project dependencies:**
```bash
pip install -r requirements.txt
```
5. **Apply migrations:**
```bash
python manage.py migrate
```
6. **Start the development server:**
```bash
python manage.py runserver
```
7. **Open your browser and navigate to http://127.0.0.1:8000/**

##Accessing the Hello World JSON Response
JSON response URL: http://127.0.0.1:8000/hello/json/

##Notes

Make sure the virtual environment is activated whenever you are working on the project.



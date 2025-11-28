# Django TODO App

Minimal Django TODO application with create/edit/delete, due dates, and resolved flag.


Setup (PowerShell):

If `python` or `pip` are not on your PATH (common on Windows), use the `py` launcher or the module form `-m pip` shown below.

1) Create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies (use `py -3 -m pip` if `pip` isn't recognized):

```powershell
py -3 -m pip install -r ".\requirements.txt"
# or, after activating the venv, you can also run:
# pip install -r ".\requirements.txt"
```

3) Run migrations and (optionally) create an admin user:

```powershell
py -3 manage.py migrate
py -3 manage.py createsuperuser
```

Run with uvicorn (recommended):

```powershell
py -3 -m uvicorn todo_project.asgi:application --reload --port 8000
```

Or run the Django dev server:

```powershell
py -3 manage.py runserver
```

Notes:
- Use `py -3 -m pip` when `pip` is not found in the shell.
- If you prefer `python` and `pip` to be available directly, reinstall Python and enable "Add Python to PATH", or add the interpreter directory to your PATH.

The app root shows the todo list. Admin is available at `/admin`.

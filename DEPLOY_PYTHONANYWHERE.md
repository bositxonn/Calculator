# PythonAnywhere Deployment

1. Create a PythonAnywhere account and open a Bash console.
2. Upload or clone this project into your home directory.
3. Create a virtualenv and install your dependencies.
4. Copy `.env.example` to `.env` and set production values:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=yourusername.pythonanywhere.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com`
5. Run:

```bash
python manage.py migrate
python manage.py collectstatic
```

6. In the PythonAnywhere Web tab:
   - Set the source code path to this project.
   - Set the working directory to the project root.
   - Point the WSGI file to your Django project.
   - Add a static files mapping:
     - URL: `/static/`
     - Directory: `/home/yourusername/your-project-folder/staticfiles`

7. Update the WSGI file to load your project and environment before calling Django:

```python
import os
import sys
from pathlib import Path

project_home = "/home/yourusername/your-project-folder"
if project_home not in sys.path:
    sys.path.append(project_home)

env_path = Path(project_home) / ".env"
if env_path.exists():
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calculator_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

8. Reload the web app from the Web tab.

If your project uses a database other than SQLite, update the database settings separately before deployment.

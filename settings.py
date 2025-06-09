ALLOWED_HOSTS = ['*']  # For testing. Later add your Render URL for security.
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
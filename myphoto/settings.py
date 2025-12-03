# Render Deployment Settings
import os
import dj_database_url

# DATABASE (Render gives DATABASE_URL)
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }

# Static files for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = ['.onrender.com']

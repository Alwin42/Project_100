import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url # Required for Render DB

# Load environment variables from .env file (for local dev)
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Uses env var in production, falls back to insecure key for local dev
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure--g@dr16w$v+94vfod^%#0g*zh3if@!hm0!skh*2pam^e9iwe+c')

# SECURITY WARNING: don't run with debug turned on in production!
# Render sets 'RENDER' env var, so we use that to turn off Debug automatically
DEBUG = True

ALLOWED_HOSTS = ['*'] # Allow all hosts for now (easiest for Render)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', # Best practice: Place above staticfiles
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'corsheaders',
    'api', 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add WhiteNoise here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Configuration
CORS_ALLOW_ALL_ORIGINS = False 
CORS_ALLOWED_ORIGINS = [
    "https://nexuslearn-lyart.vercel.app", 
    "http://localhost:5173", 
    "http://127.0.0.1:5173",
]

# --- CSRF Trusted Origins (Crucial for POST requests) ---
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com", 
    "https://nexuslearn-lyart.vercel.app", 
    "https://nexuslearn-git-main-alwins-projects-1ac1f667.vercel.app", 
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        # This tells Django to automatically look for a 'DATABASE_URL' in your .env or Render environment
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable WhiteNoise to serve static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media Files (Cloudinary)
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_STORAGE_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_STORAGE_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_STORAGE_API_SECRET')
}

# REST Framework Config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
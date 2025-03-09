from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secure-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Set to False for production

# Add your domain name here for production
ALLOWED_HOSTS = ['yourdomain.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # Add CSP middleware for security
]

ROOT_URLCONF = 'LibraryProject.urls'

# Templates settings (use your specific template directories)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add paths to your template directories here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database configuration (use PostgreSQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Change to PostgreSQL
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Or your production database host
        'PORT': '5432',  # Default port for PostgreSQL
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Set the path where static files will be stored

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Set the path where media files will be stored

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'bookshelf.CustomUser'


# Security settings

# Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # CSRF protection cookies will only be sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookies will only be sent over HTTPS

# Protect against XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = 'DENY'  # Prevent embedding in an iframe

# Prevent content type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable SSL redirect (redirect all HTTP requests to HTTPS)
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS) to enforce HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy (CSP) - Add this for XSS protection
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://trusted.cdn.com")  # Replace with actual trusted CDN URLs
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com")
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
CSP_IMG_SRC = ("'self'",)

# Ensure SSL is enforced for cookies and sessions
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_EMBEDDER_POLICY = 'require-corp'

# Proxy SSL Header Setting (for reverse proxy like Nginx or load balancer)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

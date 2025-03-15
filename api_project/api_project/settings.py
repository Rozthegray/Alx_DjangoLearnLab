INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # ✅ Add this if missing
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # ✅ Add Token Authentication
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # ✅ Restrict access to authenticated users
    ],
}

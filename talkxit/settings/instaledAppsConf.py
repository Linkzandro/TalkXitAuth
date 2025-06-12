INSTALLED_APPS = []

FIRST_PARTY_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]

CUSTOM_APPS=[
    'talkxitCore.apps.TalkxitcoreConfig'
]
THIRD_PARTY_APPS=[
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    ]

INSTALLED_APPS+=FIRST_PARTY_APPS
INSTALLED_APPS+=CUSTOM_APPS
INSTALLED_APPS+=THIRD_PARTY_APPS


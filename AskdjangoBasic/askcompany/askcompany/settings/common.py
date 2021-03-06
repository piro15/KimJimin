import os
from os.path import abspath, dirname
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
# 프로젝트 경로.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5_+^djm(1x(+(&^a)8&p8qz%=@%rq#3b9bct3uwm1$q@cpam(4'

# !!!!!!SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 파이썬 소스코드 변경될 때마다 서버 재시작.

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop',
    'blog',
    'common',

    'django_extensions',
    'debug_toolbar',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'askcompany.urls'

TEMPLATES = [
    {
        # jinja2, mako, genshi, hamIPY도 있긴 하다.하지만 이게 가장 편하다.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [  # 리스트라서 여러 디렉토리 넣어줄 수 있지만 대개 한 개.
            os.path.join(BASE_DIR, 'askcompany', 'templates'),
        ],  # 템플릿 둘 디렉토리 경로 리스트. 각 앱에서 쓰일 템플릿은 앱 안의 템플릿 디렉토리에, 프로젝트 전빈적으로 쓰일 템플릿은 여기에.
        'APP_DIRS': True,  # 앱별로 템플릿 경로 추가할 것인지. False로 하면 각 앱 아래 있는 템플릿 경로 사용X
        'OPTIONS': {
            'context_processors': [  # 이 함수들은 모두 인자를 하나 받는다. request. 반환은 딕셔너리
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },  # 사전 하나.
    # 또 다른 사전 하나 추가해서 다른 템플릿 랭귀지 사용할 수 있다. 다수의 템플릿 엔진 설치 가능.
]

WSGI_APPLICATION = 'askcompany.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# connection 이면 디폴트, connections면 딕셔너리 형식으로 각 db이름에 맞게.

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# 장고 템플릿 시간 날짜 관련 https://youngwonhan-family.tistory.com/37

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'askcompany', 'static'),
]

MEDIA_URL = '/media/'  # 미디어 필드는 파일필드, 이미지 필드. 상속받아서 커스텀 필드 생성 가능.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INTERNAL_IPS = ['127.0.0.1']


# 마이그레이션, 마이그레이트: 모델의 변경내역을 데이터베이스 스키마(데이터 베이스 구조)에 반영.
# makemigrations: 마이그레이트할 파일 생성. 생성된 파일은 migrations디렉토리안에.
# 모델 필드 관련 어떤 변경이라도 발생하면!!! 하상 할 것. 변경 내역 누적.
# 파일이 너무 많아졌다고 지우면 절대 안된다. squashmigrations 명령으로 파일 통합은 가능.
# migrate: 마이그레이션 적용
# showmigrations: 마이그레이션 적용 현황 출력 X표가 적용완료 됐다는 표시.
# sqlmigrate 앱이름 마이그레이션이름 : SQL 내역 출력
# 마이그레이트 아직 안하고 하면 보여지긴 한다. 그대로 했다는 게 아니라 ~~이렇게 할 예정이라는 것을 보여주는 것.
#정방향, 역방향(롤백)


# 장고 디버그 툴바는 현재 서버에 대한 모든 환경변수 목록을 확인할 수 있기 때문에 아무나 확인할 수 있게 해주면 안된다.
# 장고 디버그 툴바 띄우기를 허용할 ip목록이 INTERNAL_IPS
# 로컬 호스트에서만 띄우게 설정.

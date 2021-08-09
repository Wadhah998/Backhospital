"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kAb55BSKW=ev?vu-9GzP3Lke*&*7rt8#5XzRvtvSzKVa9C#J!MPE%DJ#7=-TjYQ%^SLr=uvNJ8ff-PgYpsfhdv5mRf*KzvkF%Y5mu' \
             '*9TZrz@Q5QwHYJs@9T*DrqPUAgjC8A3x&9#+tq+Cz-+&SM^$JVxq&vNs9zT#$YhVkaWtEk6y5M&EyfJK_SVVyNd!NrZ@#yA' \
             '+dcn7y9qqY&^GHwZC%rJUdeSB%wcaATg3rk3bT9K?^SPfKCFqy=Z_S?&hFRfC-6ZzF9PC%f%QL&&kucWuU7^mdVdD-65^NFa#gxS6k' \
             '+@#DZV53c7-74kCrLfWxc$2NBWHtPaaK%^=?SStt^8$fsCx#FVLNp$@aA9txWQP+z5m=EnB65*2Ljjq5k7m%vB$RtEm$rL5K&M9jG' \
             '@tRqrzy8Afbupg!dH2_E9r$eyYeZL8yV8Zw*qwK@py+YTBU3YuSAF^4?htJvvv3KL5Lj_3EYY_' \
             '#KkbKLs_S2vCdaubaZ$ErzqUd8_Gmwe_$R+*E_!vv3=KtxA7w@m2FQsj=wM$2Jfky*svVK#E%9X^etsCVuq_vcPf&&b%DxgG+EW' \
             '@ALG$jXvhUA$cL9tCt!4f*X-Hr#r=GxNpvwgJ2_C#TQ$2vH3G7Ny?sh+-r6Hjm6e@k2_2hP!ZRg^AYg=&GnHEn8WL=*N' \
             '?*y9_Q$3Am$kW3wBSb5r?_$p8+68CxFkXAP+rq2WgKaFd+e*zd2X*n#u*47=aTt@Ryy*gag8F!8AC8QPT_-4QDzWBV$#Zn' \
             '+t_pZFvaErf@y4+2@E7%yhxSExf_VgF5bdZnK#R*NQXZby&wMRdJwFCUf!Q4kv@d@qvdCBaW*%=x=Z59Dj=URqpWs^uQ72rQn!KHp@Q' \
             '^fEBHS&Prd4W&aDde&?b4bfsq%ZP?V%R@$%rdzkfw^r4N++t!m$DN_VK=Bb5!^qpm^8a^4UdRHg&ur?$3p7huRECc' \
             '*5FH4c4VargV6VRzHGr?#CMYyVFGq#D8&%D5yWD+U2%G7%Jnbv$&K+S3AcE=cMQTCP23@pqc$T*vgg4QC' \
             '&wRsE5hvcv9QtAcXMVSGf$T9yK%8MasMz5rCRNEjy^=WZmdaLVFX5U9_jvKkYuL&b75?hh-6WuqG$ujv*U5%&KM_ExHk=u#Q_=s=K' \
             '?mHhJv%HQaH$x4BJHkC4q6*kqRVjYUPAWTdZCxqa$%w4upKeeSP9r%8$YUMP=&@HMjy*fR?=?y47q!ZV=VA7VdDX3+AQ2P-F' \
             '=xfA6SY8HgcW*_V8ZkuV!rKzZUHL$N9?ZrnfMd5skr7BZad&w!j!6eQk-d%Xzh^%kY#H9-ZSX@g_qwrnpfbP6+EdPX93G+$tNT@MzH' \
             '*t#KJPM%mms9Nw2=?#=+-f42tV+5UBp7&p*bZD!n%jNs8RP7SLW&!&6uwcS+kjf4$fd87VRMdr-83*d$XZpwzd!kK^jYNQAgpX4hcW' \
             '&z_v%@c+KdsBnWKdFD9ntufvc8g$scynnzAuafVSHK2_X9GJZSQTs24A=4%dVhPzjE9-NY$8n2YaN38_PdpW6wqVjmaPrGvC7nX' \
             '=UG4h-*ZrtvML29eQq8q#x3gU4L8cs-H7!r8KN@LHNpfjk^F53Ykf#8aVd3TM5^m6ZfgCB$gVmNnnNZDRtZNXGt7_d3gT5p&NGu&^Vw' \
             '-JYSch%5W6D$bYFAFKF#gqru+*E5h!E9BxtD72@*k7nt5WHM3pPY&g4xJcc4gExDkWPjVwuSvvZ-=E?4f3-z*s*L-tXp-fW@m#9Dd' \
             '@95754PEw5utT-Ucz9Hq4VjG-KxHTYL-8EPSzW#K8mHYf6uUKmVcJ9M8qBCS@HvJXLzv&&*rpV@U+CrGN*qMp5Nz%b#Cbbx-q' \
             '=hKFhd3u9VWV4HN$MDPD-Kj4P9PbZR8aUE8=rQynG3WF$BBVX-!D6u89VbjKx^^m-+yN$&NsBqCfv#X?KHguf&-%+c-@k7!=-Tq?9C' \
             '#RufMHdHw2rjz6Em4r7DLzvS&P&?Kvn&qKNy3V#aUFm9PN^DGvt_yN-EFrDsnqt-$hMTGm32es=Y+zB7QGmA=sQ2KRSueraSSvr' \
             '+aUhjj*esEpWPq6 '
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'gestionusers.Person'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'common',
    'gestionusers',
    'gestionpatient',
    'formparent',
    'formteacher'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

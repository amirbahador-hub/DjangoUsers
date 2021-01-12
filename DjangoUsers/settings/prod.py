from .base import *
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

# if not DEBUG:
#     # Configure Sentry
#     sentry_sdk.init(
#         dsn="https://944c462d13ce41188af624719f9248b6@o398389.ingest.sentry.io/5254018",
#         integrations=[DjangoIntegration()],
#
#         # If you wish to associate users to errors (assuming you are using
#         # django.contrib.auth) you may enable sending PII data.
#         send_default_pii=True
#     )
#
# INTERFACE_DOWNLOAD_IMAGES = True

# REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'SupersMarket.drf_utils.exception_handler'
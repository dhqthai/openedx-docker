# This file includes overrides to build the `development` environment for the LMS starting from the
# settings of the `production` environment

from docker_run_production import *
from .utils import Configuration, ensure_directory_exists

# Load custom configuration parameters from yaml files
config = Configuration(os.path.dirname(__file__))

if "sentry" in LOGGING.get("handlers"):
    LOGGING["handlers"]["sentry"]["environment"] = "development"

DEBUG = True
REQUIRE_DEBUG = True

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

PIPELINE_ENABLED = False
STATICFILES_STORAGE = "openedx.core.storage.DevelopmentStorage"

ALLOWED_HOSTS = ["*"]

FEATURES["AUTOMATIC_AUTH_FOR_TESTING"] = True

# ORA2 fileupload
ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = os.path.join(SHARED_ROOT, "openassessment_submissions")
# The code in edX ORA2 is missing appropriate checks so we must ensure here that this
# directory exists:
ensure_directory_exists(ORA2_FILEUPLOAD_ROOT)

ORA2_FILEUPLOAD_CACHE_ROOT = os.path.join(
    SHARED_ROOT, "openassessment_submissions_cache"
)

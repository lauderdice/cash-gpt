"""
File for storing constants used throughout the project
"""
import os

DEFAULT_LOGGER = "FlaskAPITemplateLogger"
COMMON_ENV_FILE = "app/common/env_files/.common_env"
PROJECT_NAME = "FastAPITemplate"
APP_NAME = "FlaskAPI_Application"
POST_METHOD = "POST"
GET_METHOD = "GET"

ENV_APP_ENV = "APP_ENV"

DOCS_URL = "docs"
THERE_WAS_PROBLEM_PROCESSING = "There was a problem processing this request.."

APIDOC_USERNAME = "user"
APIDOC_PASSWORD = "password"

CORRECT_APIKEY = "123456789"
X_API_KEY = "X-API-Key"
OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")
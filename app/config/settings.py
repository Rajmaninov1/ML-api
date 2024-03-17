from enum import Enum
from pydantic_settings import BaseSettings


class Environment(str, Enum):
    PROD = 'PROD'
    TEST = 'TEST'
    DEV = 'DEV'


class Settings(BaseSettings):
    # KINESIS_DATA_STREAM: str
    # AWS_ACCESS_KEY: str
    # AWS_SECRET_KEY: str
    # AWS_REGION_NAME: str

    ENVIRONMENT: Environment = Environment.TEST

    SENTRY_DNS: str

    WEB_APP_TITLE: str = 'ML Models API'
    WEB_APP_DESCRIPTION: str = 'Api to use multiple ML Models'
    WEB_APP_VERSION: str = '1.0.0'

    OPENAPI_SERVER: str = ''

    class Config:
        env_file = 'dev.env', 'test.dev', 'prod.env'
        env_file_encoding = 'utf-8'


settings = Settings()

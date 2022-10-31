import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CACHE_TYPE = os.getenv("CACHE_TYPE")
    CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
    CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
    CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")
    CACHE_REDIS_URL = os.getenv("CACHE_REDIS_URL")
    CACHE_DEFAULT_TIMEOUT = os.getenv("CACHE_DEFAULT_TIMEOUT")


class SystemConfig:
    # Postgres
    postgres_user = os.getenv('DB_USER')
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    host_server = os.getenv("HOST_SERVER")
    db_server_port = os.getenv("DB_SERVER_PORT")
    database_name = os.getenv("DB_NAME")

    database_url = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{host_server}:{db_server_port}/' \
                   f'{database_name}'


system_config = SystemConfig()

import os


class PostgresAsyncConfig:

    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_NAME = os.environ.get("POSTGRES_NAME", "postgres")
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")


    @property
    def POSTGRES_URL(self):
        print(f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}")
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

posgres_async_config = PostgresAsyncConfig()
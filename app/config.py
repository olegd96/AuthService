from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, AliasChoices


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: Literal["DEBUG", "INFO"]

    DB_HOST: str = Field(alias="DB_HOST")
    DB_PORT: int = Field(alias="DB_PORT")
    DB_USER: str = Field(alias="DB_USER")
    DB_PASS: str = Field(alias="DB_PASS")
    DB_NAME: str = Field(alias="DB_NAME")

    SECRET_KEY: str = Field(alias="SECRET_KEY")
    ALGORITHM: str = Field(alias="ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(alias="REFRESH_TOKEN_EXPIRE_DAYS")

    TEST_DB_HOST: str = Field(alias="TEST_DB_HOST")
    TEST_DB_PORT: int = Field(alias="TEST_DB_PORT")
    TEST_DB_USER: str = Field(alias="TEST_DB_USER")
    TEST_DB_PASS: str = Field(alias="TEST_DB_PASS")
    TEST_DB_NAME: str = Field(alias="TEST_DB_NAME")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_TYPE: str = 'mongodb'
    DB_USER: str = ''
    DB_PASSWORD: str = ''
    DB_HOST: str = 'localhost'
    DB_PORT: str = '27017'
    DB_NAME: str = 'forms_db'
    SECRET_KEY: str = 'secret local'

    @property
    def db_url(self):
        return (
            f'{self.DB_TYPE}:{self.DB_USER}/{self.DB_PASSWORD}/'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )


settings = Settings()

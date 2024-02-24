from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    
    class Config:
        env_file = ".env"

settings = Settings()


if __name__ == "__main__":

    print(settings.db_user, settings.db_host, settings.db_port, settings.db_name)
  
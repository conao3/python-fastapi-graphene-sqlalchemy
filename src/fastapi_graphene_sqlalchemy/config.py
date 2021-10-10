from pydantic import BaseSettings

class Settings(BaseSettings):
    db_address: str
    db_port: str
    db_name: str
    db_username: str
    db_password: str

    @property
    def db_config(self):
        return {
            "drivername": "postgresql",
            "username": self.db_username,
            "password": self.db_password,
            "host": self.db_address,
            "port": self.db_port,
            "database": self.db_name,
        }

    class Config:
        env_file = ".env"


settings = Settings()

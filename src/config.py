class BaseConfig:
    TESTING = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass

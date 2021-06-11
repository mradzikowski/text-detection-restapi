def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert not test_app.config["TESTING"]


def test_testing_config(test_app):
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert test_app.config["TESTING"]


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert not test_app.config["TESTING"]

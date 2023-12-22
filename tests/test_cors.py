def test_add_corsheaders_app(settings):
    installed_app = "corsheaders"
    assert installed_app in settings.INSTALLED_APPS, (
        f"Check that in the `wordicum/settings.py` file with the project settings, there has been added in `INSTALLED_APPS` "
        f"the ` {installed_app}` app"
    )


def test_cors_middleware(settings):
    cors_middleware = "corsheaders.middleware.CorsMiddleware"
    assert cors_middleware in settings.MIDDLEWARE, (
        f"Check that in the `wordicum/settings.py` file with the project settings, there has been added in `MIDDLEWARE`"
        f"the `{cors_middleware}` middleware"
    )

    django_common_middleware = "django.middleware.common.CommonMiddleware"
    django_common_middleware_index = settings.MIDDLEWARE.index(django_common_middleware)
    cors_middleware_index = settings.MIDDLEWARE.index(cors_middleware)
    assert cors_middleware_index < django_common_middleware_index, (
        "Check that in the `wordicum/settings.py` file, there is in the `MIDDLEWARE` list"
        f"the `{cors_middleware}` handler and is placed before the `{django_common_middleware}`."
    )


def test_cors_allowed_origins(settings):
    setting_name = "CORS_ALLOWED_ORIGINS"
    assert hasattr(settings, setting_name), (
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"`{setting_name}` list has been added"
    )

    expected_host = "http://localhost:3000"
    assert expected_host in settings.CORS_ALLOWED_ORIGINS, (
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"`{setting_name}` list includes the `{expected_host}` host."
    )


def test_disable_cors_origin_allow_all(settings):
    setting_name = "CORS_ORIGIN_ALLOW_ALL"
    actual_value = getattr(settings, setting_name, None)
    assert actual_value is None or actual_value is False, (
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"`{setting_name}` parameter isn't there, or its value equals `False`"
    )

def test_add_corsheaders_app(settings):
    installed_app = "corsheaders"
    assert installed_app in settings.INSTALLED_APPS, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта в `INSTALLED_APPS` "
        f"добавлено приложение `{installed_app}`"
    )


def test_cors_middleware(settings):
    cors_middleware = "corsheaders.middleware.CorsMiddleware"
    assert cors_middleware in settings.MIDDLEWARE, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта в `MIDDLEWARE` "
        f"добавлено middleware `{cors_middleware}`"
    )

    django_common_middleware = "django.middleware.common.CommonMiddleware"
    django_common_middleware_index = settings.MIDDLEWARE.index(django_common_middleware)
    cors_middleware_index = settings.MIDDLEWARE.index(cors_middleware)
    assert cors_middleware_index < django_common_middleware_index, (
        "Проверьте, что в файле `ya_tube/settings.py` в списке `MIDDLEWARE` "
        f"обработчик `{cors_middleware}` размещен раньше `{django_common_middleware}`."
    )


def test_cors_allowed_origins(settings):
    setting_name = "CORS_ALLOWED_ORIGINS"
    assert hasattr(settings, setting_name), (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"добавлен список `{setting_name}`"
    )

    expected_host = "http://localhost:3000"
    assert expected_host in settings.CORS_ALLOWED_ORIGINS, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"в списке `{setting_name}` присутствует хост `{expected_host}`."
    )


def test_disable_cors_origin_allow_all(settings):
    setting_name = "CORS_ORIGIN_ALLOW_ALL"
    actual_value = getattr(settings, setting_name, None)
    assert actual_value is None or actual_value is False, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"нет параметра `{setting_name}` или его значение равно `False`"
    )

import pytest


@pytest.mark.parametrize(
    "default_class",
    [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ]
)
def test_rest_framework_throttle_classes(settings, default_class):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"добавлена настройка `{setting_name}`"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_CLASSES'
    assert rest_framework_key in rest_framework_setting, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"добавлен ключ `{rest_framework_key}`"
    )

    assert default_class in rest_framework_setting[rest_framework_key], (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"по ключу `{rest_framework_key}` добавлен класс `{default_class}`"
    )


@pytest.mark.parametrize(
    "rate_client, rate",
    [
        ('user', '100000/minute'),
        ('anon', '1000/minute')
    ]
)
def test_rest_framework_throttle_rates(settings, rate_client, rate):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"добавлена настройка `{setting_name}`"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_RATES'
    assert rest_framework_key in rest_framework_setting, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"добавлен ключ `{rest_framework_key}`"
    )

    throttle_rate = rest_framework_setting[rest_framework_key]
    assert isinstance(throttle_rate, dict), (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"по ключу `{rest_framework_key}` добавлен словарь."
    )

    actual_rate = throttle_rate.get(rate_client, None)
    assert actual_rate is not None, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"по ключу `{rest_framework_key}` в словаре `{rest_framework_key}` есть ключ `{rate_client}`."
    )

    assert actual_rate == rate, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"по ключу `{rest_framework_key}` в словаре `{rest_framework_key}` по ключу `{rate_client}` "
        f"установлен лимит согласно условию задания."
    )

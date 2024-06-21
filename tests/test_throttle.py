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
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"` {setting_name}` setting has been added"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_CLASSES'
    assert rest_framework_key in rest_framework_setting, (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has the added key `{rest_framework_key}`"
    )

    assert default_class in rest_framework_setting[rest_framework_key], (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has the class `{default_class}` added to the `{rest_framework_key}`key"
    )


@pytest.mark.parametrize(
    "rate_client, rate",
    [
        ('user', '100/minute'),
        ('anon', '10/minute')
    ]
)
def test_rest_framework_throttle_rates(settings, rate_client, rate):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"` {setting_name}` setting has been added"
    )

    rest_framework_key = 'DEFAULT_THROTTLE_RATES'
    assert rest_framework_key in rest_framework_setting, (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has the added key `{rest_framework_key}`"
    )

    throttle_rate = rest_framework_setting[rest_framework_key]
    assert isinstance(throttle_rate, dict), (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has a dictionary added to the `{rest_framework_key}` key."
    )

    actual_rate = throttle_rate.get(rate_client, None)
    assert actual_rate is not None, (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has a key in `{rest_framework_key}` of the dictionary `{rest_framework_key}` named `{rate_client}`."
    )

    assert actual_rate == rate, (
        f"Check that in the wordicum/settings.py file in the project settings, {setting_name} "
        f"has a key in {rest_framework_key} named {rate_client} "
        f"with the limit set according to the task condition."
    )

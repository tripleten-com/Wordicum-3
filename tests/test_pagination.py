import pytest


@pytest.mark.parametrize(
    "rest_framework_key, expected_value",
    [
        ('DEFAULT_PAGINATION_CLASS', 'rest_framework.pagination.PageNumberPagination'),
        ('PAGE_SIZE', 10)
    ]
)
def test_rest_framework_pagination(settings, rest_framework_key, expected_value):
    setting_name = "REST_FRAMEWORK"
    rest_framework_setting = getattr(settings, setting_name, None)
    assert rest_framework_setting is not None, (
        f"Check that in the `wordicum/settings.py` file with the project settings, the"
        f"` {setting_name}` setting has been added"
    )

    assert rest_framework_key in rest_framework_setting, (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has the added key `{rest_framework_key}`"
    )

    actual_value = rest_framework_setting[rest_framework_key]
    assert actual_value == expected_value, (
        f"Check that in the `wordicum/settings.py` file with the project settings, `{setting_name}` "
        f"has the key `{rest_framework_key}` with the value specified by the task conditions."
    )

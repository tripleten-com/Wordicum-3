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
        f"Проверьте, что в файле `ya_tube/settings.py` с настройками проекта "
        f"добавлена настройка `{setting_name}`"
    )

    assert rest_framework_key in rest_framework_setting, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"добавлен ключ `{rest_framework_key}`"
    )

    actual_value = rest_framework_setting[rest_framework_key]
    assert actual_value == expected_value, (
        f"Проверьте, что в файле `ya_tube/settings.py` c настройками проекта в `{setting_name}` "
        f"по ключу `{rest_framework_key}` установлено значение по условию задания."
    )

import pytest
from rest_framework import filters

try:
    from api.views import PostModelViewSet
except ImportError:
    raise AssertionError(
        "При импорте из файла `api/views.py` "
        "представления `PostModelViewSet` произошла ошибка."
    )


@pytest.mark.parametrize(
    "filter_, fields_attr, field",
    [
        (filters.SearchFilter, "search_fields", "text",),
        (filters.OrderingFilter, "ordering_fields", "pub_date",),
    ]
)
def test_filtering(filter_, fields_attr, field):
    assert filter_ in PostModelViewSet.filter_backends, (
        "Проверьте, что в файле `api/views.py` в представлении `PostModelViewSet` в атрибуте"
        "`filter_backends` указан нужный backend класс согласно заданию."
    )

    fields = getattr(PostModelViewSet, fields_attr)
    for actual_field in fields:
        # Проверка подстроки в строке, нужно для случая проверки использования спец символов
        assert field in actual_field, (
            f"Проверьте, что в файле `api/views.py` в представлении `PostModelViewSet` в атрибуте"
            f"`{fields_attr}` указан поле согласно заданию."
        )

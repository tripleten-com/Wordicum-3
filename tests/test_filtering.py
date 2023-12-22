import pytest
from rest_framework import filters

try:
    from api.views import PostModelViewSet
except ImportError:
    raise AssertionError(
        "When importing from the `api/views.py` file,"
        "an error occurred in the output of `PostModelViewSet`."
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
        "Check that in the `api/views.py` file, in the `PostModelViewSet` view, the attribute"
        "` filter_backends` has the required back-end class specified according to the task."
    )

    fields = getattr(PostModelViewSet, fields_attr)
    for actual_field in fields:
        # Checking a substring in a string when checking the use of special characters
        assert field in actual_field, (
            f"Check that in the `api/views.py` file, in the `PostModelViewSet` view, the attribute"
            f"`{fields_attr}` has the field specified according to the task."
        )

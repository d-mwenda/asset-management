from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist


def get_all_items(model):
    # add support for order_by passed as a kwarg later
    payload = model.objects.all()
    if not payload.exists():
        payload = 'We found no items to display'
    return payload


def check_if_queryset(payload):
    if isinstance(payload, QuerySet):
        return True
    else:
        return False


def get_single_unique_item(model, query_arg):
    """
    :param model: model that you're querying
    :param query_arg:
    """
    try:
        return model.objects.get(query_arg)
    except ObjectDoesNotExist:
        return None

from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cached_categories():
    if CACHE_ENABLED:
        categories = cache.get('categories')
        if categories is None:
            categories = Category.objects.all()
            cache.set('categories', categories)
    else:
        categories = Category.objects.all()
    return categories
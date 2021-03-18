"""
Helper function used in src.api.routes.main_urls.py
for routing URLs to the appropriate view functions
"""


def re_path(route, view, **kwargs):
    return view, route, kwargs

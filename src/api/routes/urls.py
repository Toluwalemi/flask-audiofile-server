def bootstrap_routes(app, **kwargs):
    """
    :param app:
    :return:
    """
    from src.api.routes.main_urls import urlpatterns as main_urls
    for (v, r, k) in main_urls:
        v.register(app, route_base=r, **k, **kwargs)


__all__ = ['bootstrap_routes']

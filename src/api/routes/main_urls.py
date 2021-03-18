from src.api.helpers import re_path
from src.api.views import AudioView

urlpatterns = [

    re_path('/audio/', AudioView),
]

__all__ = ['urlpatterns']

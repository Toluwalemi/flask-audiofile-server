from src.api.helpers import re_path
from src.api.views import AudioView, AudioItemView

urlpatterns = [

    re_path('/audio/', AudioView),
    re_path('/audio/<audioFileType>/<audioFileID>', AudioItemView)
]

__all__ = ['urlpatterns']

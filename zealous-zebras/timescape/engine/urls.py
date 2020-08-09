from rest_framework.routers import SimpleRouter
from .viewsets import SearchViewSet


router = SimpleRouter()
router.register('', SearchViewSet, basename="searchs")
urlpatterns = router.urls

from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects') #genera 4urls(get,post, put, delete)

urlpatterns = router.urls

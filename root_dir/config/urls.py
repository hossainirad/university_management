from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

<<<<<<< HEAD
=======

>>>>>>> d964d03cf0658392fd5eb33e3ba2e5abf56c5130
schema_view = get_schema_view(
   openapi.Info(
      title="Rana System",
      default_version='v1',
<<<<<<< HEAD
      description="This is created by Rana"
=======
      description="This is created by Rana",
>>>>>>> d964d03cf0658392fd5eb33e3ba2e5abf56c5130
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

<<<<<<< HEAD
=======

>>>>>>> d964d03cf0658392fd5eb33e3ba2e5abf56c5130
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('sw/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

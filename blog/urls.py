from django.contrib import admin
from django.urls import path, include
from hello_world.views import HelloWorldView, PostView
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', HelloWorldView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
    # path('posts/', PostView.as_view()),
]

router=routers.SimpleRouter()
router.register('post', PostView, basename = "post")

urlpatterns+=router.urls
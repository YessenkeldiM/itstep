from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = SimpleRouter()

router.register('goods', views.APIGoodsViewSet)
router.register('magazing', views.APIReadonlyMagazinViewSet)


urlpatterns = [
    # path("api/goods/", views.api_goods, name="api-goods"),
    # path("api/good_detail/<int:pk>/", views.api_good_detail, name="detail"),
    # path("api/goods/", views.APIGoods.as_view(), name="api-goods"),
    # path("api/good_detail/<int:pk>/", views.APIGoodsDetail.as_view(), name="detail"),
    path('api/', include(router.urls)),
]
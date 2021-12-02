from django.urls import path
from .views import GoodsListView

app_name = 'mainapp'


urlpatterns = [
    path('', GoodsListView.as_view(), name='goods'),
    path('<int:pk>/', GoodsListView.as_view(), name='goods_by_category'),
    # path('category/<int:pk>/', products, name='category'),
    # path('category/<int:pk>/page/<int:page>/', products, name='page'),
    # path('product/<int:pk>/', product, name='product'),
]
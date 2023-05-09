from django.urls import path
from .views import *
ListArticle

app_name = 'inventory'
urlpatterns = [
    path('article/create/', CreateArticle.as_view(), name='create_article'),
    path('article/update/<int:pk>/', UpdateArticle.as_view(), name='update_article'),
    path('article/list/', ListArticle.as_view(), name="list_article"),
    path('article/detail/<int:pk>/', RetrieveArticle.as_view(), name="detail_article"),
    path('ordering/create/', CreateOrder.as_view(), name="create_order"),
    

]

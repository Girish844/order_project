from django.urls import path
from . import views

urlpatterns = [
    path('', views.test,name="test fun"),
    path('login_page', views.login_view, name="To open login page"),
    path('order_history', views.order_history, name="To open order history page"),
    path('reg_page', views.reg_view,name="To open reg page"),
    path('login', views.login,name="login user"),
    path('register', views.register,name="register user"),
    path('order_view', views.order_view, name="To order page page"),
    path('order', views.order, name="order "),
    path("api",views.article_list),
    path("detail/<int:pk>/",views.article_detail),
    path("charts/",views.chart_detail)
]

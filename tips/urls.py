from django.urls import path, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name="tips"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('rule/', views.RuleView.as_view(), name="rule"),
    path('top/', views.TopView.as_view(), name="top"),
    path('create/', views.Create_account.as_view(), name="create"),
    path('login/', views.Account_login.as_view(), name="login"),
    path('top/logined/threadcreate/', views.create, name="tcreate" ),
    path('top/detail/<int:pk>/',views.detail, name='detail'),
    path('top/detail/<int:pk>/create/', views.Comment.as_view(), name='comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

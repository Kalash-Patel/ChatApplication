from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.UserRegistrationAPIview.as_view(), name="sign-up"),
    path('api/login/', views.UserLoginAPIview.as_view(), name="sign-in"),
    path('api/online-users/', views.UserOnlineUsersAPIview.as_view(), name="online-users"),
    path('api/chat/start/', views.StartAPIview.as_view(), name="log-out"),
    path('api/chat/send/<str:group_name>/', views.home1, name="sendmsg"),
    path('api/suggested-friends/<int:id>', views.SuggestedFriendsAPIview.as_view(), name="suggested-friends"),
]
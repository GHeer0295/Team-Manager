from django.urls import path
from TeamManager.views import team_member_delete
from . import views
from .views import HomeView, addMemberView, UpdateTeamMemberView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_new/', addMemberView.as_view(), name='add_new'),
    path('member/edit/<int:pk>', UpdateTeamMemberView.as_view(), name='update_member'),
    path('member/delete/<int:pk>', team_member_delete, name='delete_member')
]

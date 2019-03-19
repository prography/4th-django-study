from django.urls import path
from drf_app1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include


urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('class-view/snippets/', views.SnippetList.as_view()),
    path('class-view/snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('class-generic-view/snippets/', views.SnippetList_generic.as_view()),
    path('class-generic-view/snippets/<int:pk>/', views.SnippetDetail_generic.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

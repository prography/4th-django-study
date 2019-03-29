from django.urls import path, include
from drf_app1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter



snippet_list = views.ModelViewSnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.ModelViewSnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.ModelViewSnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.ModelViewUserViewSet.as_view({
    'get': 'list'
})
user_detail = views.ModelViewUserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'snippets', views.ModelViewSnippetViewSet)
router.register(r'users', views.ModelViewUserViewSet)

urlpatterns = [
    path('', views.api_root),

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('class-view/snippets/', views.SnippetList.as_view()),
    path('class-view/snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('class-generic-view/snippets/', views.SnippetList_generic.as_view()),
    path('class-generic-view/snippets/<int:pk>/', views.SnippetDetail_generic.as_view()),

    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('view-set/users')

    path('view-set/snippets/', snippet_list, name='snippet-list'),
    path('view-set/snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('view-set/snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('view-set/users/', user_list, name='user-list'),
    path('view-set/users/<int:pk>/', user_detail, name='user-detail'),

    path('router/', include(router.urls)),

]

#urlpatterns = format_suffix_patterns(urlpatterns)

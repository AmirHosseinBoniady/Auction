from django.urls import path

from . import views

from .views import ComplaintListView, PostView, PostListView, ComplaintDetailView, CommentView,ComplaintDetailView


urlpatterns = [
    path('',views.landing),
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:post_pk>/', PostView.as_view(), name='post'),
    path('post-list', PostListView.as_view(), name='post-list'),
    path('post/<int:post_pk>/comments/', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/complaint/', ComplaintDetailView.as_view(), name='complaint'),
    path('complaints/', ComplaintListView.as_view(), name='complaint-list'),
]

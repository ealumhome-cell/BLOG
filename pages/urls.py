from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostArchivedListView, PostDraftListView, LoginPageViews

urlpatterns = [
    path("", PostListView.as_view(),name="post_list"),
    path("<int:pk>/", PostDetailView.as_view(),name="post_detail"),
    path("archived", PostArchivedListView.as_view(),name="post_archived"),
    path("draft", PostDraftListView.as_view(),name="post_drafts"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path('login/',LoginPageViews.as_view(), name="login" )
]
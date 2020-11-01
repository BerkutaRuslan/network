from django.urls import path

from posts.views import CreatePostView, AddLikeView, RemoveLikeView

urlpatterns = [
    path('create', CreatePostView.as_view()),
    path('<int:pk>/like', AddLikeView.as_view()),
    path('<int:pk>/unlike', RemoveLikeView.as_view()),
    # path('analytics'),
]
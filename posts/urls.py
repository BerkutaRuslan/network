from django.urls import path

from posts.views import CreatePostView

urlpatterns = [
    path('create', CreatePostView.as_view()),
    # path('<int:pk>/like', AddLikeView.as_view()),
    # path('<int:pk>/unlike'),
    # path('analytics'),
]
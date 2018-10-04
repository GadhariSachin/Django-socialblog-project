from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^(?P<id>\d+)/post-edit/', views.PostEditView, name='postedit'),
    url(r'^(?P<id>\d+)/post-delete/', views.PostDeleteView, name='delete'),
    url(r'^articlelist/$', views.PostListView, name='postlist'),
    url(r'^create-blog/', views.PostCreateView, name='create'),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.PostDetailView, name='postdetail'),
    url(r'^likes/', views.LikePostView, name='likepost'),
]

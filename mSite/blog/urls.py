from django.conf.urls import url, include
from blog.models import Post
from . import views

urlpatterns = [
# 포스트 목록
    url(r'^$', views.post_list, name='post_list'),

# 포스트 제목 클릭시 나오는 창 출력
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

# 새글입력 링크
    url(r'^post/new/$', views.post_new, name='post_new'),

#글 수정링크
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]

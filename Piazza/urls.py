from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework import urlpatterns

from Piazza import views
from Piazza.crud import CreateCourse, DisplayCourses, CreatePost

urlpatterns=[
    url(r'welcome',views.welcome_teacher,name='welcome'),
    url(r'new_course',CreateCourse.as_view()),
    url(r'display_course',DisplayCourses.as_view()),
    url(r'post/(?P<c_name>[A-Za-z0-9]+)/$',views.display_posts),
    url(r'new_post',CreatePost.as_view())
]
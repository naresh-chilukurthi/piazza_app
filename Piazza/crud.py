from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from Piazza.models import Course, post

class CreateCourse(CreateView):
    model=Course
    template_name = "new_course.html"
    fields = ['course_name', 'course_desc','teacher']
    success_url = reverse_lazy('welcome')
class DisplayCourses(ListView):
    model=Course
    template_name ="disp_course.html"
    context_object_name = "object_list"
class CreatePost(CreateView):
    model = post
    template_name = "new_post.html"
    fields = ['post_desc', 'post_details', 'course','posted_by']
    success_url = reverse_lazy('welcome')

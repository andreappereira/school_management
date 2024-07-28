"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from rest_framework import routers


from course.views import coursesViewSet

from registration.views import ListRegistrationStudent, ListStudentsEnrolledInTheCourse, RegistrationViewSet
from student.views import StundesViewSet


router_v1 = routers.DefaultRouter()
router_v1.register('students', StundesViewSet, basename='Students')
router_v1.register('courses', coursesViewSet, basename='courses')
router_v1.register('registrations', RegistrationViewSet, basename='Registrations')

router_v2 = routers.DefaultRouter()
router_v2.register('students', StundesViewSet, basename='Students')


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('v1/', include((router_v1.urls, 'api'), namespace='v1')),
    path('v2/', include((router_v2.urls, 'api'), namespace='v2')),
    path('v1/student/<int:pk>/registrations/', ListRegistrationStudent.as_view(), name='v1-student-registrations'),
    path('v1/course/<int:pk>/students/', ListStudentsEnrolledInTheCourse.as_view(), name='v1-course-students'),
    path('', RedirectView.as_view(url='/v1/', permanent=True)),
]


# router = routers.DefaultRouter()
# router.register('students', StundesViewSet, basename='Students')
# router.register('courses', coursesViewSet, basename='courses')
# router.register('registrations', RegistrationViewSet, basename='Registrations')

# urlpatterns = [
#     path('api-auth/', include('rest_framework.urls')),
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('student/<int:pk>/registrations/', ListRegistrationStudent.as_view()),
#     path('course/<int:pk>/students/', ListStudentsEnrolledInTheCourse.as_view()),
# ]
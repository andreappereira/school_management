from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from rest_framework.test import APITestCase
from rest_framework import status

from course.models import Course


# Create your tests here.
class CourseTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('v1:courses-list')

        self.user = User.objects.create_user(username='testuser', password='testpassword')

        add_course_permission = Permission.objects.get(codename='add_course')
        change_course_permission = Permission.objects.get(codename='change_course')
        
        self.user.user_permissions.add(add_course_permission)
        self.user.user_permissions.add(change_course_permission)
        
        self.client.force_authenticate(user=self.user)

        self.course_1 = Course.objects.create(
            name='Test Course 1',
            description='Django Test',
            level=Course.courseLevel.MEDIUM
        )

        self.course_2 = Course.objects.create(
            name='Test Course 2',
            description='Django Test 2',
            level=Course.courseLevel.MEDIUM
        )

        self.course_1_url = f'/v1/courses/{self.course_1.id}/'

    def test_retrieve_courses_list(self):
        """
        Test the retrieval of the course list.

        This test ensures that the course listing API endpoint returns an HTTP 200 OK status.
        """

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        """
        Test the creation of a new course.

        This test ensures that a new course can be created via the API.
        """

        data = {
            'name': 'New Test Course',
            'description': 'New Django Test',
            'level': Course.courseLevel.MEDIUM
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_course(self):
        """
        Test the update of an existing course.
        """
        updated_data = {
            'name': 'Updated Test Course',
            'description': 'Updated Django Test',
            'level': Course.courseLevel.ADVANCED
        }
        response = self.client.put(self.course_1_url, updated_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
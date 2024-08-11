from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import blogView
from blog.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone

class PostModelTest(TestCase):
    def setUp(self) -> None:
        self.email = "admin@gmail.com"
        self.password = "admin"
        first_name = "admin"
        last_name = "admin"
        self.user = User.objects.create_user(email = self.email, first_name = first_name, last_name= last_name,password = self.password)
        self.post = Post.objects.create(author=self.user,status=1, content="Django content", viewers=22)
        self.url=reverse('post')
        self.response = self.client.get(self.url)
        self.post.save()
    
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_count_query(self):
        qs = Post.objects.all()
        self.assertTrue(qs.exists())
        self.assertEqual(qs.count(), 1)
    
    def test_url_name_list_view(self):
        self.view = resolve('/')
        self.assertEqual(self.view.url_name, 'post')
    
    def test_template_use_in(self):
        self.assertTemplateUsed(self.response, 'landing/base.html')
    
    def test_content_in_queryset(self):
        qs = Post.objects.get(status=1, published_at__lte =timezone.now())
        # print(qs)
        self.assertIn("Django", qs.content)
    
    def test_first_name_max_length(self):
        author = User.objects.get(id=1)
        email = author.email
        self.assertEqual(email, 'admin@gmail.com')

    def test_object_name_is_last_name_comma_first_name(self):
        author = User.objects.get(id=1)
        expected_object_name = f'{author.first_name}'
        self.assertEqual(str(author.first_name), expected_object_name)

    
    def tearDown(self):
        print("Done..")
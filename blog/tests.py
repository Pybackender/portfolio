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
        self.user = User.objects.create_user(email = self.email, password = self.password)
        self.post = Post.objects.create(author=self.user,status=1, content="Django content", viewers=22)
        self.url=reverse('post')
        self.response = self.client.get(self.url)
        self.post.save()
    
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_count_query(self):
        qs = Post.objects.all()
        self.assertEqual(qs.count(), 1)
        self.assertTrue(qs.exists())
    
    def test_url_name_list_view(self):
        self.view = resolve('/')
        self.assertEqual(self.view.url_name, 'post')
    
    def test_template_use_dashboard(self):
        self.assertTemplateUsed(self.response, 'landing/base.html')
    
    def test_title_in_queryset(self):
        qs = Post.objects.get(status=1, published_at__lte =timezone.now() )
        self.assertIn("Django", qs.content)
    
    def tearDown(self):
        print("Done..")
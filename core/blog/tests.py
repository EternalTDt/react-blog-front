from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user_1 = User.objects.create(
            username='test_user1', password='123456789'
        )
        test_post = Post.objects.create(
            category_id=1, title='Post title', excerpt='Post excerpt', 
            content='Post content', slug='post-title', author_id=1, status='published'
        )

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post title')
        self.assertEqual(content, 'Post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post title")
        self.assertEqual(str(cat), "django")
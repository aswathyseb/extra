from django.apps import AppConfig
from django.conf import settings
#from mypage.settings import
from django.db.models.signals import post_migrate, post_save

class Mypage(AppConfig):
    name = 'mypage'

    def ready(self):
        post_migrate.connect(init_accounts, sender=self)
        pass

def init_accounts(sender, **kwargs):

    from django.contrib.auth.models import User
    from mypage.models import Blog
    user = User.objects.filter(email='admin@buddy').first()

    if not user:
        username = 'foobar'
        user = User.objects.create(email='admin@buddy', username=username)

    for blog in Blog.objects.all():
        blog.privacy = Blog.PUBLIC
        blog.save()

    user.set_password(settings.ADMIN_PASS)
    #print("USER created")


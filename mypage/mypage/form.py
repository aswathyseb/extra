from django import forms
from django.conf import settings
from mypage.models import Blog

def get_ip(request):

    ip1 = request.META.get('REMOTE_ADDR', '')
    ip2 = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
    ip = ip1 or ip2 or '0.0.0.0'
    return ip

class LoginForm(forms.Form):

    email = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250, widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):

        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        cleaned_data = self.cleaned_data
        passw = cleaned_data['password']

        if '-' in passw:
            raise forms.ValidationError("Invalid character.")

        self.validate_ip(request=self.request)
        return passw

    def validate_ip(self, request):
        current_ip = get_ip(request)
        print(type(current_ip), settings.ALLOWED_IPS, current_ip in settings.ALLOWED_IPS,  "IP")

        if current_ip not in settings.ALLOWED_IPS:
            raise forms.ValidationError("IP is not allowed to login.")
            # return redirect("/")
            1/0




class Blogform(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.CharField(max_length=1000, widget=forms.Textarea)
    privacy = forms.CharField(widget=forms.Select(choices=Blog.PRIVACY_CHOICES))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(Blogform, self).__init__(*args, **kwargs)

    def save(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data['title']
        content = cleaned_data['content']
        privacy = cleaned_data['privacy']
        author = self.user if self.user.is_authenticated else None

        blog = Blog.objects.create(title=title, content=content,
                                   author=author, privacy = privacy)
        return blog


# class Blogform(forms.Form):
#     title = forms.CharField(max_length=250)
#     content = forms.CharField(max_length=1000, widget=forms.Textarea)
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super(BlogForm, self).__init__(*args, **kwargs)
#
#     def save(self):
#         cleaned_data = self.cleaned_data
#         title = cleaned_data['title']
#         content = cleaned_data['content']
#
#         author = self.user if self.user.is_authenticated else None
#         blog = Blog.objects.create(title=title, content=content,
#                                    author=author)
#         return blog
#
#     def clean_blog_text(self):
#         cleaned_data = super(BlogForm, self).clean()
#         content = cleaned_data['content']

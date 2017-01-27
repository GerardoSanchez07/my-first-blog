from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
# Create your views here.
def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def djangoData(request):
    posts = "HOLAa"
    print (posts)

    if request.method=="POST":
        usern = request.POST['user']
        password = request.POST['password']
        print usern
        print password

    return render(request, 'blog/templete.html', {'posts': posts})
    
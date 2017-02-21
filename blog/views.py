from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
# Create your views here.
@csrf_exempt
def post_list(request):
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method=="POST":
        usern = request.POST['Name']
        password = request.POST['Pass']
    return render(request, 'blog/post_list.html', {'posts': posts})


def djangoData(request):
    
    posts = "HOLAa..."
    print (posts)
    return render(request, 'blog/templete.html', {'posts': posts})
    
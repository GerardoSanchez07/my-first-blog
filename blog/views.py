from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):

	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


@csrf_exempt
def androidLogin(request):
	if request.method=='POST':
		print "begin"
        print request.body
        json_data  = json.loads(request.body())
        print json_data['name']
        print json_data['id']
        username = json_data['name']
        password = json_data['id']
        email = json_data['email']
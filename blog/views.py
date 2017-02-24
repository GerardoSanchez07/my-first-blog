from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
# Create your views here.
@csrf_exempt
def post_list(request):
    pts = "HI..."
    use = ""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print ('Hello')

    print ('RECEIVED REQUEST: ' + request.method)

    if request.method == 'POST':
        use = "POST REQUEST"
        name = request.body['name']
        country = request.POST['country']

    use = "no request"
    ctx = {'use': use, 'pts': pts, 'posts':posts }
    return render_to_response('blog/post_list.html', ctx, context_instance = RequestContext(request))


def djangoData(request):
    
    posts = "HOLAa..."
    print (posts)
    return render(request, 'blog/templete.html', {'posts': posts})
    

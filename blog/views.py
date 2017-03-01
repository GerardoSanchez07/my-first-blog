from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.shortcuts import render
from django.utils import timezone
from .models import Plublish, Post
import json

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

        received_json_data=request.POST['req']
        print(received_json_data)

        json_obj = json.loads( received_json_data)
        name =  (json_obj['name'])
        age = (json_obj['age'])
        value = (json_obj['value'])
        num = (json_obj['num'])

        p = Plublish(
            namep = name , agep = age,
            valuep = value, nump = num 
        )
        p.save()

        objects =  Plublish.objects.all()
        print objects

    ctx = {'use': use, 'pts': pts, 'posts':posts }
    return render_to_response('blog/post_list.html', ctx, context_instance = RequestContext(request))


def djangoData(request):
    
    posts = "HOLAa..."
    print (posts)
    return render(request, 'blog/templete.html', {'posts': posts})
    

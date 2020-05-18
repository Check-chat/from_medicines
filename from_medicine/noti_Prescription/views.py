from django.shortcuts import render

# Create your views here.
def index(request):
    notiPost = Post.objects.all()
    context = {
            'posts' : notiPost,
        }
    return render(request, 'index.html', context)
from django.shortcuts import render

posts = [
    {
        'author':'Me',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'wrz 25'
    },
    {
        'author':'you',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'wrz 26'
    }    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

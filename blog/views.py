from django.shortcuts import render
from blog.models import Post

def post_list(request):
#	import ipdb; ipdb.set_trace();
	
	posts = Post.objects.filter(author=request.user)

	return render(
		request, 
		'blog/post_list.html', 
		{
			'posts': posts
		})


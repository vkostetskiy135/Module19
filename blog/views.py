from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    items_per_page = request.GET.get('items_per_page', '5')

    paginator = Paginator(post_list, int(items_per_page))
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page
    })

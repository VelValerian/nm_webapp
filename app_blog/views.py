from django.shortcuts import render

from django.shortcuts import render

def post_list(request):
    posts = [
        {"title": "Первая статья", "slug": "pervaya", "excerpt": "Коротко о главном…"},
        {"title": "Вторая статья", "slug": "vtoraya", "excerpt": "Еще немного текста…"},
    ]
    return render(request, "blog/list.html", {"posts": posts})

def post_detail(request, slug):
    post = {"title": f"Статья: {slug}", "slug": slug, "content": "Текст статьи…"}
    return render(request, "blog/detail.html", {"post": post})

from django.shortcuts import render

from django.shortcuts import render

def training_list(request):
    # Временный контент (станет QuerySet'ом позже)
    items = [
        {"title": "Индивидуальная тренировка", "slug": "individual"},
        {"title": "Тренировка в мини группе", "slug": "mini-groupe"},
        {"title": "Онлайн тренировка", "slug": "online"},
        {"title": "Онлайн консультация", "slug": "consulting"},
    ]
    return render(request, "trainings/list.html", {"items": items})

def training_detail(request, slug):
    # Временная заглушка поиска (позже модель по slug)
    item = {"title": f"Тренировка: {slug}", "slug": slug, "content": "Описание тренировки…"}
    return render(request, "trainings/detail.html", {"item": item})

from types import SimpleNamespace
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Заглушки (будут использованы, если в БД нет записей)
STUB_ITEMS = [
    SimpleNamespace(
        title="Персональная тренировка",
        subtitle="Индивидуальные занятия с тренером для новичков и опытных бегунов.",
        bullets=[
            "Комфортное место и время — приезжаю к тебе.",
            "Индивидуальный подход — учитываю твою специфику.",
            "Прогресс с первых занятий — скорость и выносливость."
        ],
        price=3500,
        duration_min=60,
        img="online-exercise.png",
        slug="personal",
        content="Развёрнутое описание персональной тренировки."
    ),
    SimpleNamespace(
        title="Онлайн-ТРЕНИРОВКИ",
        subtitle="Разбор техники, план, питание, инвентарь.",
        bullets=[
            "Видеосвязь в удобное время.",
            "Подробные рекомендации и план на 4–6 недель."
        ],
        price=1500,
        duration_min=45,
        img="mini-groupe.png",
        slug="online-consult",
        content="Полное описание онлайн-консультации."
    ),
    SimpleNamespace(
        title="ГРУПОВАЯ тренировка",
        subtitle="Индивидуальные занятия с тренером для новичков и опытных бегунов.",
        bullets=[
            "Комфортное место и время — приезжаю к тебе.",
            "Индивидуальный подход — учитываю твою специфику.",
            "Прогресс с первых занятий — скорость и выносливость."
        ],
        price=3500,
        duration_min=60,
        img="online-exercise.png",
        slug="personal",
        content="Развёрнутое описание персональной тренировки."
    ),
    SimpleNamespace(
        title="МИНИ-ГРУППА",
        subtitle="Индивидуальные занятия с тренером для новичков и опытных бегунов.",
        bullets=[
            "Комфортное место и время — приезжаю к тебе.",
            "Индивидуальный подход — учитываю твою специфику.",
            "Прогресс с первых занятий — скорость и выносливость."
        ],
        price=3500,
        duration_min=60,
        img="online-exercise.png",
        slug="personal",
        content="Развёрнутое описание персональной тренировки."
    ),
]

def _db_items_or_stub():
    """
    Если модель Training есть и в ней есть записи — отдаём их.
    Иначе возвращаем заглушки.
    """
    try:
        from .models import Training
        qs = Training.objects.all()
        if qs.exists():
            return [
                SimpleNamespace(
                    title=o.title,
                    subtitle=o.subtitle,
                    bullets=o.bullets or [],
                    price=o.price,
                    duration_min=o.duration_min,
                    slug=o.slug,
                    content=o.content,
                )
                for o in qs
            ]
    except Exception:
        pass
    return STUB_ITEMS

def _find_in(items, slug):
    for it in items:
        if it.slug == slug:
            return it
    return None

def list_view(request):
    items = _db_items_or_stub()
    return render(request, "page/training-total.html", {"items": items})

def page_view(request, slug):
    items = _db_items_or_stub()
    obj = _find_in(items, slug)
    if not obj:
        raise Http404("Тренировка не найдена")
    return render(request, "page/training-page.html", {"obj": obj})
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Item  # your model

def item_list(request):
    query = request.GET.get("q", "").strip()

    # 1) Filter by search
    if query:
        objects = Item.objects.filter(name__icontains=query)
    else:
        objects = Item.objects.all()

    # 2) Paginate the filtered queryset
    paginator = Paginator(objects, 10)  # 10 per page
    page_number = request.GET.get("page")

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "page_obj": page_obj,
        "query": query,
    }
    return render(request, "items/item_list.html", context)

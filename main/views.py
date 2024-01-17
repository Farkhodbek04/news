from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import models


# front
def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def contact(request):
    if request.method == 'POST':
        models.Form.objects.create(
            body=request.POST['body'],
            name = request.POST['name'],
            email = request.POST['email']
        )
        return redirect('index')
    return render(request, 'front/contact.html')


def news(request):

    category_id = request.GET.get('category_id')
    categorys = models.Category.objects.all().order_by('name')

    if category_id:
        category = models.Category.objects.get(id=category_id)
        news = models.Item.objects.filter(category=category, is_active=True)
        status = category
    else:
        status = 0
        news = models.Item.objects.filter(is_active=True)

    context = {
        'news':news,
        'categorys':categorys,
        'status':status
    }
    return render(request, 'front/news.html', context)
# dashboard

def dashboard(request):
    users = User.objects.all().count()
    news = models.Item.objects.filter(is_active=True).count()
    regions = models.Region.objects.all().count()
    category = models.Category.objects.all().count()

    context = {
        'users':users,
        'news':news,
        'regions':regions,
        'category':category
    }

    return render(request, 'dashboard/index.html', context)


def create_region(request):
    if request.method == 'POST':
        models.Region.objects.create(
            name=request.POST['name']
        )
        return redirect('regions')
    return render(request, 'dashboard/region/create.html')


def regions(request):
    regions = models.Region.objects.all()
    return render(request, 'dashboard/region/list.html', {'regions':regions})



def region_update(request, id):
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        region.name = request.POST['name']
        region.save()
        return redirect('regions')
    return render(request, 'dashboard/region/update.html', {'region':region})


def region_delete(request, id):
    models.Region.objects.get(id=id).delete()
    return redirect('regions')

# Category

def categories(request):
    categories = models.Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categories': categories})

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def create_category(request):
    if request.method == 'POST' and request.POST['name']:
        models.Category.objects.create(
            name = request.POST['name']
        )
        return redirect('categories')
    return render(request, 'dashboard/category/create.html')
    
def update_category(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('categories')
    return render(request, 'dashboard/category/update.html', {'category': category})

def delete_category(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('categories')

# Items

def create_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        image = request.FILES['image']
        category = models.Category.objects.get(id=request.POST['category_id'])
        region = models.Region.objects.get(id=request.POST['region_id'])
        models.Item.objects.create(
            title = title,
            body = body,
            image = image,
            category = category,
            region = region
        )
        return redirect("items")
    context = {
        'regions': models.Region.objects.all(),
        'categories': models.Category.objects.all()
    }
    return render(request, 'dashboard/items/create.html', context)

def items(request):
    items = models.Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'dashboard/items/list.html', context)

def update_item(request, id):
    item = models.Item.objects.get(id = id)
    if request.method == 'POST':
        item.category = models.Category.objects.get(id = request.POST['category_id'])
        item.region = models.Region.objects.get(id=request.POST['region_id'])
        item.title = request.POST['title']
        item.body = request.POST['body']
        image = request.FILES.get('image')
        if image:
            item.image = image
        item.save()
        return redirect('items')

    context = {
        'categories': models.Category.objects.all(),
        'item': item,
        'regions': models.Region.objects.all()
    }
    return render(request, 'dashboard/items/update.html', context)

def delete_item(request, id):
    models.Item.objects.get(id=id).delete()
    return redirect('items')

# Murojatlar

def applications(request):
    applications = models.Form.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'dashboard/applications/list.html', context)

# def application_detail(request):
#     if request.method == "POST":
#         name = models.Form.objects.get('name')
#         body = models.Form.objects.get('body')
#         email = models.Form.objects.get('email')
#         created = models.Form.objects.get('created')
#         is_checked = models.Form.objects.get('status')
#     context = {
#         'name':name,
#         'body':body,
#         'email':email,
#         'created':created,
#         'is_checked':is_checked
#     }
#     return render(request, 'dashboard/applications/detail.html', context)

def update_checked(request, id):
    applications = models.Form.objects.all(id=id)
    is_checked = models.Form.objects.get('status')
    if is_checked:
        applications.is_checked = models.Form.objects.get('status')
        applications.save()
        return redirect('applications')
    return render(request,'dashboard/applications/details.html', {'applications':applications})


    



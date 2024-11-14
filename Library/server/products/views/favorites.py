from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from products.models import Product

def favorites_list(request):
    context = {}
    if not request.session.get('favorites'):
        request.session['favorites'] = list()
    else:
        request.session['favorites'] = list(request.session['favorites'])
    favs = request.session['favorites']
    products = []
    for fav in favs:
        item = Product.objects.get(pk=fav)
        if not item in products:
            products.append(item)
    context['favorites'] = favs
    context['object_list1'] = products
    return render(request, 'favorites/favorites.html', context=context)

def add_to_favorites(request):
    data = dict()
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])
        request.session['favorites'].append(request.POST.get('id'))
        request.session.modified = True
        data["id"] = request.POST.get('id')
        data["ses"] = request.session['favorites']
        return JsonResponse(data)
    else:
        return JsonResponse(data)
def remove_from_favorites(request):
    data = dict()
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item != request.POST.get('id'):
                item.clear()
        request.session.modified = True
        data["ses"] = request.session['favorites']
        if request.is_ajax():
            data = {
                'id': request.POST.get('id'),
            }
            request.session.modified = True
            return JsonResponse(data)
    else:
        return JsonResponse(data)
'''def remove_from_favorites(request):
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item['id'] == request.POST.get('id'):
                item.clear()
        while {} in request.session['favorites']:
            request.session['favorites'].remove({})
        if not request.session['favorites']:
            del request.session['favorites']
        request.session.modified = True
        if request.is_ajax():
            data = {
                'id':request.POST.get('id'),
            }
            request.session.modified = True
            return JsonResponse(data)
    return redirect(request.POST.get('url_form'))'''

def favorites_api(request):
    return JsonResponse(request.session.get('favorites'), safe = False)
from django.http import JsonResponse
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from products.models import Product, ProductCategory
from products.forms import ProductModelForm

from django.core.files.storage import FileSystemStorage




class ProductList(ListView):
    model = Product
    template_name = 'products/index.html'
    paginate_by = 9


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().name
        context['link_list'] = ['products/css/product.css']
        context['menu'] = ProductCategory.objects.all()

        return context


class ProductCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    success_url = reverse_lazy('products:main')
    login_url = reverse_lazy('accounts:login')

    form_class = ProductModelForm
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser


class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('products:main')
    login_url = reverse_lazy('accounts:login')

    form_class = ProductModelForm
    template_name = 'products/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:main')
    login_url = reverse_lazy('accounts:login')

    template_name = 'products/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление продукта'
        context['link_list'] = ['server/css/crud.css']
        context['menu'] = ProductCategory.objects.all()

        return context

    def test_func(self):
        return self.request.user.is_superuser


def product_rest_list():
    object_list = Product.objects.all()
    data = []

    for itm in object_list:
        data.append(
            {
                'id': itm.id,
                'name': itm.name,
                'image_url': itm.image.url if itm.image else None,
                'status': itm.status
            }
        )

    return JsonResponse({'results': data})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
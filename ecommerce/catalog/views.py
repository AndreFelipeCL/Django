# coding=utf-8

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic


class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3


product_list = ProductListView.as_view()


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    paginate_by = 3


    def get_queryset(self):
        """ Implementação de uma queryset customizável para retornoar os objetos de acordo com o slug. """
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """ Implementação para adicionarmos variaveis ao nosso context. """

        # Invocando o comportamento padrão da classe pai.
        context = super(CategoryListView, self).get_context_data(**kwargs)
        # Adicionando a category de acordo com seu slug ao contexto da view.
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def product(request, slug):
    context = {
        'product': Product.objects.get(slug=slug),
    }
    return render(request, 'catalog/product.html', context)

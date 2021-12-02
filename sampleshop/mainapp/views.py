from django.views.generic import ListView
from .models import Good, Category


class GoodsListView(ListView):
    model = Good
    template_name = 'mainapp/goods_list.html'

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Good.objects.all().prefetch_related('category').filter(category=self.kwargs['pk'])
        else:
            return Good.objects.all().prefetch_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'список товаров'
        context['categories'] = Category.objects.all()
        return context

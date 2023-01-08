from .models import Category

menu = [
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Разместить объявление', 'url_name': 'add_cnc'}
    ]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
            context = kwargs
            cats = Category.objects.all()
            context['menu'] = menu
            context['cats'] = cats
            if 'cat_selected' not in context:
                    context['cat_selected'] = 0
            return context


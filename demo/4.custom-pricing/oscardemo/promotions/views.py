from oscar.apps.promotions.views import HomeView as OscarHomeView
from oscar.core.loading import get_model

Category = get_model('catalogue', 'Category')


class HomeView(OscarHomeView):

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all()
        })
        return context

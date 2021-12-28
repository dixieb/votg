from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'criminals'

urlpatterns = [
    # /criminals
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /persons-of-interest
    url(r'^persons_of_interest$', views.persons_of_interest, name='persons_of_interest'),

    # /criminals/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /criminal/71/add
    url(r'^add/$', views.NoteCreateView.as_view(), name='note-add'),
    # url(r'^new-note/$', views.NoteCreateView.as_view(), name='new-note'),

    # /search_result
    url(r'^search_results$', views.SearchResults.as_view(), name='search-result'),

    # /thanks
    # url(r'^thanks$', views.thanks, name='thanks'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


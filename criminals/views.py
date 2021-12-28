from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView
from .models import Person, Desc, Offence, Report
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NoteForm
from bootstrap_modal_forms.generic import BSModalCreateView
import datetime

class IndexView(generic.ListView):
    template_name = 'criminals/index.html'
    context_object_name = 'all_persons'

    def get_queryset(self):
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = Person
    template_name = 'criminals/pages/details.html'

class SearchResults(generic.ListView):
    model = Person
    template_name = 'criminals/pages/search_results.html'
    context_object_name = 'search_db'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(firstName__startswith=query) |
            Q(lastName__startswith=query) |
            Q(dob__startswith=query) |
            Q(city__startswith=query) |
            Q(alias__startswith=query)
        )
        return object_list

class NoteCreateView(BSModalCreateView):
    template_name = 'criminals/report_form.html'
    form_class = NoteForm
    success_message = 'Success! Note was added.'
    success_url = reverse_lazy('criminals:persons_of_interest')


class ReportCreate(CreateView):
    model = Report
    fields = ['notes']

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()


def persons_of_interest(request):
    person = Person.objects.all()
    desc = Desc.objects.all()
    offence = Offence.objects.all()
    report = Report.objects.all()
    page = request.GET.get('page', 1)
    context = {
        'all_persons': person,
        'desc': desc,
        'offence': offence,
        'report': report
    }

    paginator = Paginator(person, 12)
    try:
        person = paginator.page(page)
    except PageNotAnInteger:
        person = paginator.page(1)
    except EmptyPage:
        person = paginator.page(paginator.num_pages)

    return render(request, 'criminals/pages/persons_of_interest.html', context=context)

# def note(request):
#     if request.method == 'POST':
#         form = ReportForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('criminals/pages/details.html')
#         else:
#             form = ReportForm()
#
#         return render(request, 'details.html', {'form': form})
#
# def thanks(request):
#     return render(request, 'criminals/thanks.html')

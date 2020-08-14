from django.shortcuts import render

from cbv import models

#all View module for class
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

#reverse_lazy module for reverse one page to success page
from django.urls import reverse_lazy


#function based view
# def index(request):
#     diction = {
#         'title': 'HOME | CBV'
#     }
    # return render(request, 'cbv/index.html', context=diction)

#class based view
# class IndexView(View):
#     def get(self, request):
#         diction = {
#             'title': 'HOME | CBV'
#         }
#         return render(request, 'cbv/index.html', context=diction)

#class based view with template in app
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home | CBV"
        context['text']="Musician List"
        return context


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'cbv/musician_details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Musician Details | CBV"
        context['text']="Musician Details"
        return context

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'cbv/musician_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "ADD Musician | CBV"
        context['text']="Add Musician"
        return context

class UpdateMusician(UpdateView):
    fields = ('first_name', 'instrument')
    model = models.Musician
    template_name = 'cbv/musician_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Musician | CBV"
        context['text']="Update Musician"
        return context

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('cbv:Home')
    template_name = 'cbv/musician_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Musician | CBV"
        context['text']="Delete Musician"
        return context

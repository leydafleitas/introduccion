from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    #args y kwargs hacen referencia a cualquier variable o parametro que el objeto del request que estemos llamando pueda tener
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html',context)
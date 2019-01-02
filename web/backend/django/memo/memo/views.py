from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Memo


class MemoList(ListView) :    
    model = Memo
    context_object_name = 'memo_list'
    queryset = Memo.objects.order_by('-last_modified')[:5]
    template_name = 'memo/index.html'


class MemoDetail(DetailView) :
    model = Memo      
    # context_object_name = 'object'   # your own name for the list as a template variable
    # queryset = Memo.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  #

    # def index(self, request, memo_id):
    #     memo = Memo.objects.order_by('-last_modified')[:5]
    #     context = {'object': memo}
    #     return render(request, 'memo/detail.html', context)
from django.urls import path, include
from .views import MemoList, MemoDetail


urlpatterns = [
    path('', MemoList.as_view(), name='index'),
    path('<int:memo_id>', MemoDetail.as_view(), name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('qna_list/', views.qna_list_view, name='qna_list'), 
    path('qna/create/', views.qna_create_view, name='qna-create'), 
    path('qna/detail/<int:pk>/', views.qna_detail_view, name='qna-detail'),
    path('qna/delete/<int:pk>/', views.qna_delete_view, name='qna-delete')
]



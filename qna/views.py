from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QnaModel
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_http_methods

#====사용자 인증 여부에 따라 홈페이지 또는 문의 페이지로 이동하는 코드====
def home(request):
    user = request.user.is_authenticated  
    # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/qna_list')
    else:
        return redirect('/signin')

#=======등록된 문의리스트를 볼 수 있는 view========
# @login_required
# class QnaListView(ListView):
#     qna = QnaModel
#     paginate_by = 10
#     template_name = 'qna/qna_list.html'
#     context_object_name = 'qna_list'
#     def get_queryset(self):
#       qna_list = QnaModel.objects.order_by('-id')
#       return qna_list


def qna_list_view(request):
    if request.method == 'GET': #GET메소드로 요청 들어 올 경우
        all_qna = QnaModel.objects.all().order_by('-created_at') #등록 역순으로 불러오기 
        return render(request, 'qna/qna_list.html', {'allqna': all_qna}) 

#==============문의글 등록 view==============
@login_required
def qna_create_view(request):
    if request.method == 'GET': #GET메소드로 요청 들어 올 경우
        return render(request, 'qna/qna_create.html')
    if request.method == 'POST':  # 요청 방식이 POST 일때 
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_qna = QnaModel()  # 문의글 등록 모델 가져오기
        my_qna.author = user  # 모델에 사용자 저장
        
        #각 데이터모델 필드에 입력 받은 값 저장
        my_qna.title =  request.POST.get('title', '') 
        my_qna.content = request.POST.get('content', '') 
        my_qna.save()
        return redirect('/qna_list') 


#=======문의글 상세페이지 view========
@login_required
def qna_detail_view(request, pk):
    post = get_object_or_404(QnaModel, pk=pk)
    if request.method == "GET":
      context = {
          'post' : post, 
      }
      return render(request, 'qna/qna_detail.html', context)
    if request.method == "POST":
      post.title = request.POST['inputValue']
      post.content = request.POST['inputcontent']
      post.save()
      return redirect('/qna/detail/'+ str(post.pk) +'/')
    
    
#========문의글 삭제 view===========
def qna_delete_view(request, pk):
  if request.method == "POST":
    post = get_object_or_404(QnaModel, pk=pk)
    post.delete()
    return redirect('/qna_list')


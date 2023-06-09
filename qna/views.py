from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QnaModel
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# ====사용자 인증 여부에 따라 홈페이지 또는 문의 페이지로 이동하는 코드====


def home(request):
    user = request.user.is_authenticated
    # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/main')
    else:
        return redirect('/signin')


def qna_list_view(request):
    if request.method == 'GET':  # GET메소드로 요청 들어 올 경우
        all_qna = QnaModel.objects.all().order_by(
            '-qna_created_at')  # QnaModel의 모든 객체 등록 역순으로 불러오기

        # 'Paginator'클래스를 이용하여 페이지네이션 객체 생성
        paginator = Paginator(all_qna, 10)  # all_qna에 저장된 객체들을 10개씩 나눔
        # GET 파라미터로 'page'가 전달됨
        page = request.GET.get('page')

        try:  # 현재 보여줄 페이지에 해당하는 QnaModel 객체들을 가져와 qna_list에 저장
            qna_list = paginator.page(page)
        except PageNotAnInteger:  # 'page'값이 없는 경우 'PageNotAnInteger' 예외 발생
            qna_list = paginator.page(1)  # 1페이지 보여주기
        except EmptyPage:  # 'page'값에 임의의 값을 입력하여 요청하였을 때, 현재 페이지 범위를 초과하는 경우
            qna_list = paginator.page(paginator.num_pages)  # 마지막 페이지 보여주기

        return render(request, 'qna/qna_list.html', {'allqna': qna_list})


# ==============문의글 등록 view==============
@login_required
def qna_create_view(request):
    if request.method == 'GET':  # GET메소드로 요청 들어 올 경우
        return render(request, 'qna/qna_create.html')
    if request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_qna = QnaModel()  # 문의글 등록 모델 가져오기
        my_qna.client = user  # 모델에 사용자 저장

        # 각 데이터모델 필드에 입력 받은 값 저장
        my_qna.qna_title = request.POST.get('title', '')
        my_qna.qna_content = request.POST.get('content', '')
        my_qna.save()
        # mypage추가
        my_qna.mypage_key.add(request.user.id)
        return redirect('/qna_list')


# =======문의글 상세페이지 view========
@login_required
def qna_detail_view(request, pk):
    post = get_object_or_404(QnaModel, pk=pk)
    if request.method == "GET":
        context = {
            'post': post,
        }
    return render(request, 'qna/qna_detail.html', context)


# =========문의글 수정 view=============
@login_required
def qna_edit_view(request, pk):
    post = get_object_or_404(QnaModel, pk=pk)
    if request.method == "GET":
        context = {
            'post': post,
        }
        return render(request, 'qna/qna_update.html', context)
    if request.method == "POST":
        post.qna_title = request.POST['inputValue']
        post.qna_content = request.POST['inputcontent']
        post.save()
        return redirect('/qna_list')
        # return redirect('/qna/edit/'+ str(post.pk) +'/')


# ========문의글 삭제 view===========
@login_required
def qna_delete_view(request, pk):
    if request.method == "POST":
        post = get_object_or_404(QnaModel, pk=pk)
        post.delete()
        return redirect('/qna_list')
    else:  # GET 요청일 경우
        return render(request, 'qna/qna_update.html')
# 요청이 GET이면 render, POST요청이면 delete

from django.urls import path
from .views import *

app_name="main"
urlpatterns=[
    path('', mainpage, name="mainpage"), #메인페이지
    path('competition/', competition, name="competition"), #팀원구하기페이지
    path('free/', free, name="free"), #자유협력페이지
    path('<str:id>',detail,name="detail"), #자유협력 상세페이지
    path('<str:id>',cetail, name="cetail"), #팀원구하기 상세페이지
    path('dnew/',dnew,name="dnew"), #자유협력 글쓰기
    path('dcreate/',dcreate, name="dcreate"),
    path('cnew/',cnew,name="cnew"), #팀원구하기 글쓰기
    path('ccreate/',ccreate, name="ccreate"),
    



]
"""bigdatawork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views


urlpatterns = [
    # path("admin/", views.add),
    path('index_first/', views.index_first, name="index_first"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('notebook/', views.notebook, name="notebook"),
    path('article/', views.article_page, name="article_page"),
    path('add/', views.add,name="add"),
    path('search/', views.search),
    path('delete/', views.delete),
    path('update_page/', views.update_page),
    path('school/', views.school,name="school"),
    path('three/', views.three,name="three"),
    path('jieyouzahuopu/', views.jieyouzahuopu, name="jieyouzahuopu"),
    path('buguanjiaodeyongqi/', views.buguanjiaodeyongqi, name="buguanjiaodeyongqi"),
    path('beitaoyandeyongqi/', views.beitaoyandeyongqi, name="beitaoyandeyongqi"),
    path('wocongweirucijuanlianrenjian/', views.wocongweirucijuanlianrenjian, name="wocongweirucijuanlianrenjian"),
    path('zhaohuaxishi/', views.zhaohuaxishi, name="zhaohuaxishi"),
    path('xianyinumashaonianshi2/', views.xianyinumashaonianshi2, name="xianyinumashaonianshi2"),
    path('waerdenghu/', views.waerdenghu, name="waerdenghu"),
    path('kuangrenriji/', views.kuangrenriji, name="kuangrenriji"),
    path('huangdineijing/', views.huangdineijing, name="huangdineijing"),
    path('dicengluoji/', views.dicengluoji, name="dicengluoji"),
    path('liaobuqidehulibaba/', views.liaobuqidehulibaba,name="liaobuqidehulibaba"),
    path('wuhezhizhong/', views.wuhezhizhong,name="wuhezhizhong"),
    path('zhongguogudaishenhua/', views.zhongguogudaishenhua,name="zhongguogudaishenhua"),
    path('naxiebuweirenzhidegushi/', views.naxiebuweirenzhidegushi, name="naxiebuweirenzhidegushi"),
    path('tazaiyunzhinan/', views.tazaiyunzhinan,name="tazaiyunzhinan"),
    path('baisedeganlanshu/', views.baisedeganlanshu,name="baisedeganlanshu"),
    path('renyuxianluo/', views.renyuxianluo,name="renyuxianluo"),
    path('bairimengwo/', views.bairimengwo,name="bairimengwo"),
    path('tazuiyele/', views.tazuiyele,name="tazuiyele"),
    path('weizhuangxuezha/', views.weizhuangxuezha,name="weizhuangxuezha"),
    path('angelidemimi/', views.angelidemimi,name="angelidemimi"),
    path('yiniweimingdexiatian/', views.yiniweimingdexiatian,name="yiniweimingdexiatian"),
    path('nibuxiangrenheren/', views.nibuxiangrenheren,name="nibuxiangrenheren"),
    path('toutoucangbuzhu/', views.toutoucangbuzhu,name="toutoucangbuzhu"),
    path('yigenvhaidexinlingshi/', views.yigenvhaidexinlingshi,name="yigenvhaidexinlingshi"),
    path('cangxia/', views.cangxia,name="cangxia"),
    path('dangwofeibenxiangni/', views.dangwofeibenxiangni,name="dangwofeibenxiangni"),
]

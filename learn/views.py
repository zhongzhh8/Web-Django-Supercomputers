# coding=utf-8
import json
from django.shortcuts import render

# Create your views here.

# coding:utf-8



from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from learn.GetNetData import getNetData


def home(request):
    return render(request, 'home.html') #,{"iframe_url": "origin_main"}

def intro(request):
    return render(request, 'intro.html', )

def main(request):
    return render(request, 'main.html',{"iframe_url": "/intro"})

def origin_main(request):
    return render(request, 'origin_main.html')

def index(request):
    return render(request, 'home.html')
    # return HttpResponse(u"欢迎光临 自强学堂!")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def monitor_data_page(request):
    return render(request, 'origin_main.html')

def get_heatmap(request):
    return render(request, 'heatmap-map.html')

def NetDataPage(request):
    disease = request.GET.get('disease')
    print('disease0=', disease)
    return render(request, 'main.html', {"iframe_url": "/showdata?disease="+disease})

def showdata(request):
    disease = request.GET.get('disease')
    print('disease1=', disease)

    key_list, value_list = getNetData(disease)
    # print('value_list=',value_list)
    # print('key_list,value_list=',key_list ,value_list)

    #在这里根据不同的疾病名字，获取对应的数据，传到js文件中展示出来
    # if disease=='LiuGan':
    #     xList= ["流感","感冒","咳嗽","发烧","不舒服","孩子"
    #         ,"妈妈","潮湿","宝宝","疫苗","病毒","高发期",
    #         "接种","广东","板蓝根","请假","吃药","持续很久","看医生"]
    #     yList=[9861, 6181, 4386, 4055, 2467, 2244,1898,1484,965,847,5820,555,550,462,366,360,2820,273,2650]

    xList=key_list
    yList=value_list
    return render(request, 'showdata.html',{'disease': json.dumps(disease),
                                            'xList': json.dumps(xList),
                                            'yList': json.dumps(yList),} )


def R_code_page(request):
    return render(request, 'main.html', {"iframe_url": 'http://127.0.0.1:3973'})
    # robjects.r.source('plot_demo.r')

    # r = robjects.r
    # # 调用R-script --- r.source('path/R-script.R')
    # r.source('static/R-script_1.R')
    # # r.source('R-script_2.R')
    # # 使用R-script
    # ### 调用自定义Test函数
    # r.Test()
    # ### 调用自定义Test1函数
    # r.Test1()
    # result_test1 = r.Test1(4)
    # print(result_test1)
    # print(result_test1[0])
    # ### 调用自定义fun_normal函数
    # sample_size = 10
    # mean_value = 0
    # sd_value = 1
    # decimal_places = 4
    # result_normal = r.fun_normal(sample_size, mean_value, sd_value, decimal_places)
    #
    # print('is it ok????????????????????????????')
    # pi = robjects.r('pi')
    # print(pi)



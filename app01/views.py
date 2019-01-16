from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    # 往数据库表中插入数据
    # book_list=[]
    # for i in range(100):
    #     book_obj = Book(title="Book_%s"%i,price=i*i)
    #     book_list.append(book_obj)
    # Book.objects.bulk_create(book_list)
    # Book_all = Book.objects.all()
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 5)
    c_page = request.GET.get("page", 1)
    currentPage = int(c_page)
    # print("count", paginator.count) 数据总数
    # print("num_pages", paginator.num_pages) 总页数
    # print("page_range", paginator.page_range) 页码的列表

    if paginator.num_pages > 10:
        if currentPage - 5 < 1:
            pageRange = range(1, 11)
        elif currentPage + 5 > paginator.num_pages:
            pageRange = range(currentPage - 5, paginator.num_pages + 1)
        else:
            pageRange = range(currentPage - 5, currentPage + 5)
    else:
        pageRange = paginator.page_range
    try:
        page = paginator.page(c_page)
    except:
        page = paginator.page(1) #第一页的page对象
        # print(page.has_next())  #是否有下一页
        # print(page.next_page_number()) #下一页页码
        # print(page.has_previous()) #是否有上一页
        # print(page.previous_page_number()) #上一页页码

    return render(request,"index.html",{"page":page,"paginator":paginator,"c_page":int(c_page),"pageRange":pageRange})
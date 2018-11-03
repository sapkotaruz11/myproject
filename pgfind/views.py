# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
from .models import PG
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    all_pg = PG.objects.all()
    return render(request,'base.html',{ 'all_pg': all_pg})


def AddPG(request):
    if request.method == 'POST':
        # print(request.FILES['myfile'])
        pg_name = request.POST.get('pg_name')
        owner_name = request.POST.get('owner_name','')
        owner_phone = request.POST.get('owner_phone','')
        pg_price = request.POST.get('pg_price','')
        pg_descp = request.POST.get('pg_descp','')
        latitude = request.POST.get('latitude','')
        longitude = request.POST.get('longitude','')
        loc_area = request.POST.get('loc_area','')
        loc_street = request.POST.get('loc_street','')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)

        image = uploaded_file_url
        new_pg=PG(pg_name=pg_name,owner_name=owner_name,owner_phone=owner_phone,pg_price=pg_price,pg_descp=pg_descp,image=image,latitude=latitude,longitude=longitude,loc_area=loc_area,loc_street=loc_street)
        new_pg.save()

        return render(request,'redirect.html')
    else:
        return render(request,'form.html')

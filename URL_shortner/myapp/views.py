from django.shortcuts import render, redirect
from django.http import  HttpResponse
# import to use model for CRUD operations
from .models import LongToShort
# Create your views here.
def helloworld(request):
    return HttpResponse("Hello world")

# HOME PAGE GET REQUEST
def home_page(request):
    context = {
        'submitted': False,
        'error': False
    }  
    if request.method == 'POST':
        data = request.POST
        long_url = data['longurl']
        custom_name = data['custom_name']
        
        try:
            # CREATE operation in database but using object (ORM)
            obj = LongToShort(long_url = long_url, short_url = custom_name)
            obj.save()
            
            # READ
            date = obj.date
            clicks = obj.clicks
            time = obj.time
            
            context['long_url'] = long_url
            context['short_url'] = request.build_absolute_uri() + custom_name
            context['date'] = date
            context['clicks'] = clicks
            context['submitted'] = True
            context['time'] = time
        except:
            context['error'] = True
        
    # else:
    #     print('No data is being received')
    return render(request, "index.html", context)

# REDIRECTING TO THE WEBSITE
def redirect_url(request, short_url):
    row = LongToShort.objects.filter(short_url = short_url)
    if(len(row)==0):
        print('No such URL exists')
        return HttpResponse('No such URL exists')
    
    obj = row[0]
    long_url = obj.long_url
    
    #UPDATE and save it to db
    obj.clicks = obj.clicks + 1
    obj.save()
    
    # return HttpResponse(long_url)
    return redirect(long_url)

# ANALYTICS PAGE 
def analytics(request):
    rows = LongToShort.objects.all();
    context ={
        'rows': rows
    }
    return render(request, "all-analytics.html", context)
    
    
    

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challanges={
    'jan':'jan',
    'feb':'feb',
    'march':'march',
    'april':'april',
    'may':'may',
    'june':'june',
    'july':'july',
    'august':'august',
    'september':'september',
    'october':'october',
    'november':'november',
    'december':None,
}

def month_by_number(request,month):
    months=list(monthly_challanges.keys())
    if month>len(months):
        return HttpResponseNotFound('not found')
    redirect_month=months[month-1]
    redirect_path=reverse('monthly_challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challange(request,month):
    try:
        text=monthly_challanges[month]
        return render(request,'challenges/challenge.html',{
            'text':text,
            'm':month,
        })
    except:
        return HttpResponseNotFound('Not Found')
    
def index(request):
    list_items=''
    months=list(monthly_challanges.keys())
    
    return render(request,'challenges/index.html',{
        'months':months,})
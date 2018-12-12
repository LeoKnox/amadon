from django.shortcuts import render, HttpResponse, redirect
from .models import Shop

def index(request):
    context = {
        "fill":Shop.objects.all()
    }
    return render(request, "amadon_app/index.html", context)

def purchase_redirect(request):

    return render(request, "amadon_app/purchase.html")

def purchase(request):
    products = {
        "1": 19.99,
        "2": 29.99,
        "3": 4.99,
        "4": 49.99
    }
    pid = products[request.POST['id']]
    if 'charge' not in request.session:
        request.session['charge']=0
    request.session['charge'] = float(pid)*float(request.POST["qty"])
    #request.session['total'] = total
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += int(request.POST['qty'])
    if 'total' not in request.session:
        request.session['total'] = 0
    request.session['total'] += request.session['charge']
    return redirect("/purchase_redirect")

# Create your views here.
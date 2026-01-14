from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'food/index.html')

def about(request):
    return render(request, 'food/order.html')
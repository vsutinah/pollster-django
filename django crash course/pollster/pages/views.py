from django.shortcuts import render

# Create your views here.
# Landing page
def index(request):
    return render(request, 'pages/index.html')
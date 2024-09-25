from django.shortcuts import render

# Create your views here.
def project_list(request):
    return render(request, 'content/project_list.html')

def experience_list(request):
    return render(request, 'content/experience_list.html')
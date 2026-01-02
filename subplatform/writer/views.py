from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def writer_dashboard(request):
    return render(request, "writer/writer-dashboard.html")

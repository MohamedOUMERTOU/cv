from django.shortcuts import render, get_object_or_404, redirect
from .models import Project,Exprience,Skill
from .forms import ContactForm

def index(request):
    projects = Project.objects.all()[:3]
    experience = Exprience.objects.all()
    skills = Skill.objects.all()
    for skill in skills:
        skill.stars = [None] * skill.level
     # Get featured projects (limit to 3)
    return render(request, 'mycv/index.html', {'experiences': experience,'skills':skills})

def portfolio(request):
    projects = Project.objects.all()  # Get all projects
    return render(request, 'mycv/portfolio.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)  # Get the specific project by ID
    return render(request, 'mycv/project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., send an email)
            form.save()
            return redirect('index')  # Redirect to home after successful form submission
    else:
        form = ContactForm()
    return render(request, 'mycv/contact.html', {'form': form})

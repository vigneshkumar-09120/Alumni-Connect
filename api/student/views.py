from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Student,skills
from comments.models import Comment
from django.contrib.auth.models import User

from .forms import StudentCreationForm, StudentUploadForm,skillform

from django.views.generic import ListView
from django.views.generic.base import TemplateView,View
from django.views.generic.edit import CreateView, FormView, DeleteView,UpdateView
from django.shortcuts import render,redirect,HttpResponseRedirect
from base.file_handlers import handle_student_csv
from .parsers import parse_query
from django.db.models import Q,Count
from posts.models import Post
from alumni.models import Alumni,Job,Higherstudies,Category

def response(request):
    return HttpResponse('Hello')

class StudentHomeView(View):
    def get(self,request):
        
        posts=Post.objects.all().order_by('-time_posted')[:2]
        context={'posts':posts}
        return render(request,"student/home.html",context)
    



def StudentListView(request):
    if'q'in request.GET:
        q=request.GET['q']
        #data=Internship.objects.filter(Full_name__icontains=q)
        multiple_q=Q(Q(usn__icontains=q)|Q(name__icontains=q)|Q(branch__icontains=q))
        data=Student.objects.filter(multiple_q).order_by('-usn')
    else:
        data=Student.objects.all().order_by('-usn')    
    context={'students':data}
    return render(request,"student/list.html",context)    

class StudentSearchView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    arg = {}

    def get(self, request):
        self.__class__.arg = parse_query(request.GET['query'])
        return super().get(self, request)

    ordering = ['user']

    def get_queryset(self):
        return Student.objects.filter(**self.__class__.arg)

class StudentCommentView(ListView):
    model = Comment
    template_name = 'comments/list.html'
    context_object_name = 'posts'
    ordering = ['posted_by']

    def get_queryset(self):
        return Comment.objects.filter(posted_by=self.request.user)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreationForm
    template_name = 'student/new.html'

    def get_success_url(self):
        return reverse('list_student')

class StudentUploadView(FormView):
    form_class = StudentUploadForm
    template_name = 'student/upload.html'

    def form_valid(self, form):
        handle_student_csv(self.request.FILES["file"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('list_student')

class StudentDeleteView(DeleteView):
    model = User

    def get_success_url(self):
        return reverse('list_student')

class StudentUpdateView(UpdateView):
    model=Student
    form_class = StudentCreationForm
    template_name = 'student/update.html'


    def get_success_url(self):
        return reverse('list_student')

def SkillView(request):
    if request.method == 'POST':
        form=skillform(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.stud=Student.objects.get(user = request.user)
            instance.save()
            return redirect('/students/sprofile')
    else:        
        form=skillform()
    return render(request,'student/skillform.html',{'form':form})        

def sprofile(request):
    data=Student.objects.get(user=request.user)
    item=skills.objects.filter(stud=data)

    
    return render(request,'student/profile.html',{'data':data,'item':item})    

def AlumniList(request):
    if'q'in request.GET:
        q=request.GET['q']
        
        #data=Internship.objects.filter(Full_name__icontains=q)
        multiple_q=Q(Q(usn__icontains=q)|Q(name__icontains=q)|Q(branch__icontains=q)|Q(job__company_name__icontains=q)|Q(job__role__icontains=q)|Q(higherstudies__specialization__icontains=q)|Q(higherstudies__degree__icontains=q)|Q(higherstudies__college_name__icontains=q))
        data=Alumni.objects.filter(multiple_q).order_by('-usn')
        context={'alumni':data}
        return render(request,"student/alsearch.html",context)
    else:
           
    
        return render(request,"student/alsearch.html",)    

def chatbot(request):
    com=Job.objects.all().values('company_name').annotate(total=Count('id')).order_by('-total','company_name')[:1]
    alumni=Alumni.objects.all().count()
    uni=Higherstudies.objects.all().values('college_name').annotate(total=Count('id')).order_by('-total','college_name')[:1]
    context={
        'com':com,
        'uni':uni,
        'alumni':alumni,
    }
    return render(request,'student/chatbot.html',context) 

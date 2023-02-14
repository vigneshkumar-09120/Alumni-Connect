from django.shortcuts import render
from django.views.generic.base import TemplateView,View
from django.views.generic.edit import CreateView, FormView, DeleteView,UpdateView
import time
from alumni.models import Alumni,Category,Job,Higherstudies
from student.models import Student
from django.forms import ValidationError
from .forms import UploadForm
from .analysis import generate
from django.urls import reverse
from .forms import Eventform
from .models import Event
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.db.models import Q ,Max ,Min,Avg,Count


class AdminHomeView(View):
    def get(self,request):
        alumni=Alumni.objects.all().count()
        students=Student.objects.all().count()
        events=Event.objects.all().count()
        eve=Event.objects.all().values('Date__year').annotate(total=Count('id')).order_by('Date__year')
        h=Category.objects.filter(Category__iexact='Higher Studies').count()
        j=Category.objects.filter(Category__iexact='Job').count()
        e=Category.objects.filter(Category__iexact='Entrepreneur').count()
        o=Category.objects.filter(Category__iexact='Others').count()
        com=Job.objects.all().values('company_name').annotate(total=Count('id')).order_by('-total','company_name')
        role=Job.objects.all().exclude(role__iexact='others').values('role').annotate(total=Count('id')).order_by('role')
        roleo=Job.objects.all().filter(role__iexact='others').count()
        spec=Higherstudies.objects.all().exclude(specialization__iexact='others').values('specialization').annotate(total=Count('id')).order_by('specialization')
        speco=Higherstudies.objects.all().filter(specialization__iexact='others').count()
        deg=Higherstudies.objects.all().values('degree').annotate(total=Count('id'))
        context={
            'alumni':alumni,'students':students,'events':events,'eve':eve,
             'h':h,
        'j':j,
        'e':e,
        'o':o,
        'com':com,
        'role':role,
        'spec':spec,
        'deg':deg,
        'roleo':roleo,
        'speco':speco,
        }
        return render(request,'admin/home.html',context)

class HelpView(TemplateView):
    template_name = 'admin/help.html'

class UploadView(FormView):
    form_class = UploadForm
    template_name = 'admin/upload.html'

    def form_valid(self, form):
        #status = generate(self.request.FILES["file"])
        #if not status:
        #    raise ValidationError('Invalid File Structure!')
        time.sleep(5)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reports')

class ReportView(TemplateView):
    template_name = 'admin/reports.html'

class EventView(CreateView):
    model = Event
    form_class = Eventform
    template_name = 'admin/event_form.html'

    def get_success_url(self):
        return reverse('list_event')     

class EventDeleteView(DeleteView):
    model = Event

    def get_success_url(self):
        return reverse('list_event')    

  

def Event_list(request):
    if'q'in request.GET:
        q=request.GET['q']
        #data=Internship.objects.filter(Full_name__icontains=q)
        multiple_q=Q(Q(Name__icontains=q)|Q(Date__icontains=q))
        data=Event.objects.filter(multiple_q)
    else:
        data=Event.objects.all()    
    context={'event':data}
    return render(request,"admin/event_list.html",context)        

class EventUpdateView(UpdateView):
    model=Event
    form_class = Eventform
    template_name = 'admin/event_form.html'


    def get_success_url(self):
        return reverse('list_event')    

def profileview(request,id):
    data=Alumni.objects.get(id=id)
    return render(request,'admin/profile.html',{'data':data})       


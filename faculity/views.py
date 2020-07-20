from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from faculity.models import Faculity_info,Rejcomplaint,Acomplaint,solcomplaint,Appcomplaint,ComplaintUpdate,dcomplaint
from students.models import Rcomplaint,genComplainto,Complaint,Rfwd_complaint,ComplainUpdate,Apcomplaint
from django.core.mail import send_mail
from django.conf import settings
from plyer import notification
from django.core.paginator import Paginator
import json
# Create your views here.
def faculity_login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['Password']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            users=['CS_Cordinator','BBa_Cordinator','Chem_Cordinator']
            hoduser=['Cs_HOD','Chemistry_HOD','	BBA_HOD','Cs_Dean','BBA_Dean','Chemistry_Dean']
            if uname in users:
                messages.success(request,"Successfully Login In")
                return redirect('corhomepage')
            
            elif uname in hoduser:
                messages.success(request,"Successfully Login In")
                return redirect('hodhomepage')


            else:
                messages.success(request,"Successfully Login In")
                return redirect('fachomepage')
        else:

            return render(request,'faculity/faculitylogin.html',{'error':'Invalid Username or password please try again!'})
    
    return render(request,'faculity/faculitylogin.html')

def logout(request):
        auth.logout(request)
        messages.success(request, "Successfully Login OUt")
        return redirect('home')


@login_required(login_url='/faculity-portal')  
def corhomepage(request):
    user=request.user
    complains_list=Rcomplaint.objects.filter(complain_type ="General",cordinator=request.user)
    paginator = Paginator(complains_list, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,'user':user}
    # notification.notify(title="New Complaint",message="You Have a new Complaint Please Check Your Portal",timeout=20)
    
    return render(request,'faculity/corhomepage.html',context)

@login_required(login_url='/faculity-portal')
def hodhomepage(request):
    user=request.user
    comp_list=Acomplaint.objects.filter(forward=user)
    complain=dcomplaint.objects.filter(forward=user)

    paginator = Paginator(comp_list, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,'user':user,'complain':complain}
    # notification.notify(title="New Complaint",message="You Have a new Complaint Please Check Your Portal",timeout=20)
    
    return render(request,'faculity/hod.html',context)

@login_required(login_url='/faculity-portal')  
def send(request,complains_id):
    subject = "Complaint Recived.."
    message = " A new complaint has been recived.Please visit your portal, " \
              "Evaluate the complain and forward to the corresponded personel" \
              "Thank YOU!S "
    email_from = settings.EMAIL_HOST_USER
    if request.method=="POST":
        email=request.POST.get('email')
        forward=request.POST.get('forward')
        print(forward,email)
        complains=Rcomplaint.objects.get(pk=complains_id)
        complain_about=complains.complain_about
        complain_too=complains.complain_too
        complain=complains.complain
        user=complains.user
        acomplaint=Acomplaint(pk=complains_id,complain_about=complain_about,complain_too=complain_too,email=email,forward=forward,complain=complain,send_to=complain_too,user=user)
        acomplaint.save()
        complains.delete()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Accepted And Send to your Corresponding HOD For approval. ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been  Recieved by the Corresponding HOD For approval. ")
        updat.save()
        recipient_list=[email,]
        messages.success(request, "  Complain successfully Sended")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('corhomepage')

    complains=Rcomplaint.objects.get(pk=complains_id)
    gcomplains=genComplainto.objects.all()
    context={'complains':complains,'gcomplains':gcomplains}
    users=request.user
    
    return render(request,'faculity/send.html',context)
    

@login_required(login_url='/faculity-portal')  
def reject(request,complains_id):
    subject = "Complaint Rejected.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        complains=Rcomplaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=complains.complain_about
        complain_too=complains. complain_too
        complain=complains.complain
        reason=request.POST.get('reason')
        comp=Rejcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,reason=reason)
        comp.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        updat.save()
        email=complains.user.email
        complains.delete()
        message = " Your complain has been Rejected!Due to these  {} Reasons.Please Register a valid COmplain Thanks! ".format(reason)
        recipient_list=[email,]
        messages.success(request,"Complain successfully Deleted")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('corhomepage')
@login_required(login_url='/faculity-portal')  
def rej(request,complains_id):
    subject = "Complaint Rejected.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        complains=Acomplaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=complains.complain_about
        complain_too=complains. complain_too
        complain=complains.complain
        reason=request.POST.get('reason')
        comp=Rejcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,reason=reason)
        comp.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        updat.save()
        email=complains.user.email
        complains.delete()
        message = " Your complain has been Rejected!Due to these  {} Reasons.Please Register a valid COmplain Thanks! ".format(reason)
        recipient_list=[email,]
        print(recipient_list)
        messages.success(request,"Complain successfully Deleted")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)

        return redirect('hodhomepage')
@login_required(login_url='/faculity-portal')  
def reje(request,complains_id):
    subject = "Complaint Rejected.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        complains=dcomplaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=complains.complain_about
        complain_too=complains. complain_too
        complain=complains.complain
        reason=request.POST.get('reason')
        comp=Rejcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,reason=reason)
        comp.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been Rejected. ")
        updat.save()
        email=complains.user.email
        complains.delete()
        message = " Your complain has been Rejected!Due to these  {} Reasons.Please Register a valid COmplain Thanks! ".format(reason)
        recipient_list=[email,]
        print(recipient_list)
        messages.success(request,"Complain successfully Deleted")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('hodhomepage')
        
@login_required(login_url='/faculity-portal')          
def fachomepage(request):
    user=request.user
    #complains=Acomplaint.objects.filter(complain_type ="General")
    # notification.notify(title="New Complaint",message="You Have a new Complaint Please Check Your Portal",timeout=20)
    complains=Rcomplaint.objects.filter( complain_type ="Harrassment")
    comp=Apcomplaint.objects.filter(complain_too=user)
    complain=Rfwd_complaint.objects.filter(complain_too=user)
    apcomplain=Appcomplaint.objects.filter(complain_too=user)
    
    context = {'complains': complains,'comp':comp,'complain':complain,'apcomplain':apcomplain}
    print(user)
    return render(request,'faculity/fachomepage.html',context)

@login_required(login_url='/faculity-portal')  
def solution(request,complains_id):
    subject = "Complaint Solved.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        complains=Rcomplaint.objects.get(pk=complains_id)

        id=complains_id
        complain_about=complains.complain_about
        complain_too=complains. complain_too
        complain=complains.complain
        solution=request.POST.get('solution')
        comp=solcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,solution=solution)
        comp.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully ")
        update.save()
        message = " Your complain has been solved!we take {} steps to solve it ".format(solution)
        email=complains.user.email
        complains.delete()
        recipient_list=[email,]
        messages.success(request,"Solution Notification successfully Send ")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('fachomepage')

@login_required(login_url="/faculity-portal")  
def solve(request,complains_id):
    subject = "Complaint Solved.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        comp=Appcomplaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=comp.complain_about
        complain_too=comp. complain_too
        complain=comp.complain
        solution=request.POST.get('solution')
        comps=solcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,solution=solution)
        comps.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully. ")
        updat.save()
        message = " Your complain has been solved!we take {} steps to solve it ".format(solution)
        email=comp.user.email
        comp.delete()
        recipient_list=[email,]
        messages.success(request,"Solution Notification successfully Send")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('fachomepage')
@login_required(login_url="/faculity-portal")  
def sole(request,complains_id):
    subject = "Complaint Solved.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        comp=Apcomplaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=comp.complain_about
        complain_too=comp. complain_too
        complain=comp.complain
        solution=request.POST.get('solution')
        comps=solcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,solution=solution)
        comps.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully ")
        update.save()
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully. ")
        updat.save()
        message = " Your complain has been solved!we take {} steps to solve it ".format(solution)
        email=comp.user.email
        comp.delete()
        recipient_list=[email,]
        messages.success(request,"Solution Notification successfully Send")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('fachomepage')

@login_required(login_url='/faculity-portal')  
def sol(request,complains_id):
    subject = "Complaint Solved.."
    email_from = settings.EMAIL_HOST_USER
    if request.method=='POST':
        complaint=Rfwd_complaint.objects.get(pk=complains_id)
        id=complains_id
        complain_about=complaint.complain_about
        complain_too=complaint. complain_too
        complain=complaint.complain
        solution=request.POST.get('solution')
        comp=solcomplaint(id=id,complain_about=complain_about,complain_too=complain_too,complain=complain,solution=solution)
        comp.save()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been solved Successfully ")
        update.save()
        message = " Your complain has been solved!we take {} steps to solve it ".format(solution)
        email=complaint.user.email
        complaint.delete()
        recipient_list=[email,]
        messages.success(request,"Complain successfully Deleted")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('fachomepage')
@login_required(login_url='/faculity-portal')
def approved(request,complains_id):
    subject = "Complaint Recived.."
    message = " A new complaint has been recived.Please visit your portal, " \
              "Evaluate the complain and forward to the corresponded personel" \
              "Thank YOU!S "
    email_from = settings.EMAIL_HOST_USER
    if request.method=="POST":
        email=request.POST.get('email')
        forward=request.POST.get('forward')
        
        print(email)
        complains=Acomplaint.objects.get(pk=complains_id)
        complain_about=complains.complain_about
        complain_too=complains.complain_too
        complain=complains.complain
        user=complains.user
        appcomplaint=dcomplaint(pk=complains_id,complain_about=complain_about,complain_too=complain_too,email=email,complain=complain,user=user,send_to=complain_too,forward=forward)
        appcomplaint.save()
        complains.delete()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Approved And send To the Corressponding Dean ")
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been Approved And send To the Corressponding Dean. ")
        updat.save()
        update.save()
        recipient_list=[email,]
        messages.success(request, "  Complain successfully Sended")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('hodhomepage')
    complains=Acomplaint.objects.get(pk=complains_id)
    complain_to=complains.complain_too
    gcomplains=genComplainto.objects.filter(gencomplain_to=complain_to)
    context={'complains':complains,'gcomplains':gcomplains}
    return render(request,'faculity/approv.html',context)
@login_required(login_url='/faculity-portal')
def approve(request,complains_id):
    subject = "Complaint Recived.."
    message = " A new complaint has been recived.Please visit your portal, " \
              "Evaluate the complain and forward to the corresponded personel" \
              "Thank YOU!S "
    email_from = settings.EMAIL_HOST_USER
    if request.method=="POST":
        email=request.POST.get('email')
    
        print(email)
        complains=dcomplaint.objects.get(pk=complains_id)
        complain_about=complains.complain_about
        complain_too=complains.complain_too
        complain=complains.complain
        user=complains.user
        appcomplaint=Appcomplaint(pk=complains_id,complain_about=complain_about,complain_too=complain_too,email=email,complain=complain,user=user)
        appcomplaint.save()
        complains.delete()
        update = ComplainUpdate(complain_id=complains_id, update_desc="The Complaint has been Approved And send To the Corressponding Personal ")
        updat = ComplaintUpdate(complain_id=complains_id, update_desc="The Complaint has been Approved And send To the Corressponding Personal. ")
        updat.save()
        update.save()
        recipient_list=[email,]
        messages.success(request, "  Complain successfully Sended")
        send_mail(subject, message, email_from,recipient_list,fail_silently=False)
        return redirect('hodhomepage')
    complains=dcomplaint.objects.get(pk=complains_id)
    complain_to=complains.complain_too
    gcomplains=genComplainto.objects.filter(gencomplain_to=complain_to)
    context={'complains':complains,'gcomplains':gcomplains}
    return render(request,'faculity/app.html',context)
def track(request):
    if request.method=="POST":
        complainId = request.POST.get('complainId')
        try:
            complain = Complaint.objects.filter(id=complainId)
            
            if len(complain)>0:
                update = ComplaintUpdate.objects.filter(complain_id=complainId)
                updates = []
                print(update)
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                    print(response)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'faculity/track.html')
     

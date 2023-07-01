from django.shortcuts import render , HttpResponse
from .models import *
from Codekaro import settings
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.core.mail import send_mail , EmailMessage
from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request , 'base.html')

def signout(request):
    context = {'log' : False}
    if request.method == "POST" :
        logout(request)
        context = {'log' : True}
        return render(request , 'signin.html' , context)

def signup(request) :
    context = {'sent' : False , 'nsent' : False}
    checking = {'exist' : True}
    if request.method == "POST" :
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email =request.POST['email']
        check = User.objects.filter(email = email)

        if(check.exists()) :
            return render(request , 'signup.html' , checking)

        if((len(username) == 0) or (len(fname) == 0) or (pass1 != pass2)) :
            context = {'sent' : False , 'nsent' : True}
            return render(request , 'signup.html' , context)

        myuser = User.objects.create_user(username=username , email=email , password= pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        #myuser.save()

        
        
        # Welcome Email
        subject = "Welcome upcoming sniper!"
        message = "Hello, Hope you are good and healthy " + myuser.username + "!" + " Thank you for adding us to your basket! , We have sent you a confirmation email, please activate your account.."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject=subject ,message= message ,from_email= from_email ,recipient_list= to_list , fail_silently = False)

         # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = False
        email.send()
        context = {'sent' : True}
        return render(request , 'signin.html' , context)
    return render(request , 'signup.html')


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')



def signin(request):
    context = {'success' : False}
     
    if request.method == "POST" :
        
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username = username , password = pass1)
        context = {'success' : True , 'username' : username}    
        
        if user is not None :
            login(request , user)
            return render(request , "home.html" , context )
        else :
            return render(request , 'signin.html' , context)
        
    return render(request , 'signin.html')    

def brainf(request):
    brains = brain.objects.all().order_by('order')
    params = {'questions' : brains}
    return render(request , 'brain.html' , params)

def recursionf(request):
    recursions = recursion.objects.all().order_by('order')
    params = {'questions' : recursions}
    return render(request , 'brain.html' , params)

def beginnerf(request):
    beginners = beginner.objects.all().order_by('order')
    params = {'questions' : beginners}
    return render(request , 'brain.html' , params)

def brutef(request):
    brutes = brute.objects.all().order_by('order')
    
    params = {'questions' : brutes}
    return render(request , 'brain.html' , params)

def greedf(request):
    greeds = greed.objects.all().order_by('order')
    params = {'questions' : greeds}
    return render(request , 'brain.html' , params)

def subf(request):
    subs = sub.objects.all().order_by('order')
    params = {'questions' : subs}
    return render(request , 'brain.html' , params)

def implementf(request):
    implements = implement.objects.all().order_by('order')
    params = {'questions' : implements}
    return render(request , 'brain.html' , params)

def sortf(request):
    sorts = sort.objects.all().order_by('order')
    params = {'questions' : sorts}
    return render(request , 'brain.html' , params)

def binaryf(request):
    binaries = binary.objects.all().order_by('order')
    params = {'questions' : binaries}
    return render(request , 'brain.html' , params)

def pointerf(request):
    pointers = pointer.objects.all().order_by('order')
    params = {'questions' : pointers}
    return render(request , 'brain.html' , params)

def hashf(request):
    hashs = hash.objects.all().order_by('order')
    params = {'questions' : hashs}
    return render(request , 'brain.html' , params)

def pairf(request):
    pairs = pair.objects.all().order_by('order')
    params = {'questions' : pairs}
    return render(request , 'brain.html' , params)

def dpstandf(request):
    dpstands = dpstand.objects.all().order_by('order')
    params = {'questions' : dpstands}
    return render(request , 'brain.html' , params)

def dpf(request):
    dps = dp.objects.all().order_by('order')
    params = {'questions' : dps}
    return render(request , 'brain.html' , params)

def treef(request):
    trees = tree.objects.all().order_by('order')
    params = {'questions' : trees}
    return render(request , 'brain.html' , params)

def graphf(request):
    graphs = graph.objects.all().order_by('order')
    params = {'questions' : graphs}
    return render(request , 'brain.html' , params)

def dsuf(request):
    dsus = dsu.objects.all().order_by('order')
    params = {'questions' : dsus}
    return render(request , 'brain.html' , params)

def segtreef(request):
    segtrees = segtree.objects.all().order_by('order')
    params = {'questions' : segtrees}
    return render(request , 'brain.html' , params)
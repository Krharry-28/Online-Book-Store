from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth, BaseUserManager
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from softy.models import CBGN, DM, HF, LF, Act_Adv, All_Book, Classics, Contact, Fantasy, Horror, Sci_fi
from softy.forms import BookForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.urls import path
#proj

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from softy.models import Document
from softy.forms import DocumentForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView


from django import forms
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
    
def sign_up(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        
        
        a_uth = authenticate(username = Username)
        
        if a_uth is not None:
            messages.add_message(request, messages.INFO, 'User alreddy exists')
            return redirect("/")
        
    
        else:                     
            user = User.objects.create_user(username=Username, password=password )
            user.last_name=last_name
            user.first_name=first_name
            user.email=email                      
            user.save()
            login(request, user)
            return redirect("/")
            
     
                        
                          
    return render(request, 'log_/sign_up.html')

            
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            messages.add_message(request, messages.INFO, 'Welcome To Books World')
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'log_/login.html')

    return render(request, 'log_/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def home(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'home.html')

def about(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'about.html')

def cover(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'cover.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'contact.html')
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def services(request):
    if request.user.is_anonymous:
        return redirect("/login")     
    return render(request,'services.html')



def signup(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'list.html')

def aabook_form(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'Addbooks.html')

def aabook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        publisher = request.POST.get('publisher')
        desc = request.POST.get('desc')
        cover = request.FILES.get('cover')
        pdf = request.FILES.get('pdf')
        CATEGORY = request.POST.get('CATEGORY')
        current_user = request.user
        user_id = current_user.id
        username = current_user.username
        a = All_Book(title=title, author=author, year=year, publisher=publisher, 
                     desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
        a.save()
        if CATEGORY == 'Action and Adventure':
            a = Act_Adv(title=title, author=author, year=year, publisher=publisher, 
                     desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()
        elif CATEGORY =='Classics':
            a = Classics(title=title, author=author, year=year, publisher=publisher, 
                         desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Comic Books and Grapical Novel':
            a = CBGN(title=title, author=author, year=year, publisher=publisher, 
                     desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Detective and Mystery':
            a = DM(title=title, author=author, year=year, publisher=publisher,
                   desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Fantasy':
            a = Fantasy(title=title, author=author, year=year, publisher=publisher,
                        desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Historical Fiction':
            a = HF(title=title, author=author, year=year, publisher=publisher, 
                   desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Horror':
            a = Horror(title=title, author=author, year=year, publisher=publisher, 
                       desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()    
        elif CATEGORY =='Literary Fiction':
            a = LF(title=title, author=author, year=year, publisher=publisher, 
                   desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()  
        elif CATEGORY =='Science Fiction':
            a = Sci_fi(title=title, author=author, year=year, publisher=publisher, 
                       desc=desc, cover=cover, pdf=pdf,Category=CATEGORY, uploaded_by=username, user_id=user_id)
            a.save()      
        messages.success(request, 'Book was uploaded successfully')
        
        return redirect('albook')
	
    else:
        messages.error(request, 'Fill all the details carefully')
        return redirect('aabook_form')

class ABookListView(LoginRequiredMixin,ListView):
    model = All_Book
    template_name = 'list.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return All_Book.objects.order_by('-id')
    
class ABookListView0(LoginRequiredMixin,ListView):
    model = Act_Adv
    template_name = 'categ/Act_Adv.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return Act_Adv.objects.order_by('-id')
    
class ABookListView1(LoginRequiredMixin,ListView):
    model = Classics
    template_name = 'categ/classics.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return Classics.objects.order_by('-id')
    
class ABookListView2(LoginRequiredMixin,ListView):
    model = CBGN
    template_name = 'categ/cbgn.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return CBGN.objects.order_by('-id')    
            
class ABookListView3(LoginRequiredMixin,ListView):
    model = DM
    template_name = 'categ/DM.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return DM.objects.order_by('-id')      
    
class ABookListView4(LoginRequiredMixin,ListView):
    model = Fantasy
    template_name = 'categ/fantasy.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return Fantasy.objects.order_by('-id')    
    
class ABookListView5(LoginRequiredMixin,ListView):
    model = HF
    template_name = 'categ/HF.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return HF.objects.order_by('-id')

class ABookListView6(LoginRequiredMixin,ListView):
    model =Horror
    template_name = 'categ/Horror.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return Horror.objects.order_by('-id')

class ABookListView7(LoginRequiredMixin,ListView):
    model = LF
    template_name = 'categ/LF.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return LF.objects.order_by('-id')

class ABookListView8(LoginRequiredMixin,ListView):
    model = Sci_fi
    template_name = 'categ/Sci-fi.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return Sci_fi.objects.order_by('-id')
    
class AViewBook(LoginRequiredMixin,DetailView):
    model = All_Book
    template_name = 'bookview.html'
    context_object_name = 'books'
    paginate_by = 3
       
    def get_queryset(self):
        return All_Book.objects.order_by('-id')
    
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'signup.html',{'documents': documents, 'form': form})


class AManageBook(LoginRequiredMixin,ListView):
    model = All_Book
    template_name = 'manage_books.html'
    context_object_name = 'books'
    paginate_by = 3
    def get_queryset(self):
        return All_Book.objects.order_by('-id')
    
class ADeleteBook(LoginRequiredMixin,DeleteView):
    model = All_Book
    template_name = 'confirm_delete.html'
    success_message = 'Data was deleted successfully'

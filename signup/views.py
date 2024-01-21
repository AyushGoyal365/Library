from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate,login
from .models import Profile,Book

 


# Create your views here.

def allbook(request):
   
    books = Book.objects.all()
    
    genres = Book.objects.values_list('genre', flat=True).distinct()
    
    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = books.filter(genre=genre_filter)
    context = {
        'books': books,
        'genres': genres,
        
    }
    return render(request, 'allbooks.html', context)
def AOA(request):
    return render(request,'AOA.html')
def authorhome(request):
    
    return render(request,'Author/home.html')
def authorsign_up(request):
    if request.method == 'POST':
        umail = request.POST.get('email')
        upass = request.POST.get('pass')
        uname = request.POST.get('authorname')
        ucity = request.POST.get('city')
        uphone = request.POST.get('phone')
        uimage = request.FILES.get('profileImage')  # Assuming you are using FILES for profile image

        
        my_user, created = User.objects.get_or_create(username=uname, email=umail)
        if created:
            my_user.set_password(upass)
            my_user.save()

        
        existing_profile = Profile.objects.filter(user=my_user).first()
        if existing_profile:
           
            existing_profile.city = ucity
            existing_profile.phone_number = uphone

            if uimage:
                existing_profile.profile_image = uimage

            existing_profile.save()

            
            author_id = generate_author_id(ucity)
            existing_profile.author_id = author_id
            existing_profile.save()

            signup_url = reverse('authorsignin')
            return HttpResponseRedirect(signup_url)

        
        new_profile = Profile(user=my_user, name=uname, city=ucity, phone_number=uphone, profile_image=uimage)

        
        author_id = generate_author_id(ucity)
        new_profile.author_id = author_id

        new_profile.save()

        signup_url = reverse('authorsignin')
        return HttpResponseRedirect(signup_url)

    return render(request, 'Author/signup.html')


def generate_author_id(city):
    
    latest_author = Profile.objects.filter(city__iexact=city).order_by('-author_id').first()

    
    if not latest_author:
        return f'AR{city[:3].upper()}0001'

    
    if latest_author.author_id:
        last_number = int(latest_author.author_id[-4:])
        new_number = last_number + 1
    else:
        new_number = 1

    
    return f'AR{city[:3].upper()}{new_number:04d}'


def authorsign_in(request):
    if request.method=="POST":
        username = request.POST.get('name')
        userpass = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=userpass)
        if user is not None:
            login(request,user)
            signin_url = reverse('authorhome')
            return HttpResponseRedirect(signin_url)
        else:
            return HttpResponse ("wrong email or password")
    return render(request,'Author/signin.html')

def authoraccount(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request,'Author/myaccount.html')

def yourbook(request):
    author = request.user

    
    author_books = Book.objects.filter(author=author)
    print(author_books)
    context = {
        'author_books': author_books,
    }
    return render(request,'Author/yourbooks.html',context)

def addnewbook(request):
    if request.method == 'POST':
        book_name = request.POST.get('bookname')
        genre_name = request.POST.get('genre')  
        number_of_pages = request.POST.get('page')
        cover_image = request.FILES.get('profileImage')

        author = request.user

        book_name_prefix = book_name[:3].upper()
        
        author_id = author.profile.author_id  
        base_book_id = f"{book_name_prefix}{author_id}"

        
        existing_books = Book.objects.filter(book_id__startswith=base_book_id)
        if existing_books.exists():
           
            max_numeric_part = max([int(book.book_id[len(base_book_id):]) for book in existing_books], default=0)
            new_numeric_part = max_numeric_part + 1

            while Book.objects.filter(book_id=f"{base_book_id}{new_numeric_part:04d}").exists():
               new_numeric_part += 1

            book_id = f"{base_book_id}{new_numeric_part:04d}"
        else:
            
            book_id = f"{base_book_id}"

        new_book = Book.objects.create(
            author=author,
            name=book_name,
            genre=genre_name,
            number_of_pages=number_of_pages,
            cover_image=cover_image,
            book_id=book_id 
        )

        return HttpResponseRedirect(reverse('authorhome'))

    
    
    return render(request, 'Author/newbook.html')


#### ADMIN  #######################

def adminallbooks(request):
    books = Book.objects.all()
    
    genres = Book.objects.values_list('genre', flat=True).distinct()
    
    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = books.filter(genre=genre_filter)
    context = {
        'books': books,
        'genres': genres,
        
    }
    return render(request, 'admin/allbooks.html', context)


def adminsign_in(request):
    if request.method=="POST":
        username = request.POST.get('name')
        userpass = request.POST.get('pass')
        if username =="Ayush" and userpass == "flash":
            signin_url = reverse('adminhome')
            return HttpResponseRedirect(signin_url)
        else:
            return HttpResponse ("wrong email or password")
    return render(request, 'admin/signin.html')

def adminhome(request):
    return render(request,'admin/home.html')

def adminaccount(request):
    return render(request,'admin/adminaccount.html')

def allauthors(request):
   
    authors = User.objects.all()

    
    author_info = []

   
    for author in authors:
        
        num_books = Book.objects.filter(author=author).count()

        
        author_info.append({
            'author': author,
            'num_books': num_books,
        })

    context = {
        'author_info': author_info,
    }

    return render(request, 'admin/allauthors.html', context)

def author_detail(request,username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request,'admin/authordetail.html',context)
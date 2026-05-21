from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Editora, Livro, Autor
from .forms import EditoraForm, LivroForm, AutorForm, SignInForm, SignUpForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseNotAllowed
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import AutorSerializer, EditoraSerializer

# -------- EDITORA --------

def listar_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'editoras/listar.html', {'editoras': editoras})

def criar_editora(request):
    form = EditoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_editoras')
    return render(request, 'editoras/form.html', {'form': form})

def editar_editora(request, id):
    editora = Editora.objects.get(id=id)
    form = EditoraForm(request.POST or None, instance=editora)
    if form.is_valid():
        form.save()
        return redirect('listar_editoras')
    return render(request, 'editoras/form.html', {'form': form})

def deletar_editora(request, id):
    editora = Editora.objects.get(id=id)
    editora.delete()
    return redirect('listar_editoras')


# -------- LIVRO --------

def listar_livros(request):
    livros = Livro.objects.all()
    page = request.GET.get('page',1)
    pag = Paginator(livros, 10)

    try:
        livros = pag.page(page)
    except PageNotAnInteger:
        livros = pag.page(1)
    except EmptyPage:
        livros = pag.page(pag.num_pages)
    
    return render(request, 'livros/listar.html', {'livros': livros})

@login_required
@permission_required('edu.add_livro', raise_exception=True)
def criar_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'livros/form.html', {'form': form})

@login_required 
@permission_required('edu.change_livro', raise_exception=True)
def editar_livro(request, id):
    livro = Livro.objects.get(id=id)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'livros/form.html', {'form': form})

@login_required
@permission_required('edu.delete_livro',  raise_exception=True)
def deletar_livro(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('listar_livros')

    


# -------- AUTOR --------

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores/listar.html', {'autores': autores})

def criar_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_autores')
    return render(request, 'autores/form.html', {'form': form})

def editar_autor(request, id):
    autor = Autor.objects.get(id=id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('listar_autores')
    return render(request, 'autores/form.html', {'form': form})


def deletar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('listar_autores')


def home(request):
    return render(request, 'homeedu.html')    



# ---- AUTENTICAÇÃO -----

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'edu/sign_up.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'edu/sign_in.html', {'form': form})


def logout_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    logout(request)
    return redirect('signin')

# -------- API REST --------

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
 
 
class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
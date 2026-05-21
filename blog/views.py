from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date


def home(request):
    return render(request, "home.html")  
def welcome(request):
  return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
  return HttpResponse(f'Você digitou: {text}')

def nome(request):
    # Simulando um nome vindo da URL ou fixo
    nome_usuario = "Jessye"

    # Lista de produtos como no seu template
    lista_bagulhos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 120},
        {"nome": "Teclado", "preco": 200},
    ]

    context = {
        "nome": nome_usuario,
        "now": datetime.now(),       
        "is_logged_in": True,        
        "role": "admin",             
        "lista_bagulhos": lista_bagulhos
    }

    return render(request, "nome.html", context)

def hora(request):
  context = {
    "nome": "Jessye",
    "data": date.today()
  }
  # vai ser rederizado no home
  return render(request, "hora.html", context)

def login(request):
  context = {
    "is_logged_in": True,
    "role": "admin"
  }
  return render(request, "login.html", context)

def info(request):
  data = {
      "disciplina": "RAD",
      "framework": "Django",
      "semestre": "2026.1"
  }
  return JsonResponse(data)

def lista(request):
    produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 120},
        {"nome": "Teclado", "preco": 200},
    ]

    context = {
        "produtos": produtos
    }

    return render(request, "lista.html", context)

def home(request):
    return render(request, "home.html")

def contato(request, telefone):
    context = {
        "telefone": telefone
    }
    return render(request, "contato.html", context)
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'editoras', views.EditoraViewSet)

urlpatterns = [
    # Autenticação
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.home, name='home'),  # ← Tela inicial
    path('editoras/', views.listar_editoras, name='listar_editoras'),
    path('editoras/nova/', views.criar_editora, name='criar_editora'),
    path('editoras/editar/<int:id>/', views.editar_editora, name='editar_editora'),
    path('editoras/deletar/<int:id>/', views.deletar_editora, name='deletar_editora'),

    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
    path('livros/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('livros/deletar/<int:id>/', views.deletar_livro, name='deletar_livro'),

    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/novo/', views.criar_autor, name='criar_autor'),
    path('autores/editar/<int:id>/', views.editar_autor, name='editar_autor'),
    path('autores/deletar/<int:id>/', views.deletar_autor, name='deletar_autor'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),

        # API REST
    path('api/', include(router.urls)),

]
# Estudo Django - Projeto de Exemplos

Este repositório contém um conjunto de exemplos e estudos práticos utilizando o Django, focado em entender conceitos básicos e avançados do framework.

## Objetivo

O objetivo deste projeto é aprender e aplicar os conceitos do Django, incluindo a criação de modelos, views, templates, formulários, autenticação e APIs, por meio de um conjunto de exercícios e práticas.

## Funcionalidades

- Cadastro e login de usuários.
- Sistema de blog com CRUD (Criar, Ler, Atualizar, Deletar).
- Autenticação de usuários.
- APIs RESTful utilizando Django REST Framework.
- Testes unitários e integração.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
my_django_project/
│
├── myapp/                  # Aplicativo principal
│   ├── migrations/         # Arquivos de migração do banco de dados
│   ├── models.py           # Definições de modelos
│   ├── views.py            # Definição das views
│   ├── urls.py             # Roteamento de URLs
│   ├── templates/          # Templates HTML
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   └── forms.py            # Definição de formulários
│
├── manage.py               # Script para gerenciamento do Django
├── requirements.txt        # Dependências do projeto
├── db.sqlite3              # Banco de dados SQLite
└── settings.py             # Configurações do Django
```

## Pré-requisitos

Certifique-se de ter o Python 3.x e o Django instalado na sua máquina. Além disso, para gerenciar as dependências, é recomendado utilizar um ambiente virtual (virtualenv).

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative o ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate o banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o painel de administração:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Rodar o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

## Principais Códigos e Scripts

### 1. **models.py**

Definição de modelos para o projeto. Exemplo:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### 2. **views.py**

Exemplo de view para exibir posts:

```python
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
```

### 3. **urls.py**

Roteamento de URLs para acessar as views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### 4. **templates/home.html**

Exemplo de template para listar os posts:

```html
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <title>Blog</title>
  </head>
  <body>
    <h1>Posts</h1>
    <ul>
      {% for post in posts %}
      <li>{{ post.title }} - {{ post.created_at }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

### 5. **views.py (API com Django REST Framework)**

Exemplo de API usando Django REST Framework:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
```

### 6. **serializers.py**

Definindo o serializer para a API:

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

## Contribuição

Se você deseja contribuir para este projeto, por favor, siga as etapas:

1. Fork o repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

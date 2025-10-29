# Aula 19 – Introdução às URLs e Views no Django

## 🧠 O que são **URLs** e **Views** no Django?

- **URLs**: definem os caminhos (endereços) que o seu site irá responder.
  Exemplo: `http://127.0.0.1:8000/sobre/` → `/sobre/` é uma URL mapeada dentro do projeto Django.

- **Views**: funções (ou classes) que processam as requisições feitas a uma URL e retornam uma resposta (texto, HTML, JSON etc).

---

## 💻 Exemplo de código (Python)

```python
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# View baseada em função (simples)
def my_view(request):
    return HttpResponse("UMA LINDA STRING")

# Configuração das URLs
urlpatterns = [
    path("admin/", admin.site.urls),  # URL padrão do painel administrativo
    path("sobre/", my_view),          # URL personalizada que chama a função my_view
]
```

## 💡 Explicação rápida

# admin → painel administrativo

# HttpResponse → cria resposta HTTP

# path → mapeia URL para view

# my_view(request) → função chamada ao acessar a URL

# urlpatterns → lista de rotas do projeto

## 🚀 Testando

# python manage.py runserver → iniciar servidor

# Acessar http://127.0.0.1:8000/sobre/ → verá "UMA LINDA STRING"

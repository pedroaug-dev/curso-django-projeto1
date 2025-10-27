````markdown
# Aula 06 – Introdução às URLs e Views no Django

## 🧠 O que são **URLs** e **Views** no Django?

- **URLs**: definem os caminhos (endereços) que o seu site irá responder.
  Exemplo: `http://127.0.0.1:8000/sobre/`
  → Aqui, `/sobre/` é uma URL mapeada dentro do projeto Django.

- **Views**: são funções (ou classes) que processam as requisições feitas a uma URL e retornam uma resposta (como texto, HTML, JSON etc).

---

## 💻 Exemplo de código

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
````

---

## 🧩 Explicação

`from django.contrib import admin`
Importa o módulo do painel administrativo do Django.

`from django.http import HttpResponse`
Permite criar uma resposta HTTP simples (texto, HTML, etc).

`from django.urls import path`
Função usada para mapear URLs a views.

`def my_view(request):`
Define uma função que será executada quando alguém acessar a URL associada.

`HttpResponse("UMA LINDA STRING")`
Retorna um texto simples na página

`urlpatterns`
Lista onde são definidas todas as rotas (URLs) do projeto.

---

## 🚀 Resultado

Ao rodar o servidor com:

```bash
python manage.py runserver
```

E acessar no navegador:

👉 **[http://127.0.0.1:8000/sobre/](http://127.0.0.1:8000/sobre/)**

Você verá na tela:

```bash
UMA LINDA STRING
```

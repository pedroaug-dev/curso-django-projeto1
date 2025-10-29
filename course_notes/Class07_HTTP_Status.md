# Aula – HTTP, Requests, Responses e Status Codes 🌐

## 📝 Conceitos

# HTTP: protocolo cliente-servidor

# Request: pedido do navegador

# Response: resposta do servidor

# Status Code: resultado da requisição, retornado pelo servidor

# Method: tipo de requisição (GET, POST, etc.)

---

## 🔹 Status Codes

| Faixa   | Tipo             | Exemplos                       |
| ------- | ---------------- | ------------------------------ |
| 100–199 | Informativa      | 100 Continue                   |
| 200–299 | Sucesso          | 200 OK, 201 Created            |
| 300–399 | Redirecionamento | 301 Moved Permanently          |
| 400–499 | Erro do cliente  | 404 Not Found, 400 Bad Request |
| 500–599 | Erro do servidor | 500 Internal Server Error      |

# Faixas:

# 1xx → info, 2xx → sucesso, 3xx → redirecionamento, 4xx → erro cliente, 5xx → erro servidor

---

## 🔹 Métodos HTTP

# GET → ler/obter dados

# POST → criar/editar dados

---

## 🔹 Inspecionando requisições (Chrome/Windows)

# Ctrl + R → recarregar, Ctrl + Shift + R → hard reload

# Network Tab → todas as requisições

### 🌐 General (informações gerais da requisição)

# - Request URL: endereço da requisição (ex: http://127.0.0.1:8000/)

# - Request Method: método HTTP usado (GET, POST, etc.)

# - Status Code: resultado da requisição (200 OK, 404 Not Found)

# - Remote Address: endereço do servidor que respondeu

# → fornece visão rápida do que foi solicitado e recebido

### 🧠 Headers

# 🥇 Request Headers → informações enviadas pelo navegador ao servidor:

# - Accept: tipos de conteúdo aceitos

# - Accept-Language: idioma preferido

# - Cookies

# - User-Agent: navegador e sistema

# → ajudam o servidor a formatar a resposta corretamente

# 🥈 Response Headers → informações enviadas pelo servidor ao navegador:

# - Content-Type: tipo de conteúdo retornado

# - Content-Length: tamanho da resposta

# - Status Code

# - Set-Cookie: cookies enviados pelo servidor

# → informam ao navegador como processar a resposta

---

## 🔹 Exemplo Django

```python
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def my_view(request):
    return HttpResponse("UMA LINDA STRING")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sobre/", my_view),
    path("", my_view),  # raiz do site
]
```

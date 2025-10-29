# Aula 22 – Movendo o código para o app Recipes 🥗

## 🔹 Refatorando views para o app

1. Copie cada função de view do arquivo principal (`urls.py`) para `recipes/views.py`.
2. Importe o necessário no topo:

```python
from django.http import HttpResponse
```

3. Opcional: renomeie funções temporariamente com `_` para evitar conflitos.
4. No `urls.py` do projeto, importe as views do app Recipes:

```python
from recipes.views import home, contato, sobre
```

5. Teste cada rota no navegador ✅ e, se tudo funcionar, apague as funções antigas.

---

## 🔹 Refatorando URLs para o app

1. Crie `recipes/urls.py` e mova as URLs do projeto para ele.
2. Exemplo de `recipes/urls.py`:

```python
from django.urls import path
from .views import home, contato, sobre

urlpatterns = [
    path("", home, name="home"),           # 🏠 Home
    path("contato/", contato, name="contato"), # ✉️ Contato
    path("sobre/", sobre, name="sobre"),   # ℹ️ Sobre
]
```

3. No `urls.py` do projeto principal, inclua as URLs do app com `include`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),       # 🔑 Admin
    path("recipes/", include("recipes.urls")), # 🥗 App Recipes
]
```

---

## 🔹 Funcionamento 🌐

- Todas as URLs do app Recipes ficam isoladas dentro do app.
- Aninhamento de URLs:

  - `/recipes/` → Home do Recipes 🏠
  - `/recipes/sobre/` → Sobre ℹ️
  - `/recipes/contato/` → Contato ✉️

- Facilita manutenção, escalabilidade e organização do projeto.

---

## 🔹 Benefícios 💡

- `urls.py` do projeto limpo 🧹
- Views organizadas no app correspondente 📂
- Possibilidade de dividir views em arquivos menores
- Padrão de projeto profissional e escalável 🚀
- Evita conflitos em trabalhos de equipe 🤝

---

## 🔹 Resumo 📝

1. Movemos views para `recipes/views.py`.
2. Criamos `recipes/urls.py` para organizar as rotas.
3. Incluímos URLs do app no `urls.py` do projeto com `include`.
4. Testamos cada rota no navegador ✅
5. Preparação para separar views em arquivos menores caso o projeto cresça.

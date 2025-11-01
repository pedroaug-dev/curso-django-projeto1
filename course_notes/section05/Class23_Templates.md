# 🧩 Class23_Templates_Render_HTML

## 🎯 Objetivo

Usar **templates HTML** no Django para separar a lógica (Python) da apresentação (HTML).

## 🧠 Conceito

- View → processa a requisição.
- Template → mostra o resultado.
- `render()` liga os dois e retorna HTML renderizado.

## ⚠️ Antes

```python
def home(request):
    return HttpResponse("<h1>Olá Mundo</h1>")
```

➡️ Funciona, mas é desorganizado.

## 💡 Agora com `render()`

```python
from django.shortcuts import render

def home(request):
    return render(request, "recipes/home.html")
```

- Localiza o template.
- Processa e **retorna** a resposta.

## 🧱 Estrutura recomendada

```arduino
recipes/
 ├── templates/
 │    └── recipes/
 │         └── home.html
 └── views.py
```

➡️ Nome da pasta dentro de `templates` deve ser igual ao nome do app.

## ⚙️ Configuração

Em `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'recipes.apps.RecipesConfig',
]
```

---

## 🧩 Exemplo de `home.html`

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <title>Recipes</title>
  </head>
  <body>
    <h1>Olá, Mundo!</h1>
  </body>
</html>
```

## 🌐 Templates globais (opcional)

```python
TEMPLATES = [
    {'DIRS': [BASE_DIR / "base_templates"],},
]
```

➡️ Usado para páginas gerais (ex: base, erro, etc.).

## 🧭 Dicas

- Evite conflito de nomes → use namespaces (`recipes/home.html`).
- Sempre mantenha a estrutura organizada e clara.

## 🏁 Resumo prático

| Conceito         | Descrição                             |
| ---------------- | ------------------------------------- |
| `render()`       | Retorna o HTML processado             |
| `templates/`     | Guarda os arquivos HTML               |
| Namespace        | Evita colisões de nomes               |
| `INSTALLED_APPS` | Registra o app no projeto             |
| `DIRS`           | Caminho opcional p/ templates globais |

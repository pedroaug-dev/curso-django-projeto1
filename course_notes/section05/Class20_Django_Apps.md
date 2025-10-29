# Aula 20 – Criando, conhecendo e entendendo apps do Django 🏗️

## Contexto

- Cada app organiza funcionalidades separadas:
  - Ex: página inicial (Home/Rome), sobre, contato.
- Apps permitem reutilização em outros projetos e mantêm o código modular.

---

## Criando um app de receitas

```powershell
python manage.py startapp recipes
```

- Cria pasta `receitas/` com arquivos que compõem um App Django:

# Estrutura de um App Django 📦

- 🗂️ `migrations/` → Registra alterações no **banco de dados**, como criação ou modificação de tabelas, permitindo que o Django aplique essas mudanças de forma controlada.
- 📄 `__init__.py` → Indica que a pasta é um **pacote Python**, permitindo importar módulos e arquivos do app em outras partes do projeto.
- 🏛️ `admin.py` → **Registra modelos** no painel administrativo do Django, permitindo criar, editar e deletar registros pelo admin.
- ⚙️ `apps.py` → Contém a **configuração do app**, incluindo nome e opções de inicialização necessárias para o Django.
- 🧱 `models.py` → Define os **modelos** do app, que representam tabelas e estruturas de dados no banco.
- 🧪 `tests.py` → Arquivo para **testes unitários e de integração**, garantindo que o app funcione corretamente antes de ir para produção.
- 🌐 `views.py` → Contém as **views** do app, que processam requisições HTTP e retornam respostas (HTML, JSON, redirecionamentos etc.).

💡 No nosso caso, todas as funcionalidades (Home, Sobre, Contato) ficam em **um app só**, chamado `receitas`.

---

## Estrutura e rotas

- Página inicial (raiz do site): `path("", home_view)`

- Sobre: `path("sobre/", sobre_view)`

- Contato: `path("contato/", contato_view)`

- Para cada rota, criamos uma função na `views.py` do app:

```python
def home_view(request):
    return HttpResponse("Página Inicial")

def sobre_view(request):
    return HttpResponse("Sobre")

def contato_view(request):
    return HttpResponse("Contato")
```

💡 Evita criar todas as funções no `urls.py` do projeto, mantendo a lógica modular e organizada.

---

## Observações

- Cada app tem seu próprio espaço para views, templates, formulários e modelos.
- Apps podem ser reutilizados em outros projetos copiando a pasta do app.
- `admin.py` permite criar CRUD automático para modelos do app.
- `tests.py` permite testar funcionalidades do app automaticamente.
- A próxima aula irá mostrar como mover views e URLs do projeto principal para dentro do app.

---

## Próximos passos

1. Mover views para o app `receitas`.
2. Criar URLs específicas dentro do app.
3. Organizar templates e static files.
4. Trabalhar com formulários e validação de dados.

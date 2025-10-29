# Aula 4 – Arquivos iniciais do Django 🚀

## 📁 `__init__.py`

# 📝 indica que a pasta é um pacote Python

# normalmente vazio, mas necessário para importar módulos

## ⚙️ `settings.py`

# 🔧 configurações do projeto:

# - INSTALLED_APPS → apps instaladas

# - DATABASES → banco de dados

# - Templates, estáticos, mídia

# - Segurança e idioma

## 🌐 `urls.py`

# 🛣️ define rotas/URLs do projeto

# mapeia caminhos do navegador para views

## 🔄 `asgi.py`

# 🚀 deploy assíncrono (ASGI)

# suporta WebSockets e apps assíncronas

## ⚡ `wsgi.py`

# ⚡ deploy síncrono (WSGI)

# usado na maioria dos servidores de produção (Gunicorn, uWSGI)

## 🖥️ `manage.py`

# 📌 gerencia o projeto via terminal

# comandos úteis:

# - python manage.py runserver → iniciar servidor

# - python manage.py migrate → aplicar migrations

# - python manage.py startapp → criar nova app

# Aula 4 – Entendendo os arquivos iniciais de um projeto Django

Quando você cria um projeto Django (`django-admin startproject projeto .`), ele gera alguns arquivos essenciais:

## 🔹 `__init__.py`

- Indica que a pasta é um **pacote Python**.
- Normalmente vazio, mas necessário para que Python reconheça a pasta como módulo importável.

## 🔹 `settings.py`

- Contém todas as **configurações do projeto**:
  - Apps instaladas (`INSTALLED_APPS`)
  - Banco de dados (`DATABASES`)
  - Templates, estáticos, mídia
  - Configurações de segurança e idioma

## 🔹 `urls.py`

- Define as **rotas/URLs do projeto**.
- Mapeia os caminhos que o usuário acessa no navegador para as views do Django.

## 🔹 `asgi.py`

- Arquivo para deploy em servidores **ASGI** (suporta WebSockets e aplicações assíncronas).
- Padrão moderno para produção assíncrona.

## 🔹 `wsgi.py`

- Arquivo para deploy em servidores **WSGI** (modo síncrono).
- Utilizado na maioria dos servidores de produção (Gunicorn, uWSGI).

## 🔹 `manage.py`

- Script de **gerenciamento do projeto** via terminal.
- Permite rodar comandos como:
  - `python manage.py runserver` → iniciar servidor de desenvolvimento
  - `python manage.py migrate` → aplicar migrations do banco
  - `python manage.py startapp` → criar uma nova app

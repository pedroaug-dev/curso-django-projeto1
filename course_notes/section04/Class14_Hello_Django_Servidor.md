# Aula 14 – Criando e rodando projeto Django 🚀

## 📂 Criar projeto

django-admin startproject projeto . # 🌱 cria projeto Django na pasta atual

# Estrutura criada:

# - manage.py → script de gerenciamento

# - projeto/ → arquivos de configuração (settings.py, urls.py, asgi.py, wsgi.py)

## 🖥️ Rodar servidor de desenvolvimento

python manage.py runserver # ▶️ inicia servidor local (padrão: http://127.0.0.1:8000/)

# ⚡ monitora alterações e recarrega automaticamente

## 📊 Mensagens do servidor

# Performing system checks... → verifica configuração do projeto

# 0 silenced → sem problemas ocultos

# Starting development server at http://127.0.0.1:8000/ → servidor rodando

# Quit with CTRL-BREAK → parar servidor

# WARNING → ⚠️ apenas para desenvolvimento, não use em produção

## 🌐 Acessar projeto

http://127.0.0.1:8000/ # 🖱️ endereço local do projeto

# 127.0.0.1 ou localhost → sua máquina local

# Porta 8000 → padrão do Django para desenvolvimento

💡 Dica: Abrindo esse link, verá a página padrão do Django, confirmando que o servidor está funcionando.

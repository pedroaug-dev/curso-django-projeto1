# Aula 2 – Git, SSH e GitHub 🚀

## 💻 Configurar Git

git config --global user.name "Pedro Augusto Guimarães Santos" # 📝 nome global
git config --global user.email "pedroaugustoguimaraesantos@gmail.com" # 📧 email global
git config --global init.defaultBranch main # 🌿 branch padrão

## 🐍 Inicializar repositório

git init # 📁 cria repositório local

## 🔑 Criar chave SSH

ssh-keygen # 🌱 press Enter para padrão

## 📋 Copiar chave pública

type C:\Users\Geral/.ssh/id_ed25519.pub # 🔎 exibe chave para copiar

## 🌐 Adicionar chave ao GitHub

# GitHub > Settings > SSH and GPG keys > New SSH key > Cole a chave > Add SSH Key

## 🔗 Conectar repositório local ao GitHub

git remote add origin git@github.com:pedroaug-dev/curso-django-projeto1.git # 🔗 adiciona remoto

## 🖥️ Abrir projeto no VS Code

code . # 📝 abre pasta no VS Code

## 🚫 Criar .gitignore

# venv/, \*.pyc, **pycache**/ # ⚠️ arquivos/pastas que não vão pro GitHub

## 📤 Enviar arquivos para GitHub

git add . # ➕ adiciona todos
git commit -m "Initial" # 💾 primeiro commit
git push --set-upstream origin main # ⬆️ envia branch main

## 📊 Status dos arquivos

git status # 🔍 mostra arquivos untracked (U) ou modificados (M)

## ⚡ Dicas extras

ssh -T git@github.com # ✅ testar conexão SSH

# ⚠️ Evite OneDrive; prefira C:\Projetos

# 💡 Atualize .gitignore sempre que criar novos arquivos que não vão pro GitHub

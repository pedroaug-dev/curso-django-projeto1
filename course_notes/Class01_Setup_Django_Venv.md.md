````markdown
# Aula 1 – Iniciando o primeiro projeto com Django e Venv

## 🔹 Comandos básicos do PowerShell

```powershell
# Criação e navegação de pastas
mkdir nome_da_pasta          # Cria uma nova pasta com o nome informado
cd "Área de Trabalho"        # Acessa a pasta Área de Trabalho (aspas necessárias se houver espaço no nome)
cd Desktop                   # Alternativa em inglês para a mesma pasta
dir                          # Lista os arquivos e pastas do diretório atual, útil para conferir o caminho

# Abrir o Visual Studio Code pela linha de comando
code .                       # Abre o VS Code no diretório atual

# Adicionar o comando `code` ao PATH (se ainda não estiver funcionando)
# 1. Abra o VS Code
# 2. Pressione Ctrl + Shift + P
# 3. Digite: Shell Command: Install 'code' command in PATH
# Isso permite usar o comando `code` em qualquer terminal do Windows

# Abrir o VS Code em uma pasta específica
code nome_da_pasta            # Abre o VS Code diretamente na pasta especificada
```
````

---

## 🐍 Aula – Iniciando o primeiro projeto com Django e Venv

### 1️⃣ Etapa 1 – Criar pasta e preparar o ambiente

```powershell
cd area de trabalho
mkdir curso-django-projeto1      # Cria a pasta do projeto
cd curso-django-projeto1         # Entra na pasta do projeto

# Atualiza as ferramentas principais do Python antes de criar o ambiente virtual
python -m pip install pip setuptools wheel --upgrade
```

**💡 Observação:**
Atualizar `pip`, `setuptools` e `wheel` garante que outras bibliotecas (como Django) serão instaladas sem problemas ou warnings.

---

### 2️⃣ Etapa 2 – Criar e ativar o ambiente virtual

```powershell
python -m venv venv             # Cria o ambiente virtual chamado "venv"

# Ativar o venv depende do terminal usado:
.\venv\Scripts\Activate          # PowerShell (recomendado)
# venv\Scripts\activate          # CMD
# source venv/Scripts/activate   # Git Bash
```

**💡 Observação:**
Após ativar, o terminal exibirá `(venv)` antes do caminho, indicando que o ambiente virtual está ativo.

---

### 3️⃣ Etapa 3 – Atualizar ferramentas dentro do venv

```powershell
# Atualiza novamente pip, setuptools e wheel dentro do ambiente virtual
python -m pip install pip setuptools wheel --upgrade
```

**💡 Observação:**
No Windows PowerShell, colocar `--upgrade` no final funciona melhor, evitando warnings ou erros que podem ocorrer se estiver no meio do comando.

---

### 4️⃣ Etapa 4 – Instalar o Django

```powershell
pip install django --upgrade        # Instala a última versão do Django no venv
django-admin --version              # Verifica se o Django foi instalado corretamente
```

**💡 Observação:**
Sempre execute `django-admin --version` para confirmar que o Django está ativo no ambiente virtual correto.

---

### 5️⃣ Etapa 5 – Desativar o venv

```powershell
deactivate                          # Desativa o ambiente virtual e volta para o Python global
```

**💡 Observação:**
Não é necessário informar o nome do venv, o comando `deactivate` sempre fecha o ambiente ativo.

---

## ⚡ Dicas extras

- **Problemas com pip no PowerShell:**
  Se ocorrer erro como `ModuleNotFoundError: No module named 'pip._internal.cli.main'`, pode ser necessário reinstalar o pip dentro do venv:

  ```powershell
  python -m ensurepip --upgrade
  ```

  Ou recriar o venv do zero:

  ```powershell
  rmdir /s /q venv
  python -m venv venv
  .\venv\Scripts\Activate
  python -m ensurepip --upgrade
  ```

- **Evite colocar o projeto dentro do OneDrive**, pois ele pode travar arquivos temporários do Python. Prefira algo como:

  ```powershell
  C:\Projetos\curso-django-projeto1
  ```

- **Sempre verifique se o ambiente virtual está ativo** antes de instalar pacotes:

  ```
  (venv) PS C:\Users\Pedro\Área de Trabalho\curso-django-projeto1>
  ```

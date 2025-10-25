````markdown
# Aula 2 – Configurando chaves SSH, Git e enviando o projeto para o GitHub

## 🔹 Passo 1 – Configurar o Git no computador

```powershell
# Definir nome do usuário global do Git
git config --global user.name "Pedro Augusto Guimarães Santos"

# Definir e-mail do usuário global do Git
git config --global user.email "pedroaugustoguimaraesantos@gmail.com"

# Definir o nome do branch padrão como 'main' para novos repositórios
git config --global init.defaultBranch main
```
````

**💡 Observação:**
Essas configurações são globais e valem para todos os projetos Git do computador.

---

## 🔹 Passo 2 – Inicializar o repositório Git local

```powershell
# Inicializa um repositório Git dentro da pasta do projeto
git init
```

---

## 🔹 Passo 3 – Criar chave SSH

```powershell
# Gera uma nova chave SSH (pressione Enter para todas as opções padrão)
ssh-keygen
```

**💡 Observação:**

- Pressione **Enter** para usar os caminhos e senhas padrão.
- A chave pública será criada em:

```
C:\Users\Geral/.ssh/id_ed25519.pub
```

---

## 🔹 Passo 4 – Copiar a chave pública

```powershell
# Exibe o conteúdo da chave pública para copiar
type C:\Users\Geral/.ssh/id_ed25519.pub
```

- Copie o texto que aparecer, exemplo:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJMBdHdPskGHVVMkeT6xBKKhAiM9IqpclDYwUGqRHst9 pedro augusto@DESKTOP-5PBTU2D
```

---

## 🔹 Passo 5 – Adicionar a chave SSH ao GitHub

1. Acesse: **GitHub > Settings > SSH and GPG keys > New SSH key**
2. No campo **Key**, cole a chave copiada.
3. Dê um **Title** descritivo (ex: `PC Desktop Pedro`).
4. Clique em **Add SSH Key**.

---

## 🔹 Passo 6 – Conectar o repositório local ao GitHub

```powershell
# Copie o endereço SSH do repositório GitHub (Quick setup)
# Exemplo:
git@github.com:pedroaug-dev/curso-django-projeto1.git

# Adiciona o repositório remoto
git remote add origin git@github.com:pedroaug-dev/curso-django-projeto1.git
```

---

## 🔹 Passo 7 – Abrir o projeto no VS Code

```powershell
code .
```

**💡 Observação:**
Isso abre a pasta do projeto no VS Code para começar a editar arquivos e criar commits.

---

## 🔹 Passo 8 – Criar arquivo `.gitignore`

- Crie um arquivo chamado `.gitignore` na raiz do projeto.
- Inclua pastas ou arquivos que **não devem ser enviados para o GitHub**, por exemplo:

```
venv/
*.pyc
__pycache__/
```

---

## 🔹 Passo 9 – Enviar os arquivos para o GitHub

```powershell
# Adicionar todos os arquivos ao Git
git add .

# Criar o primeiro commit
git commit -m "Initial"

# Enviar os arquivos para o GitHub no branch 'main'
git push --set-upstream origin main
```

**💡 Observação sobre git push:**

- A primeira vez que você envia um branch local para o remoto, use `--set-upstream origin main` (ou `-u origin main`) para definir o **upstream**.
- Depois disso, nas próximas atualizações, basta usar apenas:

```powershell
git push
```

- O Git saberá para qual branch remoto enviar os commits automaticamente.

---

## 🔹 Passo 10 – Status dos arquivos no Git

```powershell
git status
```

- Um **arquivo novo** que ainda não foi adicionado aparece com **`U` (Untracked)**.
- Um **arquivo que já foi enviado para o GitHub** mas teve alguma alteração aparece com **`M` (Modified)**.

💡 Dica: Sempre verifique `git status` antes de adicionar e commitar arquivos, assim você sabe exatamente o que será enviado.

---

## ⚡ Dicas extras

- Sempre verifique se a conexão SSH está funcionando antes de enviar arquivos:

```powershell
ssh -T git@github.com
```

- Evite colocar o projeto dentro do OneDrive, pois pode travar arquivos temporários do Python. Prefira algo como:

```
C:\Projetos\curso-django-projeto1
```

- Lembre-se de atualizar o `.gitignore` sempre que criar novos arquivos ou pastas que não precisam ir para o GitHub.

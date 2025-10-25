## 🔹 Comandos utilizados

```bash
django-admin startproject projeto .
```

- Cria um **novo projeto Django** chamado `projeto` na pasta atual (`.` significa "diretório atual").
- Cria a estrutura básica de pastas e arquivos do Django, incluindo:

  - `manage.py` → script principal para gerenciar o projeto
  - Pasta `projeto/` → contém arquivos de configuração (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`)

```bash
python manage.py runserver
```

- Inicia o **servidor de desenvolvimento do Django**.
- Permite acessar o projeto localmente pelo navegador no endereço mostrado (por padrão: `http://127.0.0.1:8000/`).
- Monitora alterações nos arquivos (`Watching for file changes with StatReloader`) e recarrega automaticamente o servidor se algo mudar.

---

## 🔹 Mensagens do servidor

```
Performing system checks...
System check identified no issues (0 silenced).
```

- O Django faz **checagens de sistema** para garantir que a configuração do projeto está correta.
- “0 silenced” significa que não há problemas ocultos nem erros de configuração.

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- Informa que o servidor de desenvolvimento está **rodando** no endereço local `http://127.0.0.1:8000/`.
- Para parar o servidor, pressione **CTRL + BREAK** (ou CTRL + C no terminal comum).

```
WARNING: This is a development server. Do not use it in a production setting.
Use a production WSGI or ASGI server instead.
```

- É um **aviso** de que o servidor iniciado é apenas para desenvolvimento, **não deve ser usado em produção**.
- Em produção, você usaria servidores WSGI ou ASGI como Gunicorn, uWSGI ou Daphne.

---

## 🔹 Link do servidor

```
http://127.0.0.1:8000/
```

- É o **endereço local** onde você pode acessar o projeto no navegador.
- “127.0.0.1” ou “localhost” significa **apenas sua máquina local**.
- Porta `8000` é a porta padrão do Django para desenvolvimento.

💡 Dica: Se você abrir esse link no navegador, verá a **página padrão do Django**, confirmando que o servidor está funcionando.

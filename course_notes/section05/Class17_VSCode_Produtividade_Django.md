# Aula 17 – VS Code e produtividade com Django 🚀

## 🖥️ Terminal integrado

# Ctrl + ' → abre terminal integrado

# python manage.py runserver → rodar servidor Django

# Ctrl + Shift + P → abre Command Palette (acessar comandos, extensões, tarefas)

## 🐞 Debug Django no VS Code

# Crie `.vscode/launch.json` com:

```python
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django", # 📝 nome da configuração
            "type": "python", # 🐍 tipo Python
            "request": "launch", # ▶️ iniciar programa
            "program": "${workspaceFolder}/manage.py", # caminho principal
            "args": ["runserver"], # argumentos para manage.py
            "django": true # habilita modo Django
        }
    ]
}
```

💡 Dicas:

# - Salve launch.json, vá em Run and Debug → Start Debugging

# - Use breakpoints e inspecione variáveis para maior produtividade

```

```

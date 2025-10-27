# Aula 5 – Usando o VS Code a nosso favor para produtividade com Django

## 🔹 Abrindo o terminal integrado

- No VS Code, você pode abrir o terminal integrado com:

```

Ctrl + '

```

- No terminal, você pode rodar comandos do Django normalmente, por exemplo:

```bash
python manage.py runserver
```

- Você também pode abrir o **Command Palette** do VS Code com:

```
Ctrl + Shift + P
```

- A partir daí, consegue acessar rapidamente comandos do terminal, extensões, tarefas e outras funcionalidades do VS Code.

---

## 🔹 Configurando o debug do Django no VS Code

Para rodar o servidor com **debug**, é necessário criar um arquivo `launch.json` dentro da pasta `.vscode` com a seguinte configuração:

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```

### 🔹 Explicação dos campos

- `"name"`: nome da configuração que aparece no VS Code (ex: Python: Django).
- `"type"`: define que é uma configuração para Python.
- `"request"`: indica que vamos **iniciar** (`launch`) o programa.
- `"program"`: caminho do arquivo principal, geralmente `manage.py`.
- `"args"`: argumentos passados ao `manage.py`, aqui usamos `runserver`.
- `"django"`: habilita o modo Django para o debug.

💡 **Dica:**

- Depois de salvar o `launch.json`, basta ir na aba **Run and Debug** do VS Code e clicar em **Start Debugging**.
- Assim você consegue usar breakpoints, inspecionar variáveis e ter muito mais produtividade enquanto desenvolve no Django.

```

```

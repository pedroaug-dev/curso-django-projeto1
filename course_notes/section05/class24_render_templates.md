### Class 24 – A função `render` e caminhos de templates

- **Função `render`**:

  - Carrega um template HTML e retorna um `HttpResponse`.
  - Recebe **request**, **template** e **contexto** (dicionário de variáveis).
  - Permite passar **status HTTP**, ex.: `render(request, "home.html", status=404)`.

- **Contexto**:

  - Dicionário de Python que envia variáveis para o template.
  - Exemplo:

    ```python
    render(request, "home.html", {"nome": "Luiz Otávio"})
    ```

    No HTML: `{{ nome }}` exibe o valor.

- **Caminhos de templates**:

  - Django busca templates dentro da pasta padrão `templates` do app.
  - Para múltiplas pastas, é possível especificar caminhos completos:

    ```python
    render(request, "receitas/home.html")
    render(request, "base/tempo.html")
    ```

  - Evita colisão de nomes usando subpastas por app ou base/global.

- **Boas práticas**:

  - Criar subpastas dentro de `templates` por app (`recipes/`, `base/`, `global/`).
  - Evita confusão e garante prioridade correta ao carregar templates.

- **Resumo visual**:

  1. `render` → carrega template + contexto + status HTTP.
  2. Pastas de templates organizadas evitam colisão de nomes.
  3. Variáveis passadas no contexto aparecem no HTML usando `{{ }}`.

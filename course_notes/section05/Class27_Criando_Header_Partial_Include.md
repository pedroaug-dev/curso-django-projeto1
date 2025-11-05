# Aula 27: Criando Header e Partial com Include no Template

## Resumo Sucinto

- Objetivo: Criar o header do site como um trecho parcial reutilizável (`partial`) e incluí-lo nos templates com `{% include %}`.
- Separar o menu do header, que será implementado depois, pois é independente.
- Estrutura do header:
  - Container externo (ocupa a largura total da página)
  - Container interno (centralizado, largura fixa)
  - Logo + link para a página inicial
- CSS inicial:
  - Reset: `* { box-sizing: border-box; margin: 0; padding: 0; }`
  - Fonte base: 16px (`1rem`)
  - Trabalhar com unidades `rem` para consistência
- Separação de partial:
  - Criar pasta `partials` dentro de `templates`
  - Criar `header.html` para o header
  - Incluir nos templates com `{% include 'partials/header.html' %}`
- Observações:
  - O código CSS ainda está dentro do template; depois será movido para arquivos estáticos
  - Partial permite reutilização em todas as páginas
  - Incluir ícones via Font Awesome (`<i class="fas fa-icon"></i>`)
  - Evitar alterações desnecessárias e focar em estruturar o header primeiro

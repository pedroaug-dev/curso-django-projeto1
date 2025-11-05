# Class 26. Adicionando font-awesome no template

Fala pessoal.

Então agora sabendo o que a gente vai fazer que no caso fica mais fácil porque agora a gente tem um objetivo.

A forma mais simples seria copiar todo o CSS ou HTML pronto e colar no Django, mas isso não é o ideal.
Vamos fazer juntos, entendendo cada passo.

## Limpeza do projeto
- Remover funções de exemplo que não serão usadas (`sobe` e `contato`) do `views.py`.
- Remover importações desnecessárias.
- Salvar e garantir que não existam erros pendentes.

## Preparando o Font Awesome
1. Acessar o site oficial do Font Awesome (fontawesome.com) e escolher a versão estável (por exemplo, 5.15).
2. Selecionar os tipos de ícones que serão usados:
   - **Brands**: para ícones de marcas (Twitter, Facebook, etc.)
   - **Solid**: para ícones sólidos genéricos
   - **Font CSS**: o arquivo principal da fonte
3. Copiar o código CSS/JS correspondente para o nosso template inicial.
4. Colar os links no `<head>` do HTML principal, antes de outros conteúdos.

### Observações importantes:
- Não incluir códigos desnecessários ainda, só o que será usado imediatamente.
- No futuro, podemos separar CSS/JS em arquivos estáticos dedicados.
- Ícones podem ser utilizados com classes específicas do Font Awesome (FAS, FAB, etc.) e ajustados com CSS sem perder qualidade.

## Testando ícones
- Escolher um ícone de exemplo no site do Font Awesome.
- Copiar a classe do ícone.
- Inserir no HTML do template.
- Atualizar a página e verificar se o ícone aparece corretamente.

### Dicas:
- Sempre começar com o mínimo necessário.
- Separar e organizar arquivos estáticos só quando for realmente necessário.
- Testar cada alteração para evitar confusão.

Na próxima aula, continuaremos implementando e testando ícones no site.

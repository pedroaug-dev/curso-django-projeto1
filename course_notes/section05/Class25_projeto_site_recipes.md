# Class 25 - O que vamos criar neste projeto? Conheça o nosso site! 🍰

## 1. Objetivo
Criar um site de receitas simples, bonito e funcional, onde usuários podem criar contas, adicionar receitas e interagir com o conteúdo de forma segura.

---

## 2. Funcionalidades principais

### Página Inicial
- Logo e campo de busca.
- Lista de todas as receitas disponíveis.

### Visualização de Receitas
- Imagem da receita, título, autor, data e categoria.
- Tempo de preparo e número de porções.
- Detalhes da receita em **texto puro** (não HTML).

### Sistema de Usuários
- Criação de conta com validação de dados (usuário, email e senha).
- Login e dashboard personalizado.
- Controle total sobre suas receitas **enquanto não publicadas**.
- Após publicação por administradores, o usuário **não pode mais editar ou apagar**.

### Segurança
- Validações do Django e adicionais no formulário.
- ReCaptcha do Google para evitar bots.
- Apenas texto puro permitido para conteúdo de receitas.
- Usuários só podem escolher categorias existentes.

### Gerenciamento de Receitas
- Criar, editar e apagar receitas **antes da publicação**.
- Administrador aprova e publica receitas.
- Dashboard mostra receitas não publicadas do usuário.

---

## 3. Extras
- Validação de formulários e campos obrigatórios.
- Upload de imagens para receitas (respeitando regras de segurança).
- Prevenção contra edição de receitas já publicadas.

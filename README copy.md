# Geração de guia de estudo com LLM e arquitetura multi-agentes

Este repositório tem como objetivo o desenvolvimento de uma aplicação baseada em agentes inteligentes utilizando a plataforma CREWAI. 
O projeto consiste na criação de quatro agentes que auxiliarão alunos no processo de aprendizado, fornecendo planos de estudo personalizados, conteúdos relevantes e mensagens motivacionais.

## 📌 Objetivos do Projeto

O projeto visa explorar a construção de agentes inteligentes que interagem de forma autônoma para melhorar a experiência de estudo dos alunos. Cada agente desempenha um papel específico para tornar o aprendizado mais eficiente e motivador.

### 🧠 Agentes Inteligentes Desenvolvidos

1. **Coach Motivador**
💡 Responsável por: Enviar mensagens motivacionais e dicas de produtividade para manter o aluno focado, disciplinado e engajado durante o processo de estudos.

2. **Coordenador Especialista em Guia de Estudos**
📚 Responsável por: Criar um guia de estudos personalizado para o aluno, considerando suas dificuldades em determinadas disciplinas e fornecendo uma estrutura clara e organizada para o aprendizado.

3. **Coordenador Especialista em Plano de Estudos**
📚 Responsável por: Desenvolver um plano de estudos personalizado, com cronograma e metas, adaptado às necessidades e ao ritmo do aluno.

4. **Coordenador Especialista em Material de Estudos**
🔍 Responsável por: Pesquisar e selecionar vídeos no YouTube sobre os tópicos estudados, garantindo que o aluno tenha acesso aos materiais mais relevantes e de qualidade para complementar seu aprendizado.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.0**  
- **CREWAI** (Plataforma para criação de agentes inteligentes)  
- **YouTube API** (Para busca de vídeos educativos)  
- **Ambiente virtual (.venv)**  
- **Gerenciamento de pacotes com PIP**  

---

## 📌 Instalação e Configuração

Antes de iniciar o desenvolvimento, é necessário configurar o ambiente corretamente.

### Passo 1: Verificando a versão do Python

O projeto requer **Python 3.11.0**. Para verificar a versão instalada:

```sh
python --version
```

Se necessário, faça o download da versão correta em: [Python Downloads](https://www.python.org/downloads/).

### Passo 2: Atualizando o PIP

Para garantir que as dependências sejam instaladas corretamente, atualize o **PIP**:

```sh
python.exe -m pip install --upgrade pip
```

### Passo 3: Criando e Ativando o Ambiente Virtual

Para manter as dependências organizadas e evitar conflitos, utilize um **ambiente virtual**:

#### Criando o ambiente virtual:
```sh
python -m venv .venv
```

#### Ativando o ambiente virtual:
- **Windows**:
  ```sh
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```sh
  source .venv/bin/activate
  ```

Após a ativação, todas as bibliotecas instaladas estarão isoladas dentro desse ambiente.

### Passo 4: Instalando Dependências

Para instalar as bibliotecas necessárias:

```sh
pip install -r requirements.txt
```

Se precisar adicionar pacotes manualmente:

```sh
pip install nome-do-pacote
```

---

## 📖 Como Funciona o Projeto

1. O **Aluno** informa a disciplina e suas dificuldades.  
2. O **Coach Motivador** envia mensagens motivacionais ao aluno.  
3. O **Coordenador de Guia de Estudos** criar um guia de estudos personalizado 
4. O **Coordenador de Plano de Estudos** criar um guia de estudos personalizado 
5. O **Coordenador Especialista em Conteúdo** pesquisa vídeos no YouTube sobre o assunto.  

Essa abordagem permite que o estudante tenha um direcionamento claro, materiais de apoio e incentivo durante seu processo de aprendizado.

---

## 📌 Como Contribuir

Caso deseje contribuir para este projeto, siga estas etapas:

1. **Fork** o repositório.
2. Crie uma **branch** para a sua funcionalidade (`git checkout -b minha-feature`).
3. Faça o **commit** das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o **push** para a branch (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

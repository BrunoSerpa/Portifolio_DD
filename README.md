<h1 align="center"> Desafio do Portifólio  Pessoal</h1>

<span id="sobre"></span>

# Sobre o Desafio

Através das dicas e métodos ensinados pelo profº Fabrício Galende Marques de Carvalho, deverá sem feito um portifólio Pessoal Web. 

# Conteúdos do ```doc/```:
- Wireframe: O protótipo do site
- Palheta de Cores: As cores principais utilizada no site

<span id="comoUsar"></span>

# Como Usar

<b>O que será necessário:</b></summary>

- <a href="https://git-scm.com/downloads">Git</a> Será necessário o git para fazer uma clonagem do repositório.

- <a href="https://www.python.org/downloads">Python</a> Utilizei a versão 3.11.2, mas qualquer uma a partir da 3.7 irá funcionar, não se esqueça de na hora da instalação, marcar a opção da instalação do pip, pois será necessário para rodar o ambiente virtual.
  
<b>Como executar o sistema:</b>

1º Passo: Clonar o repositório:
```console
git clone "https://github.com/BrunoSerpa/Portifolio_DD" .
```

2º Passo: Criar o ambiente virtual:
```console
python -m venv venv
```

3º Passo: Ativar o ambiente virtual (no windows o arquivo é o .bat):
```console
venv/Scripts/activate.bat
```

4º Passo: Instalar as dependências:
```console
pip install -r requirements.txt
```

5º Passo: Executar a aplicação (na pasta ```src/```)
```console
flask --app app run
```

> OBS: Se o seu python não for estiver na versão recomendada é possível os comandos não funcionarem. Para instalar a versão desejada <a href="https://www.python.org/downloads/release/python-3112/">Clique Aqui</a>

6º Passo: Para finalzar a aplicação:
```console
deactivate
```
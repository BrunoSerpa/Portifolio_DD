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

<span id="clonando"></span>
<b>Clonando o repositório:</b>
  
1º Passo: Entra na pasta que você deseje armazenar o repositório e aperte as teclas CRTL + L.

2º Passo: Digite `cmd` (Isso abrirá um prompt de comando com o diretório da pasta que você se encontra)

3º Passo: Dentro do cmd insira o comando:

`git clone "https://github.com/BrunoSerpa/Desafio02_DW1" .`
  
<b>Rodando Desafio:</b>

1° Passo: Dentro do prompt criado em "<a href="#clonando">Clonando o repositório</a>" insira os comandos:

`cd src` (Entrará na pasta `src/`)

`py -m venv venv` (Criará uma máquina virtual denominada "`venv`")
>Caso o segundo comando não funcionar, troque a palavra py do comando  por <b>py3</b>. 

> OBS: Se o seu python não for estiver na versão recomendada é possível os comandos não funcionarem. Para instalar a versão desejada <a href="https://www.python.org/downloads/release/python-3112/">Clique Aqui</a> ou vá para o site oficial da linguagem.

2º Passo: Insira os Comandos:

  `.\venv\Scripts\activate` (Entrará na sua máquina virtual)

  `pip install -r requirements.txt` (Instalará os requerimentos para rodar a aplicação, encontrados no arquivo `requirements.txt`)

  `flask run` (Isso Executará o arquivo `app.py` e liberará um link para ver a aplicação sendo executada)


4º Passo: Quando finalzar, insira `deactivate` no prompt: (Isso vai parar o venv)
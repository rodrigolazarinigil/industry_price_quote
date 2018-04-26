## Industry Price Quote Model

Esse projeto carrega dados csv para uma base postgres limpando e organizando os dados.

### Instalação (somente para dev):

1) Crie um virtualenv com python 3.5;
1) Adicione os arquivos .csv no diretório 'data'
1) Instale os requerimentos:
```
pip install -r requirements.txt
```

### Executando:

1) A máquina precisa ter os binários do docker e docker-compose instalados;
1) Subindo o postgres com as tabelas em branco:
```
make dev-up
```
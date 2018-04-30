## Industry Price Quote Model

Esse projeto carrega dados csv para uma base postgres limpando e organizando os dados.

*Leia em outros idiomas: [Inglês](README.md), [Português do Brasil](README.ptbr.md)

### Instalação (somente para dev):

1) Crie um virtualenv com python 3.5;
1) Adicione os arquivos .csv no diretório 'data'
1) Instale os requerimentos:
```
pip install -r requirements.txt
```

### Executando:

1) Inicie o banco postgres de amostra em docker:
```
make dev-up
```

### Diretórios do projeto

- data: Contém os arquivos .csv de origem;
- db: Contém o modelo do banco de dados postgres;
- dw/: ETL para as tabelas do data warehouse
- util/: Outras funções;


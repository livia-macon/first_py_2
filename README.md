# Meu primeiro pacote Python

Este pacote foi criado para exemplificar o uso de pacotes Python.

## Como criar um pacote Python

Para criar um pacote Python a partir de um diretório, basta seguir os seguintes passos:

1. Instalar o pacote `setuptools`:

```bash
pip install setuptools
```

2. Verificar o arquivo `setup.py` com as informações do pacote.

3. Utilizar o comando para criar o pacote:

```bash
python setup.py sdist
```

4. O pacote será criado no diretório `dist`.

5. Para instalar o pacote, basta utilizar o comando (atenção para o caminho do arquivo):

```bash
pip install dist/first_py-1.0.tar.gz
```


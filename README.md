# Gerador de QR Code

Script em Python que gera uma imagem de QR Code a partir de um link e a salva como `qrcode.png`. Ao escanear o QR Code com a câmera do celular, a pessoa é direcionada para o link configurado (no código atual, um arquivo do Google Drive).

## Requisitos

- Python 3.8 ou superior
- Biblioteca [`qrcode`](https://pypi.org/project/qrcode/)
- Biblioteca [`Pillow`](https://pypi.org/project/pillow/) (necessária para gerar a imagem)

## Instalação

```bash
pip install "qrcode[pil]"
```

Esse comando já instala o `qrcode` junto com o `Pillow`.

## Como usar

1. Salve o código em um arquivo, por exemplo `gerar_qrcode.py`.
2. Execute no terminal:

```bash
python gerar_qrcode.py
```

3. O arquivo `qrcode.png` será criado na mesma pasta em que o script foi executado.

## Como o código funciona

```python
import qrcode

class Gerar:
    def msg(self):
        data = "https://drive.google.com/file/d/..."
        qr = qrcode.QRCode()
        qr.add_data(data)
        qr.make()
        img = qr.make_image()
        img.save('qrcode.png')

a = Gerar()
a.msg()
```

| Trecho | O que faz |
|---|---|
| `import qrcode` | Importa a biblioteca que cria QR Codes. |
| `class Gerar` | Define uma classe que agrupa a lógica de geração. |
| `data = "..."` | Guarda o conteúdo que será codificado (o link). |
| `qrcode.QRCode()` | Cria o objeto do QR Code. |
| `qr.add_data(data)` | Adiciona o conteúdo ao QR Code. |
| `qr.make()` | Calcula e monta o desenho do QR Code. |
| `qr.make_image()` | Converte o desenho em uma imagem. |
| `img.save('qrcode.png')` | Salva a imagem no arquivo `qrcode.png`. |
| `a = Gerar()` e `a.msg()` | Cria um objeto da classe e executa o método que gera o arquivo. |

## Como trocar o link

Edite a variável `data` dentro do método `msg`:

```python
data = "https://seu-link-aqui.com"
```

Também funciona com texto simples, número de telefone, endereço de site, entre outros.

## Observações

- Se já existir um `qrcode.png` na pasta, ele será **sobrescrito**.
- O link do Google Drive precisa estar com o compartilhamento configurado como "Qualquer pessoa com o link", caso contrário quem escanear não conseguirá abrir o arquivo.
- Se você apagar ou mover o arquivo no Drive, o QR Code continuará existindo, mas deixará de funcionar.

## Possíveis melhorias

- Receber o link e o nome do arquivo como parâmetros em vez de deixá-los fixos no código.
- Personalizar tamanho e cores (`box_size`, `border`, `fill_color`, `back_color`).
- Pedir o link ao usuário com `input()`.

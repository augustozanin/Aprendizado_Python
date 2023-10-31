from flask import Flask

app = Flask(__name__)


# Um decorator atribui uma nova funcionalidade a função que esta abaixo dele
# como no exemplo abaixo, a homepage é acessada agora com /home

@app.route('/')
def homepage():
    return 'essa é minha Homepage'


@app.route('/contatos')
def contatos():
    return 'Esses são os meus contatos'


app.run()

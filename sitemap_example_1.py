from flask import Flask, make_response

app = Flask(__name__)


@app.route('/artigos')
def artigos():
    "este endpoint retorna a lista de artigos"


@app.route('/paginas')
def paginas():
    "este endpoint retorna a lista de paginas"


@app.route('/contato')
def contato():
    "este endpoint retorna o form de contato"


######################################
# Esta parte poderia ser uma extensão
######################################
@app.route('/sitemap.xml')
def sitemap():
    items = [
        '<url><loc>{0}</loc></url>'.format(page)
        for page in ['/artigos', '/paginas', '/contato']
    ]
    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        '{0}</urlset>'
    ).format(''.join(items)).strip()
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'
    return response
#######################################
# / Esta parte poderia ser uma extensão
#######################################


app.run(debug=True)

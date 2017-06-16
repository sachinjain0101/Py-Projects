#!flask/bin/python
from flask import Flask
from core.main import ColSizeExp

app = Flask(__name__)

@app.route('/')
def index():
    colsizeexp = ColSizeExp()
    return colsizeexp.getHTMLOutput()

    #out = colsizeexp.calcLinReg()

    #return """ <table border="1" cellpadding="5" cellspacing="5">
    #           <col width="300">
    #           <col width="300">
    #           <th>Table Name</th>
    #           <th>Days to Expire</th>
    #       """ + outstr + """ </table>
    #       """

@app.route('/version')
def version():
    return """
            <table border="1" cellpadding="3" cellspacing="0" width="200">
              <tr>
                <td>Column Size Expiration</td>
                <td>1.0</td> 
              </tr>
            </table>
           """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)

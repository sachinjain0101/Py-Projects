#!flask/bin/python
from flask import Flask
from core.main import ColSizeExp
from collections import OrderedDict

app = Flask(__name__)

@app.route('/')
def index():
    colsizeexp = ColSizeExp()
    out = colsizeexp.calcLinReg()
    outstr=''
    for k in OrderedDict(sorted(out.items(), key=lambda t: t[1])):
        outstr += '<tr> <td>'+k+'</td> <td>'+str(int(out.get(k)))+'</td> </tr>'
    return """ <table border="1" cellpadding="5" cellspacing="5">
               <col width="300">
               <col width="300">
               <th>Table Name</th>
               <th>Days to Expire</th>
           """ + outstr + """ </table>
           """

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

from flask import Flask, request, render_template
import sys
from utils import df_mgr as dfm
from scripts import graph_mngr as gm
app = Flask(__name__)
master = None
cols = None
colRefDict = {}


@app.route('/')
def hello_world():
    cols = master.columns
    cols = [x for x in cols]
    return render_template("home.html", tag = "Hello Word", cols = cols, colRefDict = colRefDict, colVals = colRefDict.keys())

@app.route('/display', methods=["post"])
def get_display():
        att_keys = [x for x in request.form.listvalues()][0]
        attrs = [colRefDict[_key] for _key in att_keys]
        _graph = gm.get_graph(master, attrs)
        return render_template("dashboard.html", graph= _graph)

if __name__ == '__main__':
    files = sys.argv[1:]
    master = dfm.get_dataframe(files)
    cols = master.columns
    for col in cols:
            colRefDict.update({
                col.replace(" ", "_").lower() :col
            })
    print (colRefDict)
    app.run()

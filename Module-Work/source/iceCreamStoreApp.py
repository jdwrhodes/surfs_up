#%%
from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
#import jsonify
# %%
databaseConnectionString = 'sqlite:///./Module-9/databases/icecreamstore.sqlite'
# %%
databaseEngineObject = create_engine(databaseConnectionString)
# %%
autoMapBaseInstance: automap_base = automap_base()
# %%
autoMapBaseInstance.prepare(databaseEngineObject,reflect=True)
#%%
autoMapBaseInstance
# %%
iceCreamStore = autoMapBaseInstance.classes.icecreamstore
# %%
app = Flask(__name__)
#%%
@app.route('/')
def home():
    session: Session = Session(databaseEngineObject)
    iceCreamMenu = session.query(iceCreamStore.Flavors, iceCreamStore.Price).filter(iceCreamStore.Flavors != 'testflavor').all()
    session.close()
    return render_template('index.html', my_name = 'Josh', menu = iceCreamMenu)

#%%
@app.route('/insert')
def insert():
    pass
    
# keep going to add the rest of crud
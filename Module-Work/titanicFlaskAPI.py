#%%
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
#import jsonify
# %%
databaseConnectionString = 'sqlite:///./Module-9/databases/titanic.sqlite'
# %%
databaseEngineObject = create_engine(databaseConnectionString)
# %%
autoMapBaseInstance: automap_base = automap_base()
# %%
autoMapBaseInstance.prepare(databaseEngineObject,reflect=True)
# %%
Passenger = autoMapBaseInstance.classes.passenger
# %%
app = Flask(__name__)
#%%
@app.route('/')
def home():
    """List all api routes"""
    return {
        'default':'/',
        'names':'/api/names',
        'passengers':'/api/passengers',
        'passenger_class': '/api/passenger_class/<int = [1,2,3]>'
    }
# %%
@app.route('/api/names')
def names():
    session: Session = Session(databaseEngineObject)
    results = session.query(Passenger.name).all()
    session.close()
    return jsonify(results)
#%%
@app.route('/api/passengers')
def passengers():
    session: Session = Session(databaseEngineObject)
    results = session.query(Passenger.name, Passenger.age, Passenger.pclass).all()
    session.close()
    
    allPassengers = []
    for name, age, pclass in results:
        passenger = {}
        passenger['name'] = name
        passenger['age'] = age
        passenger['pclass'] = pclass
        allPassengers.append(passenger)
    
    return jsonify(allPassengers)

#%%
@app.route('/api/passenger_class/<class_number>')
def passenger_class(class_number):
    session: Session = Session(databaseEngineObject)
    pClass = ''
    results = ''
    if class_number == 1:
        pClass = '1st'
    elif class_number == 2:
        pClass = '2nd'
    elif class_number == 3:
        pClass = '3rd'
    if pClass == '':
        results = session.query(Passenger.name, Passenger.pclass).all()
    else:
        results = session.query(Passenger.name, Passenger.pclass).filter(Passenger.pclass == pClass)
    
    session.close()
    return jsonify(results)
#%%
if __name__ == '__main__':
    app.run(debug=True)
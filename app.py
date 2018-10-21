from flask import Flask, render_template
import os
import time


# Create a Flask app:
app = Flask(__name__)

message = 'Hot Wells'
pythonDay = time.strptime('30 11 18 8' ,'%d %m %y %H' )
tiempoActual = time.time()
tiempoFaltante =time.mktime(pythonDay)- tiempoActual
dias = int(tiempoFaltante/(3600*24))
horas  = int( tiempoFaltante/3600- dias*24)
minutos  = int( tiempoFaltante/60- dias*24*60 - horas*60 )
segundos  = int( tiempoFaltante- dias*24*3600 - horas*3600-minutos*60 )

# Render index:
@app.route('/')
def index():
    if(tiempoFaltante>1):
        pythonDay = time.strptime('30 11 18 8' ,'%d %m %y %H' )
        tiempoActual = time.time()
        timepoFaltante =time.mktime(pythonDay)- tiempoActual
        dias = int(timepoFaltante/(3600*24))
        horas  = int( timepoFaltante/3600- dias*24)
        minutos  = int( timepoFaltante/60- dias*24*60 - horas*60 )
        segundos  = int( timepoFaltante- dias*24*3600 - horas*3600-minutos*60 )
        return render_template('index.html', d = dias, h = horas, m= minutos, s = segundos )




def hello():
    return "Hot wells"
# Main:
if __name__ == '__main__':
    app.run(debug=False)

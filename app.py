import pandas as pd
from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine,MetaData,text
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)
app.json.sort_keys = False

#app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atendimentos.db'


# Criando SQLite engine
engine = create_engine('sqlite:///instance/atendimentos.db')
# Transformando csv em dataframe
df = pd.read_csv('atendimentos.csv')
df = df.drop('Unnamed: 0',axis=1)
df['data_atendimento'] = pd.to_datetime(df['data_atendimento'],format='mixed').dt.date

# Transformando df em tabela
df.to_sql('atendimentos', con=engine, if_exists='replace', index=False)


@app.route('/api/v2/atendimentos', methods=['GET'])
def atendimentos2():
    # Pegando argumentos de filtro
    condicao_saude = request.args.get('condicao_saude', type=str ,default=None)
    data_atendimento = request.args.get('data_atendimento',type=str ,default=None)           
    unidade = request.args.get('unidade', type=str ,default=None) 
    
    
    sqliteConnection = sqlite3.connect('instance/atendimentos.db')
    cursor = sqliteConnection.cursor()
    #filtros unicos
    if condicao_saude:
        cursor.execute(f" select * from atendimentos where condicao_saude=? ",(condicao_saude,))
        
    if data_atendimento:
        cursor.execute(f" select * from atendimentos where data_atendimento=? ",(data_atendimento,))

    if unidade:
        cursor.execute(f" select * from atendimentos where unidade=? ",(unidade,))

    #filtros combinados
    if condicao_saude and data_atendimento:
        cursor.execute(f" select * from atendimentos where condicao_saude=? and data_atendimento=?",(condicao_saude,data_atendimento))
        
    if data_atendimento and unidade:
        cursor.execute(f" select * from atendimentos where data_atendimento=? and unidade=?",(data_atendimento,unidade))

    if condicao_saude and unidade:
        cursor.execute(f" select * from atendimentos where data_atendimento=? and condicao_saude=?",(data_atendimento,condicao_saude))
    # retorna todos
    if condicao_saude is None and unidade is None and data_atendimento is None:
        cursor.execute("select * from atendimentos")    
   
    
    resultado = cursor.fetchall()
    atendimentos = list()
    for item in resultado:
        atendimentos.append(
            {
               'id': item[0],
               'nome':item[1],
               'nascimento':item[2],
               'CNS': item[3],
               'CPF': item[4],
               'unidade':item[5],
               'data_atendimento':item[6],
               'condicao_saude':item[7]
 
            }
        )
     
    return make_response(jsonify(mensagem="Lista de atendimentos",dados=atendimentos))


with app.app_context():    
#db.create_all()
    app.run(debug=True)
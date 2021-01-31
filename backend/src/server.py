from flask import Flask, render_template, request, jsonify

#from flask_mysqldb import MySQL
#from flask_sqlalchemy import SQLAlchemy
from db.db_manager import DBManager

from db.process_cvs import processFile

import logging
from multiprocessing import Process

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.getLogger('pika').setLevel(logging.WARNING)
log = logging.getLogger()

import sys

server = Flask(__name__)
#mysql = MySQL(server)

# @server.route("/insert")
# def insert():
#    db.insert_record()
#    return {"succcess": True}

# @server.route("/hello")
# def hello():
#    rec = db.query_titles()

#    response = ''
#    for c in rec:
#       response = response  + '<div>   Hello  ' + c + '</div>'
#    return response
       
@server.route("/ping")
def ping():
   # rec = db.query_titles()

   # response = ''
   # for c in rec:
   #    response = response  + '<div>   Hello  ' + c + '</div>'
   return {"ping": True}

@server.route("/process_cvs", methods=['GET','POST'])
def process_cvs():
   status = "Ready"
   try:
      record_id = request.args.get('record_id') #request.form.get('record_id') #request.form.get('record_id')
      log.info("PROCESS record_id : " + str(record_id))
      # if record_id == None:
      #    record_id = create_record_order_status(record_id)
      #    status = "Pending"
      # else:
      #    status = get_record_order_status(record_id)
      p.start()
      log.info("Background process done")
   except:
      log.info("ERROR ")
      log.info(sys.exc_info())
      return {"status": "failed"}
   #process(db, log)
   return {"status": "successful",
           "record_id": record_id,
           "status": status}
       
@server.route("/search", methods=['GET'])
def query_by_code():
   code = request.args.get('code')
   log.info("Hiting Searching - code : " + code)
   rec = db.query_code(code)
   
   list_of_codes = []

   for c in rec:
      list_of_codes.append({
         "pattern": c['pattern'],
         "payment": bool(c['payment']),
         'occur': c['occur']
      })

   resp = {
      "search_code": code,
      "bill_code": list_of_codes,
      "payment": True
   }
   return resp

@server.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
   # server.config['MYSQL_DATABASE_USER'] = 'root'
   # server.config['MYSQL_DATABASE_PASSWORD'] = 'root'
   # server.config['MYSQL_DATABASE_DB'] = 'EmpData'
   # server.config['MYSQL_DATABASE_HOST'] = 'db'
   # mysql.init_app(server)

   #server.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db'
   #db = SQLAlchemy(server)
   db = DBManager()
   db.populate_db()
   p = Process(target=processFile(db))
   server.run(host='0.0.0.0', debug=True)
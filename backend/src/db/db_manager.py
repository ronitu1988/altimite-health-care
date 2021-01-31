import mysql.connector
import logging
# from TN import TN

# network = TN()
log = logging.getLogger()


class DBManager:
    def __init__(self, database='altimitehealthcare', host="db", user="root", password_file=None):
        #pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password='root',
            host=host, # name of the mysql service as set in the docker-compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        #pf.close()
        self.cursor = self.connection.cursor(buffered=True,dictionary=True)
    
    def populate_db(self):
        #self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `codes` (
                `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                `code` VARCHAR(7),
                `pattern` VARCHAR(255),
                `payment` boolean,
                `occur` int
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS `records` (
                `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                `record_id` VARCHAR(50),
                `status` VARCHAR(25)
            );
        """)


        # self.cursor.execute("""
        # ALTER TABLE codes ADD INDEX index_code (`code`);
        # """)

        # self.cursor.execute("ALTER TABLE codes ADD INDEX index_code_pattern (`code`, `pattern`);")

        # self.cursor.execute('ALTER TABLE codes ADD CONSTRAINT codes_pattern UNIQUE (code, pattern);')
        self.connection.commit()
    
    def insert_record(self, patient_acct, medical_acct, billing_codes):
        pattern = ",".join(billing_codes)
        for code in billing_codes:
            sqlquery = "INSERT INTO codes (code, pattern, payment, occur) VALUES ('{0}', '{1}', {2}, {3}) ON DUPLICATE KEY UPDATE occur = occur+1".format(str(code), str(pattern), False, 1)
            log.info(code + "insert sqlquery : " + str(sqlquery))
            self.cursor.execute(sqlquery)
        self.connection.commit()
        log.info("Insert Done ")

    def query_code(self, code):
        query = "SELECT * FROM codes WHERE code='{0}'".format(code)
        log.info("Query code : " + query)
        self.cursor.execute(query)
        return self.cursor
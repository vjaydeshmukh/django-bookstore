from payment_info import PaymentInfo
from mysql.connector import MySQLConnection, Error
from dbconfig import read_db_config
from abc_dao import AbcDao

class PaymentInfoDao(AbcDao):
    
    def create(self, p_payment):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [p_payment.card_number, p_payment.expir_date, p_payment.cvc, p_payment.customer_id, p_payment.billing_address_id]
            cursor.callproc('createPaymentInfo',args)

            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    def update(self, p_payment):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [p_payment.card_id, p_payment.card_number, p_payment.expir_date, p_payment.cvc, p_payment.customer_id, p_payment.billing_address_id]
            cursor.callproc('updatePaymentInfo',args)

            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()
    def delete(self, p_payment):
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [p_payment.card_id]
            cursor.callproc('deletePaymentInfo', args)

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
    def get_all(self, p_payment):
        all_payments = []
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)
            cursor = conn.cursor()
            args = [p_payment.customer_id]
            cursor.callproc('getAllPaymentInfoByCustomerID',args)
            

            for result in cursor.stored_results():
                payments = result.fetchall()

            for x in payments:
                currentpayment = PaymentInfo()
                currentpayment.card_id = x[0]
                currentpayment.card_number = x[1]
                currentpayment.expir_date = x[2]
                currentpayment.cvc = x[3]
                currentpayment.customer_id = x[4]
                currentpayment.billing_address_id = x[5]
                all_payments.append(currentpayment)

                cursor.close()
            conn.close()
        except Error as error:
            print(error)
        except Exception as e:
            print(e)
        return all_payments
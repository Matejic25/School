import mysql.connector as mc


class Database:
    def __init__(self):
        self.db = None

    def connection(self):
        try:
            self.db = mc.connect(
                host="localhost",
                username="root",
                password="1234321",
                database="bradam"
            )
            return self.db
        except mc.Error:
            print("DB connection failed")

    def get_company_id_by_pib(self, pib):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT id FROM firma WHERE pib like '{pib}'")
        result = mycursor.fetchone()
        return result[0]

    def get_company_pib_by_id(self, id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT pib FROM firma WHERE id = {id}")
        result = mycursor.fetchone()
        return result[0]

    def get_company_name_by_id(self, company_id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT naziv FROM firma WHERE id = {company_id}")
        result = mycursor.fetchone()
        return result[0]

    def get_extinguishers_of_company_by_id(self, company_id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT tip, pod_o_proizvodjacu, fabricki_broj, ispravnost FROM aparat"
                         f" WHERE pripada_firmi = {company_id}")
        result = mycursor.fetchall()
        return result

    def get_controlled_extinguishers_of_company_by_id(self, company_id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT tip, pod_o_proizvodjacu, fabricki_broj, ispravnost FROM aparat"
                         f" WHERE pripada_firmi = {company_id} AND vrsta = 1;")
        result = mycursor.fetchall()
        return result

    def get_periodic_extinguishers_of_company_by_id(self, company_id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT tip, pod_o_proizvodjacu, fabricki_broj, ispravnost FROM aparat"
                         f" WHERE pripada_firmi = {company_id} AND vrsta = 2;")
        result = mycursor.fetchall()
        return result

    def get_addresses_by_pib(self, pib):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT naziv FROM adresa WHERE pib = '{pib}';")
        result = mycursor.fetchall()
        return result

    def get_extinguishers_of_company_at_certain_address(self, address, company_id):
        mycursor = self.connection().cursor()
        mycursor.execute(f"SELECT id FROM adresa WHERE naziv LIKE '%{address}';")
        address_id = mycursor.fetchone()
        mycursor.execute(f"SELECT * FROM aparat as ap WHERE ap.pripada_firmi = {company_id} AND ap.na_adresi = {address_id[0]};")
        result = mycursor.fetchall()
        return result

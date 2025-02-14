from dataclasses import dataclass
import mysql.connector


@dataclass
class Client():
    """ Represents a client in our model who has an agent and views listings """
    client_id: int
    first_name: str
    middle_initial: str
    last_name: str
    phone_area_code: int
    phone_number: int
    email_address: str
    agent_license_number: int
    listing_mls_numbers: list

    @classmethod
    def from_client_id(cls, client_id: int, db_connection: mysql.connector.MySQLConnection):
        """ Returns a client from the database """
        pass
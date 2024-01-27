import os
import sqlite3
import time
from pysnmp.hlapi import *

# Function to insert SNMP data into SQLite database
def insert_data(uptime, incoming_bytes):
    conn = sqlite3.connect('db/snmp_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO snmp_data (uptime, incoming_bytes) VALUES (?, ?)", (uptime, incoming_bytes))
    conn.commit()
    conn.close()

# Function to collect SNMP data every 10 seconds
def collect_snmp_data():
    while True:
        snmp_oid_direction = os.environ.get('SNMP_OID_DIRECTION')
        snmp_oid_speed = os.environ.get('SNMP_OID_SPEED')
        snmp_community = os.environ.get('SNMP_COMMUNITY')
        snmp_target = os.environ.get('SNMP_TARGET')

        # Define OIDs for the attributes you want to collect
        oids = [
            snmp_oid_direction,
            snmp_oid_speed
        ]

        snmp_data = {}

        for oid in oids:
            errorIndication, errorStatus, errorIndex, varBinds = next(
                getCmd(SnmpEngine(),
                       CommunityData(snmp_community, mpModel=0),
                       UdpTransportTarget((snmp_target.split(':')[0], int(snmp_target.split(':')[1]))),
                       ContextData(),
                       ObjectType(ObjectIdentity(oid)))
            )

            if errorIndication:
                print(f"Error: {errorIndication}")
            else:
                for varBind in varBinds:
                    oid_name = str(varBind[0])
                    oid_value = varBind[1].prettyPrint()
                    snmp_data[oid_name] = oid_value

        # Print SNMP data for debugging
        print("SNMP Data:", snmp_data)

        try:
            # Insert SNMP data into the database
            insert_data(snmp_data[snmp_oid_direction], snmp_data[snmp_oid_speed])
        except KeyError as e:
            print("KeyError:", e)

        # Wait for 10 seconds before collecting data again
        time.sleep(10)

if __name__ == "__main__":
    collect_snmp_data()

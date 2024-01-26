from pysnmp.hlapi import *

def get_snmp_data():
    # Define OIDs for the attributes you want to collect
    oids = [
        'iso.3.6.1.4.1.18248.31.1.2.1.1.3.7',  # Direction in degres 1231 = 123.1
        'iso.3.6.1.4.1.18248.31.1.2.1.1.3.8'   # speed in 12 = 1.2 m/s
    ]

    for oid in oids:
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData('public', mpModel=0),
                   UdpTransportTarget(('10.68.30.201', 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        if errorIndication:
            print(f"Error: {errorIndication}")
        else:
            for varBind in varBinds:
                print(varBind)

if __name__ == "__main__":
    get_snmp_data()

import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.181/restconf/"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
        yangConfig = {
            "ietf-interfaces:interface": {
                "name": "Loopback65070031",
                "description": "Added by RESTCONF",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "172.30.31.1",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }

        resp = requests.put(
            api_url + "data/ietf-interfaces:interfaces/interface=Loopback65070031", 
            data=json.dumps(yangConfig), 
            auth=basicauth, 
            headers=headers, 
            verify=False
            )

        resp = requests.put(
        url=api_url + "data/ietf-interfaces:interfaces/interface=Loopback65070031",
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )
        if(resp.status_code == 204):
            return "Cannot create: Interface loopback 65070031"
        elif(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
            return "Interface Loopback65070031 is created successfully"
        
        else:
            print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url + "data/ietf-interfaces:interfaces/interface=Loopback65070031", 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "interface Loopback 65070031 is deleted successfully"
    elif(resp.status_code == 404):
        return "Cannot delete: Interface loopback 65070031"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070031",
            "enabled": True
        }
    }

    resp = requests.patch(
        api_url + "data/ietf-interfaces:interfaces/interface=Loopback65070031",
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070031 is enabled successfully"
    elif(resp.status_code == 404):
        return "Cannot enable: Interface loopback 65070031"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070031",
            "enabled": False
        }
    }

    resp = requests.patch(
        api_url + "data/ietf-interfaces:interfaces/interface=Loopback65070031", 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 65070031 is shutdowned successfully"
    elif(resp.status_code == 404):
        return "Cannot shutdown: Interface loopback 65070031"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "https://10.0.15.181/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback65070031"

    resp = requests.get(
        url=api_url_status,
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json['ietf-interfaces:interface']['admin-status']
        oper_status = response_json['ietf-interfaces:interface']['oper-status']
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 65070031 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 65070031 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 65070031"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

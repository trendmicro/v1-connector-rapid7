# Description

[Cisco ISE](https://www.cisco.com/c/en/us/products/security/identity-services-engine/index.html) is a secure network access tool. Cisco ISE allows for controlled access to a network and the ability to quarantine suspicious endpoints.
 The Cisco ISE InsightConnect plugin allows you to retrieve ANC details, endpoint details and manage quarantine.

This plugin utilizes the [ISE](https://github.com/bobthebutcher/ise) library.

# Key Features
  
* Manage Quarantine  
* Retrieve endpoint details  
* Retrieve ANC details

# Requirements
  
* Cisco_ISE host's IP address  
* Cisco_ISE username and password

# Supported Product Versions
  
* Cisco ISE API 2023-05-09

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP address for Cisco ISE|None|192.0.2.0/24|
|credentials|credential_username_password|None|True|Username and password|None|{"username": "ExampleUsername", "password": "ExamplePassword"}|
|ssl_verify|boolean|True|True|Enable SSL verification|None|True|
  
Example input:

```
{
  "address": "192.0.2.0/24",
  "credentials": {
    "password": "ExamplePassword",
    "username": "ExampleUsername"
  },
  "ssl_verify": true
}
```

## Technical Details

### Actions


#### Get ANC Endpoint
  
This action is used to returns ANC information based on the MAC address supplied

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mac|string|None|True|MAC address of the endpoint|None|00:0E:35:D4:D8:52|
  
Example input:

```
{
  "mac": "00:0E:35:D4:D8:52"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|ANCEndpoint|False|Endpoint information|{"id":"82e2b6d0-546b-11e8-bc94-12d1173c5b91","name":"00:0E:35:D4:D8:52","description":"","mac":"00:0E:35:D4:D8:52","profileId":"2ac6a950-8c00-11e6-996c-525400b48521","staticProfileAssignment":false,"groupId":"aa10ae00-8bff-11e6-996c-525400b48521","staticGroupAssignment":false,"portalUser":"","identityStore":"","identityStoreId":"","link":{"rel":"self","href":"https://10.4.22.225:9060/ers/config/endpoint/name/00:0E:35:D4:D8:52","type":"application/xml"}}|
  
Example output:

```
{
  "results": {
    "description": "",
    "groupId": "aa10ae00-8bff-11e6-996c-525400b48521",
    "id": "82e2b6d0-546b-11e8-bc94-12d1173c5b91",
    "identityStore": "",
    "identityStoreId": "",
    "link": {
      "href": "https://10.4.22.225:9060/ers/config/endpoint/name/00:0E:35:D4:D8:52",
      "rel": "self",
      "type": "application/xml"
    },
    "mac": "00:0E:35:D4:D8:52",
    "name": "00:0E:35:D4:D8:52",
    "portalUser": "",
    "profileId": "2ac6a950-8c00-11e6-996c-525400b48521",
    "staticGroupAssignment": false,
    "staticProfileAssignment": false
  }
}
```

#### Quarantine
  
This action is used to quarantine a host

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mac_address|string|None|True|The host MAC address|None|00:0E:35:D4:D8:52|
|policy|string|None|True|The quarantine policy to apply|None|Shut_Down|
  
Example input:

```
{
  "mac_address": "00:0E:35:D4:D8:52",
  "policy": "Shut_Down"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ers_anc_endpoint|ErsAncEndpoint|False|Returns info on the endpoint and what policy was applied|{"id":"5810ed0b-f1e8-40dc-bbda-78dcda4ae33d","macAddress":"00:0E:35:D4:D8:51","policyName":"komand_test","link":{"rel":"self","href":"https://10.4.22.225:9060/ers/config/ancendpoint/5810ed0b-f1e8-40dc-bbda-78dcda4ae33d","type":"application/xml"}}|
  
Example output:

```
{
  "ers_anc_endpoint": {
    "id": "5810ed0b-f1e8-40dc-bbda-78dcda4ae33d",
    "link": {
      "href": "https://10.4.22.225:9060/ers/config/ancendpoint/5810ed0b-f1e8-40dc-bbda-78dcda4ae33d",
      "rel": "self",
      "type": "application/xml"
    },
    "macAddress": "00:0E:35:D4:D8:51",
    "policyName": "komand_test"
  }
}
```

#### Query Endpoint
  
This action is used to query an endpoint for more information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|True|The hostname or MAC of the endpoint|None|00:0E:35:D4:D8:52|
  
Example input:

```
{
  "hostname": "00:0E:35:D4:D8:52"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ers_endpoint|ERSEndPoint|False|Returns a JSON containing information on the host|{"id":"82e2b6d0-546b-11e8-bc94-12d1173c5b91","name":"00:0E:35:D4:D8:52","description":"","mac":"00:0E:35:D4:D8:52","profileId":"2ac6a950-8c00-11e6-996c-525400b48521","staticProfileAssignment":false,"groupId":"aa10ae00-8bff-11e6-996c-525400b48521","staticGroupAssignment":false,"portalUser":"","identityStore":"","identityStoreId":"","link":{"rel":"self","href":"https://10.4.22.225:9060/ers/config/endpoint/name/00:0E:35:D4:D8:52","type":"application/xml"}}|
  
Example output:

```
{
  "ers_endpoint": {
    "description": "",
    "groupId": "aa10ae00-8bff-11e6-996c-525400b48521",
    "id": "82e2b6d0-546b-11e8-bc94-12d1173c5b91",
    "identityStore": "",
    "identityStoreId": "",
    "link": {
      "href": "https://10.4.22.225:9060/ers/config/endpoint/name/00:0E:35:D4:D8:52",
      "rel": "self",
      "type": "application/xml"
    },
    "mac": "00:0E:35:D4:D8:52",
    "name": "00:0E:35:D4:D8:52",
    "portalUser": "",
    "profileId": "2ac6a950-8c00-11e6-996c-525400b48521",
    "staticGroupAssignment": false,
    "staticProfileAssignment": false
  }
}
```

#### Remove from Quarantine
  
This action is used to remove a host from quarantine

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|mac_address|string|None|True|The host MAC address|None|00:0E:35:D4:D8:52|
  
Example input:

```
{
  "mac_address": "00:0E:35:D4:D8:52"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Returns true in the endpoint was removed from quarantine|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|None|Hyper text reference|None|
|Rel|string|None|None|Rel|None|
|Type|string|None|None|Type|None|
  
**ErsAncEndpoint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|ERS endpoint ID|None|
|Link|link|None|None|Link|None|
|MAC Address|string|None|None|ERS endpoint MAC address|None|
|Policy Name|string|None|None|Name of the policy applied to the ERS endpoint|None|
  
**ERSEndPoint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Group ID|string|None|None|Group ID|None|
|ID|string|None|None|ID|None|
|Identity Store|string|None|None|Identity store|None|
|Identity Store ID|string|None|None|Identity store ID|None|
|Link|link|None|None|Link|None|
|MAC|string|None|None|MAC|None|
|Name|string|None|None|Name|None|
|Portal User|string|None|None|Portal User|None|
|Profile ID|string|None|None|Profile ID|None|
|Static Group Assignment|boolean|None|None|Static group assignment|None|
|Static Profile Assignment|boolean|None|None|Static profile assignment|None|
  
**ANCEndpoint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|ANC endpoint ID|None|
|Link|link|None|None|ANC endpoint link|None|
|MAC Address|string|None|None|MAC Address of ANC endpoint|None|
|Policy Name|string|None|None|Policy Name|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 2.2.3 - Updated SDK to the latest version
* 2.2.2 - Update requests to version 2.20.0
* 2.2.1 - New spec and help.md format for the Extension Library
* 2.2.0 - New action Get ANC Endpoint
* 2.1.2 - Fixed issue where Query Endpoint would return an error if endpoint was not found | Update to input description for Query Endpoint
* 2.1.1 - Fixed issue where error message wasn't printed correctly in case of failure
* 2.1.0 - New action Remove from Quarantine
* 2.0.0 - Support web server mode | Add SSL verification support
* 1.0.0 - Initial plugin

# Links

* [Cisco Developer Documentation](https://developer.cisco.com/docs/)

## References

* Cisco ISE API can be found at <your Cisco ISE server address>:9060/ers/sdk
* [Cisco ISE](https://www.cisco.com/c/en/us/products/security/identity-services-engine/index.html)
* [ISE Library](https://github.com/bobthebutcher/ise)


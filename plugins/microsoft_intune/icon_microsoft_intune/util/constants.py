GET_AUTOPILOT_DEVICE_ENDPOINT = "deviceManagement/windowsAutopilotDeviceIdentities/{device_id}"
GET_MANAGED_APP_ENDPOINT = "deviceAppManagement/mobileApps/{app_id}"
GET_MANAGED_APPS_ENDPOINT = "deviceAppManagement/mobileApps"
GET_MANAGED_DEVICE_ENDPOINT = "deviceManagement/managedDevices/{device_id}"
GET_MANAGED_DEVICES_ENDPOINT = "deviceManagement/managedDevices"
MANAGED_DEVICE_ACTION_ENDPOINT = "deviceManagement/managedDevices/{device_id}/{action}"
SCAN_DEVICE_ENDPOINT = "deviceManagement/managedDevices/{device_id}/windowsDefenderScan"
WINDOWS_AUTOPILOT_DEVICE_ENDPOINT = "deviceManagement/windowsAutopilotDeviceIdentities/{device_id}"
WINDOWS_DEFENDER_SIGNATURES_ENDPOINT = "deviceManagement/managedDevices/{device_id}/windowsDefenderUpdateSignatures"
WIPE_DEVICE_ENDPOINT = "deviceManagement/managedDevices/{device_id}/wipe"


class AuthType:
    username = "Username-Password"
    client = "Client-Credentials"

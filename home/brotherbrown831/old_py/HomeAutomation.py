from org.myrobotlab.net import BareBonesBrowserLaunch


def outsideLights(value):
  if value = 1
    BareBonesBrowserLaunch.openURL("http://ip_address:3480/data_request?id=action&output_format=xml&DeviceNum=6&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=01")
  else 
    BareBonesBrowserLaunch.openURL("http://ip_address:3480/data_request?id=action&output_format=xml&DeviceNum=6&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0")

def garageLights(value):
  if value = 1
    BareBonesBrowserLaunch.openURL("http://ip_address:3480/data_request?id=action&output_format=xml&DeviceNum=6&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=01")
  else 
    BareBonesBrowserLaunch.openURL("http://ip_address:3480/data_request?id=action&output_format=xml&DeviceNum=6&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=0")    
  
  def alarmOn(value):
    BareBonesBrowserLaunch.openURL("http://ip_address:3480/data_request?id=action&output_format=xml&DeviceNum=6&serviceId=urn:upnp-org:serviceId:SwitchPower1&action=SetTarget&newTargetValue=01")

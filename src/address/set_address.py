import os

def SetAddress():
  local = False
  address = os.getenv("ADDRESS")
  if(address == "local"):
    local = True
    url = "http://localhost"
  else:
    url = "http://" + address
  return url , local
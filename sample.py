from datetime import datetime
import json

class OmronSample:
  excluded = ["device","time_measured"]

  def __init__(self,device):
    self.device = device;
  
  def update(self, data):
    #self.time_measured = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    self.temperature = str(int(hex(data[9]) + '{:02x}'.format(data[8], 'x'), 16) / 100)
    self.relative_humidity = str(int(hex(data[11]) + '{:02x}'.format(data[10], 'x'), 16) / 100)
    self.ambient_light = str(int(hex(data[13]) + '{:02x}'.format(data[12], 'x'), 16))
    
    self.barometric_pressure = str(int(hex(data[17]) + '{:02x}'.format(data[16], 'x')
                                  + '{:02x}'.format(data[15], 'x') + '{:02x}'.format(data[14], 'x'), 16) / 1000)
    self.sound_noise = str(int(hex(data[19]) + '{:02x}'.format(data[18], 'x'), 16) / 100)
    self.eTVOC = str(int(hex(data[21]) + '{:02x}'.format(data[20], 'x'), 16))
    self.eCO2 = str(int(hex(data[23]) + '{:02x}'.format(data[22], 'x'), 16))
    self.discomfort_index = str(int(hex(data[25]) + '{:02x}'.format(data[24], 'x'), 16) / 100)
    self.heat_stroke = str(int(hex(data[27]) + '{:02x}'.format(data[26], 'x'), 16) / 100)
    self.vibration_information = str(int(hex(data[28]), 16))
    self.si_value = str(int(hex(data[30]) + '{:02x}'.format(data[29], 'x'), 16) / 10)
    self.pga = str(int(hex(data[32]) + '{:02x}'.format(data[31], 'x'), 16) / 10)
    self.seismic_intensity = str(int(hex(data[34]) + '{:02x}'.format(data[33], 'x'), 16) / 1000)
    
  def __str__(self):
    return str(self.time_measured+" "+self.temperature)

  def databoom_message(self):
    data = { 
	"type": "data",\
        "message": { 
        "device": self.device,\
	"signals" : []
        }
    }
    fields=(self.__dict__)
    for f in fields:
      if f not in self.excluded:
        s = {
	  "name": f,\
	  "value":getattr(self,f)\
        }
        data["message"]["signals"].append(s)
    return json.dumps(data)

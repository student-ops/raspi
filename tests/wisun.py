import sys
sys.path.append('../src')

from aruduino_sync import witemp 

if __name__ == '__main__':
  temp = str(witemp.readTemp())
  text = "今の気温は" + temp +"℃です"
  print(text)





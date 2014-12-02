# Aira 
#### A Webapp that tracks temperature and humidity.

<img src="http://i.imgur.com/4nnrstW.png" alt="Screnshot" style="width:200px;height:auto;margin:0 auto;">

### Hardware Requirement

- Raspberry Pi
- DHT_22 Sensor


### Installation


To use this Webapp, you need to create a Xively account on [http://xively.com](http://xively.com). You will need to grab your Feed ID and API key.

To setup Aira, you need to add your Feed ID and your API key in script.js and air.py.

`script.js`

			var feedID = YOUR_FEED_ID; //#CHANGE IT
			var key = "YOUR_KEY"; //#CHANGE IT


`air.py`

			FEED_ID = "YOUR_FEED_ID" #CHANGE IT
			API_KEY = "YOUR_KEY" #CHANGE IT

Place the `wind` folder on your Raspberry Pi (/home/pi). And run these commands :

		cd wind
		chmod 755 launcher.sh
		sudo crontab -e
		@reboot sh /home/pi/wind/launcher.sh
		sudo reboot

Place the `sun` folder on any Web Server.

### Ressources:

[Reset.css](http://meyerweb.com/eric/tools/css/reset/), from Eric Meyer.

[Air.py](https://greenpihouse.wordpress.com/2013/10/25/rspberry-pi-dht22-xively/), from RaspberryPi Greenhouse.

[DHT Driver](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_DHT_Driver), from Adafruit.



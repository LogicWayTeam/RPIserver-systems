# Overview of Coоling system 

Run indication script. If press the button, that connected to 17 BCM and GND, еhen the PWR led will light up.

```bash 
python /home/../indication-system/main_indication.py
```

Put it on the offload for Rasbian OS.

```bash
sudo nano /etc/rc.local
```

```bash
...
sudo python /home/../indication-system/main_indication.py &

exit 0
```
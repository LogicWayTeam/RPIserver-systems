# Overview of Coоling system 

Display actual temperature one time.

```bash
vcgencmd measure_temp
```

Put it on the offload for Rasbian OS.

```bash
sudo nano /etc/rc.local
```
```bash
...
sudo python /home/../cooling-system/main_cooling.py &
exit 0
```

### Test cooling system by loading 4 cores

```bash
sudo apt-get install sysbench
```
```bash
sysbench --num-threads=4 --test=cpu --cpu-max-prime=20000 --validate run
```

And track temperature by this script.

```bash
python /home/../cooling-system/display_temp.py
```
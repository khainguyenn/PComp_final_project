import grovepi
import time
import subprocess

air_sensor = 0
gas_sensor = 1

grovepi.pinMode(air_sensor, "INPUT")
grovepi.pinMode(gas_sensor, "INPUT")

print("=== Air Quality Monitor ===")
print("Ctrl+C to stop\n")

last_spoken = 0
warning_active = False

def speak(text):
    subprocess.call('espeak -a 200 -s 130 --stdout "' + text + '" | aplay -D plughw:1,0', shell=True)

try:
    while True:
        try:
            air = grovepi.analogRead(air_sensor)
            gas = grovepi.analogRead(gas_sensor)
            gas_density = round(gas / 1024 * 100, 1)

            if air > 700:
                air_status = "high pollution"
            elif air > 300:
                air_status = "low pollution"
            else:
                air_status = "fresh air"

            print(f"Air Quality : {air:4d} — {air_status.upper()}")
            print(f"Gas (MQ3)   : {gas:4d} ({gas_density}%)")
            print("-" * 40)

            # WARNING MODE
            if gas > 100:
                warning_active = True
                print("⚠️  WARNING: High gas detected!")
                speak("Warning! Gas level is too high!")
                time.sleep(2) 

            else:
                if warning_active:
                    warning_active = False
                    last_spoken = 0 
                    speak("Gas level is back to normal.")

          
                now = time.time()
                if now - last_spoken >= 20:
                    message = f"The air quality now is {air_status}. Air quality value is {air}. Gas level is {gas_density} percent."
                    speak(message)
                    last_spoken = now

        except TypeError:
            print("Read error, retrying...")
        except IOError:
            print("IO error, retrying...")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopped.")

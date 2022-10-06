# Water - Water.mp3 (3.5l) - Drank - log
# Eyes - eyes.mp3 - Done Every 30 min Done EyDone - log
# Physical activity - physical.mp3 Every 45 min Done ExDone - Done

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(True):
        a = input("")
        if a == stopper:
            mixer.music.stop()
            break 

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("Drinkwater.mp3", "stop")  
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40 * 60
    eyessecs = 20 * 60
    exercisesecs = 10 * 60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time,Please drink 1 glass of water. Enter 'drank' to stop the alarm")
            musiconloop('Drinkwater.mp3', 'drank')
            init_water = time()
            log_now("Drank water at")
        
        if time() - init_eyes > eyessecs:
            print("Eyes exericse time,Please do Eye exercise atleast 5 min. Enter 'doneeyes' to stop the alarm")
            musiconloop('EyeRingtone.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes relaxed at")

        if time() - init_exercise > exercisesecs:
            print("Exercise time,Please do Physical activity atleast 5 min Enter 'doneexercise' to stop the alarm")
            musiconloop('Physical.mp3', 'doneexercise')
            init_exercise = time()
            log_now("Physical activity Done at")    
 

import sys
import time
import speech_recognition
import speech_recognition as sr
import re
from cflib.positioning.motion_commander import MotionCommander

def voice_commander(scf):
    if re.findall(r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*' + 'Прямо' + r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*',
                  transcript, re.IGNORECASE):
     forward(scf)
     voice_commander(scf)
    elif re.findall(r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*' + 'Назад' + r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*',
                  transcript, re.IGNORECASE):
     back(scf)
     voice_commander(scf)
    elif re.findall(r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*' + 'Вверх' + r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*',
                  transcript, re.IGNORECASE):
     up(scf)
     voice_commander(scf)
    elif re.findall(r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*' + 'Вниз' + r'[А-Яа-яA-Za-z0-9% ,\-\"«»\[\]\']*',
                  transcript, re.IGNORECASE):
     down(scf)
     voice_commander(scf)
        



def forward():
    motion_controller = MotionCommander(scf)
    motion_controller.take_off()
    motion_controller.forward(1)
    time.sleep(1)

def back():
    motion_controller = MotionCommander(scf)
    motion_controller.take_off()
    motion_controller.back(1)
    time.sleep(1)

def up():
    motion_controller = MotionCommander(scf)
    motion_controller.take_off()
    motion_controller.up(1)
    time.sleep(1)

def down():
    motion_controller = MotionCommander(scf)
    motion_controller.take_off()
    motion_controller.down(1)
    time.sleep(1)


if __name__ == '__main__':
    index = 0
    srr = sr.Recognizer()
    mic = sr.Microphone()

    cflib.crtp.init_drivers()
    with SyncCrazyflie(uri, cf=CrazyLogger(create_lg_stab(), rw_cache='./cache')) as scf:
        voice_commander(scf)

    while True:
        with mic as sourse:
            try:
                srr.energy_threshold = 900
                srr.adjust_for_ambient_noise(sourse)
                audio = srr.listen(sourse)
                transcript = srr.recognize_google(audio, language='ru-RU')
                print(transcript)
            except speech_recognition.UnknownValueError:
                pass

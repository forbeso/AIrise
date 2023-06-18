from gtts import gTTS
import openai
from time import sleep
from datetime import datetime
import random

#YYYY-MM-DD HH:MM:SS.ssssss
# Insert your OpenAI API key here
openai.api_key = ""


class Alarm:

  def __init__(self, time: datetime, phrase: str, accent: str,
               phrase_type: str):
    self.time = time
    self.phrase = phrase
    self.accent = accent
    self.phrase_type = phrase_type

  def show_alarm_details(self):
    print(f"Time: {self.time} \nPhrase: {self.phrase} \nAccent: {self.accent}")

  def set_time(self, time: datetime):
    self.time = time

  def set_phrase(self, phrase: str):
    self.phrase = phrase

  def set_phrase_type(self, phrase_type: str):
    self.phrase_type = phrase_type

  def set_accent(self, accent: str):
    self.accent = accent

  def play(self):
    pass


class AlarmManager:

  def __init__(self):
    self.alarms = []

  def add_alarm(self, alarm: Alarm):
    self.alarms.append(alarm)

  def remove_alarm(self, alarm: Alarm):
    try:
      self.alarms.remove(alarm)
    except ValueError:
      print("Alarm not found")

  def update_alarm(self, alarm: Alarm, new_time: datetime, new_phrase: str):
    alarm.set_time(new_time)
    alarm.set_phrase(new_phrase)

  def get_alarms(self):
    for alarm in self.alarms:
      print("\n")
      alarm.show_alarm_details()


def generate_phrase(prompt):
  response = openai.Completion.create(engine="text-davinci-003",
                                      prompt=prompt,
                                      max_tokens=2048,
                                      temperature=0.8)
  #sleep(5)
  print(response)
  return response["choices"][0]["text"]


phrase_type = "motivational"

prompt = f"Wake me up in a {phrase_type} way. You should clear your throat first. You know, so you don't startle me. Tell  me how great my day is going to be. Get me pumped to take on my goals"

response = generate_phrase(prompt)

alarm1 = Alarm(time=datetime.now(),
               phrase=response,
               phrase_type=phrase_type,
               accent="en-us")
alarm2 = Alarm(time=datetime.now(),
               phrase="Wakey Wakey!",
               phrase_type=phrase_type,
               accent="jp")

#alarm1.show_alarm_details()
alarm_man = AlarmManager()

alarm_man.add_alarm(alarm1)
alarm_man.add_alarm(alarm2)

alarm_man.get_alarms()

tts = gTTS(response, lang='en-us')
filename = "wake_up_phrase.mp3"
tts.save(filename)

print("audio generated")

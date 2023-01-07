
def import_message():
    print(f"Subsystem ${__name__} imported successfully!")

import pyttsx3

class TTS:
    def __init__(self):
        self.tts_engine = pyttsx3.init()

    def select_voice(self):
        import os

        index_file_path = "./voice_index.txt"

        if not os.path.exists(index_file_path) or os.path.getsize(index_file_path) == 0:
            voices_list = self.tts_engine.getProperty("voices")

            for index, voice in enumerate(voices_list):
                print(f"{index}: {voice.name}")

            voice_index = str(int(input("Select voice you want to use: ")))

            if int(voice_index) not in range(0, len(voices_list) - 1, 1):
                print("Invalid voice index!")

                self.select_voice()

            else:
                self.tts_engine.say(f"You selected voice number {voice_index}.")
                self.tts_engine.runAndWait()

                self.tts_engine.say("Are you sure you want to use this voice?")
                self.tts_engine.runAndWait()

                confirmation_flag = str(input("Are you sure you want to use this voice? "))

                if confirmation_flag == "yes" or confirmation_flag == "y":
                    with open(index_file_path, "w") as index_file:
                        index_file.write(voice_index)

        else:
            with open(index_file_path, "r") as index_file:
                voice_index = int(index_file.read())

if __name__ != "__main__":
    import_message()
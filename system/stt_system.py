
def import_message():
    print(f"Subsystem ${__name__} imported successfully!")

import speech_recognition

class STT:
    def __init__(self):
        pass

    def select_microphone(self):
        import os

        index_file_path = "./microphone_index.txt"

        if not os.path.exists(index_file_path) or os.path.getsize(index_file_path) == 0:
            devices = speech_recognition.Microphone.list_microphone_names()

            for index, microphone in enumerate(devices):
                print(f"{index}: Microphone {microphone}")

            device_index = str(int(input("Select microphone you want to use: ")))

            if int(device_index) not in range(0, len(devices) - 1, 1):
                print("Invalid device index!")

                self.select_microphone()

            else:
                with open(index_file_path, "w") as index_file:
                    index_file.write(device_index)

        else:
            with open(index_file_path, "r") as index_file:
                device_index = int(index_file.read())

if __name__ != "__main__":
    import_message()
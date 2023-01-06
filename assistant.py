
class VoiceAssistant:
    def __init__(self):
        self.VA_VERSION_MAJOR = va_config.VA_VERSION_MAJOR
        self.VA_VERSION_MINOR = va_config.VA_VERSION_MINOR

        self.VA_VERSION = f"{self.VA_VERSION_MAJOR}.{self.VA_VERSION_MINOR}"

if __name__ == "__main__":

    import config as va_config

    import system.tts_system as tts_system
    import system.stt_system as stt_system
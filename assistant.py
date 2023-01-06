
class VoiceAssistant:
    def __init__(self):
        self.VA_VERSION_MAJOR = va_config.VA_VERSION_MAJOR
        self.VA_VERSION_MINOR = va_config.VA_VERSION_MINOR

        self.VA_VERSION = f"{self.VA_VERSION_MAJOR}.{self.VA_VERSION_MINOR}"

    def initialize_subsystems(self):
        self.tts_subsystem = tts_system.TTS()
        self.stt_subsystem = stt_system.STT()

    def initialize_commands(self):
        import commands.greeting

if __name__ == "__main__":
    import config as va_config

    import system.tts_system as tts_system
    import system.stt_system as stt_system

    voice_assistant = VoiceAssistant()

    voice_assistant.initialize_subsystems()
    voice_assistant.initialize_commands()

    voice_assistant.stt_subsystem.select_microphone()
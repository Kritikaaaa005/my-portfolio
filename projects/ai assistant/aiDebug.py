# assistant_debug.py
import sys
import subprocess

def powershell_speak(text):
    # fallback using Windows PowerShell System.Speech
    cmd = [
        "powershell",
        "-Command",
        "Add-Type -AssemblyName System.Speech; "
        f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
    ]
    try:
        subprocess.call(cmd, shell=False)
    except Exception as e:
        print("PowerShell fallback failed:", e)

# Try pyttsx3 first and show debug info
def test_pyttsx3():
    try:
        import pyttsx3
    except Exception as e:
        print("Could not import pyttsx3:", e)
        return False

    try:
        engine = pyttsx3.init()
    except Exception as e:
        print("pyttsx3.init() failed:", e)
        return False

    try:
        voices = engine.getProperty('voices')
        print("Available voices:", [getattr(v, 'name', str(v)) for v in voices])
    except Exception as e:
        print("Could not list voices:", e)

    try:
        print("pyttsx3: attempting to say a test phrase...")
        engine.say("This is a test from pyttsx three.")
        engine.runAndWait()
        print("pyttsx3 speak finished (no errors).")
        return True
    except Exception as e:
        print("pyttsx3 speak failed:", e)
        return False

if __name__ == "__main__":
    ok = test_pyttsx3()
    if not ok:
        print("\npyttsx3 failed — trying PowerShell fallback (this does not need extra pip installs)...")
        powershell_speak("This is a fallback test using PowerShell.")
    else:
        print("\npyttsx3 seems to work. If your assistant still does not speak, check your system volume and default audio device.")
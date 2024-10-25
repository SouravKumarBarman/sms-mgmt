import subprocess

def start_session(session_name):
    try:
        subprocess.run(["screen", "-dmS", session_name, "python3", "program.py"])
        return True
    except Exception as e:
        print(f"Error starting session: {e}")
        return False

def stop_session(session_name):
    try:
        subprocess.run(["screen", "-S", session_name, "-X", "quit"])
        return True
    except Exception as e:
        print(f"Error stopping session: {e}")
        return False

def restart_session(session_name):
    stop_session(session_name)
    return start_session(session_name)

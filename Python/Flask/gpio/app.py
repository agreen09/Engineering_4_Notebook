from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    led1 = GPIO.input(17)
    led2 = GPIO.input(18)
    if request.method == "POST":
        print(request.form)
        if('hiddenElement1' in request.form):
            print("LED 1")
            if(led1 == True):
                GPIO.output(17, GPIO.LOW)
                msg1 = "LED 1 is off"
                checked1 = ""
            else:
                GPIO.output(17, GPIO.HIGH)
                msg1 = request.form.get("submitBtn")
                checked1 = "checked"
            if(led2 == True):
                msg2 = "LED 2 is on"
                checked2 = "checked"
            else:
                msg2 = "LED 2 is off"
                checked2 = ""
        else:
            if(led2 == True):
                GPIO.output(18, GPIO.LOW)
                msg2 = "LED 2 is off"
                checked2 = ""
            else:
                GPIO.output(18, GPIO.HIGH)
                msg2 = request.form.get("submitBtn")
                checked2 = "checked"
            if(led1 == True):
                msg1= "LED 1 is on"
                checked1 = "checked"
            else:
                msg1 = "LED 1 is off"
                checked1 = ""
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        msg1 = "LED 1 is off"
        msg2 = "LED 2 is off"
        checked1 = ""
        checked2 = ""
    return render_template(
        "index.html",
        msg1=msg1,
        msg2=msg2,
        checked1=checked1,
        checked2=checked2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

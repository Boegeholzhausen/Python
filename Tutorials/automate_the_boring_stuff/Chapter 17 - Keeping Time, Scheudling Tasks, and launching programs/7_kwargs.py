import threading

threadObj = threading.Thread(target=print, args=["penis", "noch ein Penis", "ein weiterer Penis"], kwargs={"sep": " & "})

threadObj.start()
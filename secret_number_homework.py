secret = 7

guess = raw_input("Gib eine Zahl ein: ")

while secret != int(guess):
   guess = raw_input("Falsche Zahl, neue Eingabe: ")
if int(guess) == secret:
       print "Gratulation, geheime Zahl gefunden"

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("prachi.17cs@cmr.edu.in","poushi2000")
message = "hello friend"
server.sendmail("sriharsha8811@gmail.com","sriharsha8811@gmail.com", message)
print("sss")
server.quit()


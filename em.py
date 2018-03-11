import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("prachi.17cs.cmr.edu", "poush")
message = "hii!"
s.sendmail("prachi.17cs@cmr.edu.in", "vibhasree49@gmail.com", message)
s.quit()


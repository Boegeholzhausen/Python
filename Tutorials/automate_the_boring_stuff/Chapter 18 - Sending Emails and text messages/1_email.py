import smtplib

conn = smtplib.SMTP("smtp.gmail.com", 587)
print(type(conn))

print(conn)
print(conn.ehlo())
print(conn.starttls())
# print(conn.login("jannisboeg@gmail.com", "Uzk5NpY98"))
# conn.sendmail("jannisboeg@gmail.com", "jannis1210@gmail.com")
conn.quit()
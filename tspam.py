import smtplib
gmail_user='tmoy.nandy@gmail.com'
gmail_password='8420309494711227'


for x in range(0,25):

	FROM = gmail_user  
	to = ['000webhost.com']  
	subject = 'Website down'  
	body = 'My website was up and running fine and suddenly it shows  "there is nothing here yet" message and its not working anymore.Its an emergency of sorts to keep my site up and running for a week.Please solve the problem asap.The website is : https://21121996.000webhostapp.com/\n\n- Tanumoy nandy'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s"""  % (FROM, ", ".join(to), subject, body)

	try:
        	server=smtplib.SMTP("smtp.gmail.com",587)
        	server.ehlo()
        	server.starttls()
        	server.login(gmail_user,gmail_password)
        	server.sendmail(FROM,to,email_text)
        	server.close()
        	print('email sent')

	except:
        	print('something went wrong')

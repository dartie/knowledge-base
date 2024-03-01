# Send email with Django


## Links
* https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html
* https://www.tutorialspoint.com/django/django_sending_emails.htm


## Settings
1. Edit ````settings.py```` adding the following settings


1. If you have activated two-step verification, you need to turn that off. Also, you can try another thing: 
  * Go to https://www.google.com/settings/security/lesssecureapps and https://myaccount.google.com/security?pli=1#connectedapps, allow access for the less secure app. 
     Google might consider your server's sign-in process as less secure sign-in technology, which makes your account more vulnerable. So allowing access might help you.




## Send email
### No attachment
  ````python
  # send license to email: "subject", "message", "from", ["to"], fail_silently=False, html_message=True
  email_subject = "License generated #{id_lic} - {Customer} - {Deal}".format(id_lic=record_id, Customer=info_dict['Customer_info'], Deal=info_dict['Deal_info'])
  email_message = "Please see license attached.\\n\\nBest Regards,\\nLicense"  # TODO: set
  email_from = "licenses@prqa.com"
  email_to = ['licenses@prqa.com']
  send_mail(email_subject, email_message, email_from, email_to, fail_silently=False, html_message=True)
  ````


### With attachment
  ````python
  # send license to email: "subject", "message", "from", ["to"], fail_silently=False, html_message=True
  email_subject = "License generated #{id_lic} - {Customer} - {Deal}".format(id_lic=record_id, Customer=info_dict['Customer_info'], Deal=info_dict['Deal_info'])
  email_message = "Please see license attached.\\n\\nBest Regards,\\nLicense"  # TODO: set
  email_from = "licenses@prqa.com"
  email_to = ['licenses@prqa.com']


  email = EmailMessage(email_subject, email_message, email_from, email_to)
  email.content_subtype = "html"
  
  fd = open(license_signed_fullfilename, 'r')
  email.attach(license_filename, fd.read(), 'text/plain')
  
  res = email.send()
  ````




## Send email with attachment not text
  ````python
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate




def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    assert isinstance(send_to, list)


    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject


    msg.attach(MIMEText(text))


    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)




    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


  ````
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0NzQxNjUzM119
-->

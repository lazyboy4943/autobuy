import smtplib 

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('ispsinstock@gmail.com', 'ispsinstock123')


    subject = 'In Stock!!!! (Test)'
    body = 'Buy the Playstation NOW!!!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail('ispsinstock@gmail.com', 'ispsinstock@gmail.com', msg)
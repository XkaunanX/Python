import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Datos del correo
to = "usuario@dominio.com"
subject = "Tarea Completada"
body = "La tarea ha sido completada con éxito."

# Configuración del servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "tu_email@gmail.com"
sender_password = "tu_contraseña"

# Configurar el mensaje
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Enviar el correo
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Cifrar la conexión
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, msg.as_string())

print(f"Notificación enviada a {to}")

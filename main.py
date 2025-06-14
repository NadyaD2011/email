from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


import smtplib as smtp
import os


def send_msg(email_from, password, email_to, msg):
    server = smtp.SMTP_SSL('smtp.yandex.ru:465')
    server.login(email_from, password)
    server.sendmail(to_addrs=email_to, from_addr=email_from, msg=msg)
    server.quit()


def write_email(email_from, email_to):
    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = "Тестовое письмо"

    process_module = ['Основы Python', 'Github', 'API']
    complet_module = ['Командная строка', 'Введение в JS', 'WEB-разработка', 'Введение в Python']
    learn_time = '3 месяца'

    if complet_module != []:
        text_message = f'Привет, Мама(Папа), я занимаюсь в школе третье место уже {learn_time}. В процессе я выполнил модули: {complet_module}! Сейчас я работаю над модулями {process_module}. Обучение мне нравится, я получил море знаний!'
        msg.attach(MIMEText(text_message, "plain"))
    else:
        text_message = f"Привет, Мама(Папа), я занимаюсь в школе третье место уже {learn_time}. Сейчас я работаю над модулями {process_module}. Пока что я улучшаю свои навыки и узнаю много нового!"
        msg.attach(MIMEText(text_message, "plain"))

    msg = msg.as_string()

    return msg


def main():
    load_dotenv()

    password = os.environ['PASSWORD']
    email_from = "dikovich-88@yandex.ru"
    email_to = "nadya.dikovitch@yandex.ru"

    msg = write_email(email_from, email_to)
    send_msg(email_from, password, email_to, msg)


if __name__ == "__main__":
    main()
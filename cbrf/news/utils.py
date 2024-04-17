from django.core.mail import send_mail
from companies.models import Organisation

def send_email_to_organization(feedback):
    organization = feedback.organization
    subject = 'Обращение от клиента'
    message = f'Здравствуйте, {organization.name_short}!\n\nПоступило новое обращение от клиента:\n\n'
    message += f'ФИО: {feedback.full_name}\n'
    message += f'Номер договора: {feedback.contract_number}\n'
    message += f'Дата договора: {feedback.contract_date}\n'
    message += f'Текст обращения:\n{feedback.message}\n\n'
    message += 'С уважением,\nВаш сайт'
    sender = 'your@email.com'  # Замените на вашу электронную почту
    recipient = organization.email
    send_mail(subject, message, sender, [recipient])
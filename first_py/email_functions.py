from botcity.plugins.email import BotEmailPlugin

def ler_email(usuario: str, senha: str, assunto: str) -> list:
    """
    Função para ler e-mails de uma conta do Gmail com base em um assunto.
    Args:
        usuario (str): O endereço de e-mail do usuário.
        senha (str): A senha do e-mail do usuário.
        assunto (str): Assunto a ser procurado.
    Returns:
        list: Lista de e-mails encontrados.
    """

    email = BotEmailPlugin.config_email(MailServers.GMAIL, usuario, senha)

    messages = email.search(f'SUBJECT "{assunto}"')

    emails_info = []

    for msg in messages:
        email_data = {
            "Date": msg.date_str,
            "From": msg.from_,
            "Message": msg.text
        }
        emails_info.append(email_data)

    return emails_info

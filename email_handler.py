import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_with_attachment(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, login, password):
    try:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as attachment_file:
                attachment = MIMEApplication(attachment_file.read(), _subtype="octet-stream")
                attachment.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment_path)}'
                )
                msg.attach(attachment)
        else:
            print(f"Attachment file '{attachment_path}' does not exist.")

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    send_email_with_attachment(
        sender_email="youremail@example.com",
        receiver_email="recipient@example.com",
        subject="Test Email with Attachment",
        body="Please find the attachment below.",
        attachment_path="path/to/your/file.txt",
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        login="youremail@example.com",
        password="yourpassword"  # Use app password if applicable
    )

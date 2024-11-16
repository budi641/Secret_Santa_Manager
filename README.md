
# Secret Santa Python Program

This Python program facilitates a Secret Santa activity by randomly assigning each participant a person to buy a gift for and then sending them an email with their assignment.

## Features

- Input the names and emails of participants.
- Randomly assign each participant a Secret Santa.
- Send personalized emails to each participant with their Secret Santa assignment.
  
## Requirements

Before running the program, make sure you have the following dependencies installed:

- Python 3.x
- `smtplib` and `random` (standard Python libraries)
- `email.mime.text` and `email.mime.multipart` (standard Python libraries)

If you need to install any extra libraries for email sending, you can do so using pip:

```bash
pip install secure-smtplib
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/budi641/Secret_Santa_Manager.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Secret_Santa_Manager
   ```

3. In the `secret_santa.py` script, input the names and email addresses of all participants in the `participants` dictionary. Example:

   ```python
   participants = {
       'Alice': 'alice@example.com',
       'Bob': 'bob@example.com',
       'Charlie': 'charlie@example.com',
       # Add more participants here
   }
   ```

4. In the `send_email()` function, input your email credentials (either your email address and password, or use an app-specific password if using Gmail):

   ```python
   sender_email = "your_email@example.com"
   sender_password = "your_email_password"
   ```

   **Important:** For Gmail, you may need to enable "Less secure apps" or use an [app-specific password](https://support.google.com/accounts/answer/185833?hl=en).

## Running the Program

To run the program, execute the `secret_santa.py` script:

```bash
python secret_santa.py
```

The program will:
1. Randomly assign each participant a Secret Santa.
2. Send an email to each participant with the details of their assigned Secret Santa.

## Customization

- You can modify the email template in the `send_secret_santa_emails()` function to fit your needs.
- Add more participants to the `participants` dictionary as required.
- Adjust the subject and body of the emails to add more personal touches.

## Troubleshooting

1. **Email Sending Issues:**
   - If you're using Gmail, ensure that you have allowed access for less secure apps or are using an app-specific password.
   - If you're using a different email provider, ensure that your SMTP settings (e.g., server address, port) are correct.

2. **Participant List:**
   - Ensure that the `participants` dictionary is populated correctly with names as keys and emails as values.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Python Standard Library for `smtplib` and `random`.
- This project was created as part of a personal Secret Santa gift exchange program.
```

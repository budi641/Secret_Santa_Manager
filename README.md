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
   git clone https://github.com/budi641/Secret_Santa_Manager-python.git
   ```

2. Navigate to the project folder:

   ```bash
   cd Secret_Santa_Manager
   ```

3. In the `secret_santa.py` script, input the names and email addresses of all participants in the `participants` dictionary. Example:

   ```python
   participants = {
       'Ahmed': 'ahmed@example.com',
       'Ameen': 'ameen@example.com',
       'Mazen': 'mazen@example.com',
       # Add more participants here
   }
   ```

4. In the `send_email()` function, input your email credentials (either your email address and password, or use an app-specific password if using Gmail):

   ```python
   sender_email = "your_email@example.com"
   sender_password = "your_email_password"
   ```

   **Important:** For Gmail, you may need to follow the steps below if you're encountering authentication errors.

## Gmail Authentication Issues

If you're using Gmail as your email provider and encounter authentication errors (e.g., `535, b'5.7.8 Username and Password not accepted'`), there are several potential causes and solutions:

### 1. **Two-Factor Authentication (2FA) Enabled:**
If you have Two-Factor Authentication (2FA) enabled on your Gmail account, you cannot use your regular Gmail password for SMTP login. You will need to generate an **App Password**.

#### Steps to Generate an App Password:
1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
2. Under **"Signing in to Google"**, click on **"App passwords"**.
3. Select **"Mail"** for the app and **"Windows Computer"** (or your desired device) for the device.
4. Google will generate a 16-character password. Use this **App Password** in place of your regular Gmail password in the script.

### 2. **Allow Less Secure Apps:**
If you do not have 2FA enabled, you may need to enable access for less secure apps in your Google account to allow SMTP login. 

#### Solution:
- Go to the [Less secure apps settings page](https://myaccount.google.com/lesssecureapps).
- Turn on **"Allow less secure apps"**.

### 3. **Unlock Captcha:**
If Google blocks login attempts due to suspicious activity, you may need to unlock the CAPTCHA for Gmail SMTP login.

#### Solution:
- Visit [this CAPTCHA URL](https://accounts.google.com/DisplayUnlockCaptcha) to unlock access.
- After unlocking the CAPTCHA, try running the script again.

### 4. **Check for Account Security Issues:**
If you see security alerts from Google or face login issues, verify your account's security settings and review login activity. Google might block your login if it detects suspicious activity, and you may need to complete additional verification steps.

---

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

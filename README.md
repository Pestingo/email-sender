# Email Sender

📧 **Email Sender** is a Python script that allows you to send emails using the `smtplib` module. This project is perfect for anyone who needs a simple way to send emails programmatically.

## Features

- Send emails with customizable content
- Uses environment variables for secure handling of email credentials

## Prerequisites

- Python 3.x
- An email account (e.g., Gmail) with an app-specific password

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/email-sender.git
    cd email-sender
    ```

2. Set up environment variables for your email credentials:

    ### On Windows:
    ```sh
    set SENDER_EMAIL=your-email@gmail.com
    set SENDER_PASSWORD=your-app-password
    ```

    ### On macOS/Linux:
    ```sh
    export SENDER_EMAIL="your-email@gmail.com"
    export SENDER_PASSWORD="your-app-password"
    ```

    ### In PyCharm:
    - Open Run/Debug Configurations.
    - Add `SENDER_EMAIL` and `SENDER_PASSWORD` in the Environment variables field.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. Follow the prompts to enter the recipient's email and the email content.

## Example

```sh
Enter the email of the recipient:
recipient@example.com
Enter the content for the email:
This is a test email.

Contact
If you have any questions or suggestions, feel free to open an issue or contact me at pesterpestingo@gmail.com.


### Additional Steps

1. **Create a License**: Include a `LICENSE` file with the appropriate license text. For example, use the MIT License if you want others to freely use and modify your code.

2. **Create a .gitignore File**: Include a `.gitignore` file to exclude unnecessary files from your repository. For Python projects, you can use the following:

    ```text
    __pycache__/
    *.pyc
    .DS_Store
    .env
    ```

3. **Upload the Files to GitHub**:
    - Initialize the Git repository:
      ```sh
      git init
      ```
    - Add the files to the repository:
      ```sh
      git add .
      ```
    - Commit the changes:
      ```sh
      git commit -m "Initial commit"
      ```
    - Add the remote repository:
      ```sh
      git remote add origin https://github.com/yourusername/email-sender.git
      ```
    - Push the changes:
      ```sh
      git push -u origin master
      ```

### Python Script

Here is the Python script for sending emails:

```python
import smtplib
import os

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Securely get the sender email and password from environment variables
        sender_email = os.getenv('SENDER_EMAIL')
        sender_password = os.getenv('SENDER_PASSWORD')
        
        if not sender_email or not sender_password:
            print("Error: Please set the SENDER_EMAIL and SENDER_PASSWORD environment variables.")
            return

        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, content)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    to = input("Enter the email of the recipient:\n")
    content = input("Enter the content for the email:\n")
    sendEmail(to, content)

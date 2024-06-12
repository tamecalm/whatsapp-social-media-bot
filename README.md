# WhatsApp Social Media Bot
This project is a WhatsApp bot integrated with social media functionalities such as post scheduling, analytics tracking, and content recommendations.
## Setup
1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/whatsapp-social-media-bot.git
   cd whatsapp-social-media-bot
   ```
2. **Create a virtual environment and activate it:**

   ```
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```
3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**

   ```
   export FLASK_APP=run.py
   export FLASK_ENV=development
   export SECRET_KEY=your_secret_key
   export DATABASE_URL=sqlite:///site.db
   export TWILIO_ACCOUNT_SID=your_twilio_account_sid
   export TWILIO_AUTH_TOKEN=your_twilio_auth_token
   export TWILIO_PHONE_NUMBER=your_twilio_phone_number
   ```
5. **Initialize the database:**

   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
6. **Run the application:**

   ```
   flask run
   ```
7. **Access the application in your browser at** `http://localhost:5000`

## Testing

To run unit tests:

```
python -m unittest discover -s tests
```
## Deployment

1. Create an account on Render (https://render.com/)
2. Add your project to a GitHub repository.
3. Connect your GitHub repository to Render.
4. Set up environment variables in Render dashboard.
5. Deploy your application on Render.

## Contributors

- John (@tamecalm)
  
## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

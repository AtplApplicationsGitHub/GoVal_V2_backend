from app import create_app

# Create app instance with default config
app = create_app()

if __name__ == "__main__":
    ssl_context = ('/etc/letsencrypt/live/dev.goval.app/fullchain.pem', '/etc/letsencrypt/live/dev.goval.app/privkey.pem')
    app.run(host='0.0.0.0', port=2053, debug=True, ssl_context=ssl_context)

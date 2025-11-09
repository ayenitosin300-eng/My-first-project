from pyngrok import ngrok
import subprocess
import time

# 1. Set your ngrok auth token
ngrok.set_auth_token("35CJwL75TKxPkzXUssIGvkicOvD_rv2wgY18rQeCcCqfvN3t")

# 2. Start your account_ui.py app (make sure it runs on port 5000)
process = subprocess.Popen(["python", "account_ui.py"])

# 3. Expose port 5000 through ngrok
public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")

# 4. Keep the tunnel open while your app runs
try:
    process.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    process.terminate()
    ngrok.disconnect(public_url)
    ngrok.kill()

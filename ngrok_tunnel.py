from pyngrok import ngrok
import time

# Expose port 5000
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Keep tunnel open
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Tunnel closed")

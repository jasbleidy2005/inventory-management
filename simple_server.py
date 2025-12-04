from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is working!"

if __name__ == '__main__':
    print("\n" + "="*50)
    print("SERVER STARTING...")
    print("Open: http://localhost:5000")
    print("="*50 + "\n")
    
    try:
        app.run(host='127.0.0.1', port=5000, debug=True)
    except Exception as e:
        print(f"ERROR: {e}")
        input("Press Enter to exit...")

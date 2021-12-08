from flask import Flask, render_template, request
from gen import gen_key, secret_key

app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reset')
def reset():
    txt = "-1,-1"
    f = open("keys.txt","w")
    f.write(txt)
    f.close()
    return('Reset.')

@app.route('/getkey', methods=["GET","POST"])
def submit():
    if request.method == "POST":
        f = open("keys.txt","r")
        txt = f.read().split(',')
        x = int(txt[0])
        y = int(txt[1])
        f.close()
        result = request.form
        t = result["type"]
        private_key = result["key"]
        
        if(t == "Sender"):
            x = gen_key(int(private_key))
            f = open("keys.txt","w")
            txt = str(x)+","+str(y)
            f.write(txt)
            f.close()
            if(y != -1):
                return('Your Private key is {} and your Public Key is {}'.format(private_key,y))
            else:
                return('Your Public Key has not been generated yet. Wait for the other user to upload theirs and refresh this page.')
        
        if(t == "Reciever"):
            y = gen_key(int(private_key))
            f = open("keys.txt","w")
            txt = str(x)+","+str(y)
            f.write(txt)
            f.close()
            if(x != -1):
                return('Your Private key is {} and your Public Key is {}'.format(private_key,x))
            else:
                return('Your Public Key has not been generated yet. Wait for the other user to upload theirs and refresh this page.')



if __name__ == "__main__":
    app.run()
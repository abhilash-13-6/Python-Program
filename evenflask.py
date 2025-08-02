from flask import Flask
app=Flask(__name__)

@app.route("/<int:number>")
def prime(number):
    primes=""
    for i in range(1,number+1):
        if(i%2==0):
         primes+=str(i)+","
    return primes

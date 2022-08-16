def announce(f):
    def wrapper():
        print("Calculating moments left to live...")
        f()
        print("Lifespan Analysis complete.")
    return wrapper

@announce
def timeLeft():
    print("312 years, 4 months, 271 days, 21 hours, 37 seconds.")
    
timeLeft()
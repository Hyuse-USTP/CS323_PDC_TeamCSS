import time

def cook_rice():
    print("  [Sequential] Cooking rice... (20 minutes)")
    for n in range(1, 21):
        print(f"{n} minute(s) elapsed") 
        time.sleep(1) 
    print("  [Sequential] Rice is done.")

def cook_egg():
    print("  [Sequential] Cooking egg... (6 minutes)")
    for n in range(1, 7):
        print(f"{n} minute(s) elapsed") 
        time.sleep(1) 
    print("  [Sequential] Egg is done.")

def main_sequential():
    print("~STARTING SEQUENTIAL EXECUTION~")
    start_time = time.time()
    
    cook_rice()
    cook_egg() 
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total Sequential Time: {total_time:.4f} minutes")

if __name__ == "__main__":
    main_sequential()

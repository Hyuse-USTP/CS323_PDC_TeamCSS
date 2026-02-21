import time
import threading


def cook_rice(results):
    start = time.time()
    print("  -> Starting to cook rice...")
    for i in range(1, 21): 
        time.sleep(1)
        print(f"[Rice] Still cooking... ({i}m / 20m)")
    print("  -> Rice is done.")
    results['rice'] = time.time() - start

def cook_egg(results):
    start = time.time()
    print("  -> Starting to cook egg...")
    for i in range(1, 7): 
        time.sleep(1)
        print(f"[Egg]  Still cooking... ({i}m / 5m)")
    print("  -> Egg is done.")
    results['egg'] = time.time() - start



def run_parallel():
    print("\n--- PARALLEL: Two Burners (Concurrent execution) ---")
    results = {}
    start_time = time.time()
    
    rice_worker = threading.Thread(target=cook_rice, args=(results,))
    egg_worker = threading.Thread(target=cook_egg, args=(results,))
    
    rice_worker.start()
    egg_worker.start()
    
    rice_worker.join()
    egg_worker.join()
    
    end_time = time.time()
    return end_time - start_time, results['rice'], results['egg']


if __name__ == "__main__":
    par_time, rice_time, egg_time = run_parallel()
    
    print("\n" + "="*40)
    print("PARALLEL EXECUTION REPORT")
    print("="*40)
    print(f"Rice Cooking Time:{rice_time:.4f} minutes")
    print(f"Egg Cooking Time:{egg_time:.4f} minutes")
    print(f"Total Parallel Time:{par_time:.4f} minutes")
import multiprocessing
import os
import sys
from collections import Counter
import time

def input_grades(num_students, num_subjects):
    matrix = []
    print(f"\n--- Grade Entry Phase ({num_students} students, {num_subjects} subjects each) ---")
    for i in range(num_students):
        while True:
            try:
                user_input = input(f"Student {i + 1}: Enter {num_subjects} grades: ").strip()
                grades = [float(g) for g in user_input.replace(',', ' ').split()]
                
                if len(grades) != num_subjects:
                    print(f"Error: You entered {len(grades)} grades. Please enter exactly {num_subjects}.")
                    continue
                    
                matrix.append(grades)
                break # Move to next student
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return matrix

def compute_gwa(grades):
    process_id = os.getpid()
    
    # Calculate GWA
    if not grades:
        gwa = 0.0
    else:
        gwa = sum(grades) / len(grades)
    
    # Format output
    print(f"[Process {process_id}] Processing: {grades} -> GWA: {gwa:.2f}")
    return process_id

def main():
    print("Multiprocessing Grade Calculator")
    
    while True:
        try:
            print("\n--- Configuration ---")
            n_students = int(input("How many students? "))
            n_subjects = int(input("How many subjects per student? "))
            
            max_cores = multiprocessing.cpu_count()
            n_cores = int(input(f"How many cores to use? (Available: {max_cores}): "))
            
            # Basic validation for cores
            if n_cores < 1:
                print("At least 1 core is required. Setting to 1.")
                n_cores = 1
            
            # 1. Input Phase
            student_matrix = input_grades(n_students, n_subjects)
            start = time.time()
            
            print(f"\n--- Processing Phase ({n_cores} Cores) ---")
            print(f"Main Process ID: {os.getpid()}")
            
            # 2. Execution (Parallelism)
            with multiprocessing.Pool(processes=n_cores) as pool:
                worker_logs = pool.map(compute_gwa, student_matrix, chunksize=1)
            
            end = time.time()

            # 3. Summary Phase
            print("\n--- Workload Summary ---")
            workload_count = Counter(worker_logs)
            for pid, count in workload_count.items():
                print(f"Worker PID {pid} handled {count} calculation(s).")
            
            print(f"Time Taken: {end - start:.6f} seconds")
            print("\n--- Batch Complete ---")
            
            # Check if user wants to continue
            if input("\nCalculate grades again? (y/n): ").lower().strip() != 'y':
                print("Exiting program.")
                break

        except ValueError:
            print("Invalid input. Please enter integers for configuration.")

if __name__ == "__main__":
    main()


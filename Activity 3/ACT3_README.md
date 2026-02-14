1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
    * Task parallelism is when multiple operations are being performed concurrently on the same object. It is demonstrated in the Part A of the lab activity where multiple deduction functions are performed concurrently on a single salary. It is more efficient than sequentially running each function because the program doesn't have to wait for one function to finish before proceeding to the next, reducing execution time.
    * Data parallelism is when one operation is performed on multiple objects simultaneously. This is demonstrated in the Part B of the lab activity, where a single payroll function is performed on five employees at once. The benefits of this are similar to task parallelism, where the program doesn't have to wait for the function to finish executing on one employee before proceeding to the next, therefore minimizing the time of execution.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
    * The module concurrent.futures provides high-level functions for asynchronously executing callables via an Executor. Utilizing the with statement to initialize an Executor is essential for robust resource management, as it automatically triggers a shutdown and joins threads or processes once the block concludes. For task execution, submit() provides granular control by returning Future objects, which are proxies for pending results that allow for status checking and asynchronous retrieval. Whereas map() facilitates efficient batch processing of iterables while maintaining strict result ordering. 

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?
    * True parallelism did not occur because what ThreadPoolExecutor provides is concurrency, not parallelism. ThreadPoolExecutor only executes using one core at a time, and with GIL, other threads must wait if one thread is currently running. Parallelism only happens when multiple cores are working simultaneously, which is made possible via ProcessPoolExecutor.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory
space separation and GIL behavior.
5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which
approach scales better and why?
6. Provide a real-world payroll system example. Indicate where Task Parallelism and
Data Parallelism would be applied, and which executor you would use.
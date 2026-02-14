from concurrent.futures import ThreadPoolExecutor

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

deduction_rates = [
    ("SSS", 0.045),
    ("PhilHealth", 0.025),
    ("Pag-IBIG", 0.02),
    ("WithholdingTax", 0.1)
]



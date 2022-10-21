import os
import subprocess
import time
import sys
import numpy as np


def run_test(testname: str, n: int):
  print(f"Running test {testname} for {n} iterations: ", end="")
  res = []
  for i in range(n):
    if i % 5 == 0:
      print(".", end ="", flush=True)

    start = time.time()
    subprocess.call(f"axsim.bat -testplusarg UVM_TESTNAME={testname} -sv_seed random", stdout = subprocess.DEVNULL)
    end = time.time()
    res.append(end-start)
  print()
  return res

if __name__ == "__main__":
  # Check if axsim has been created
  print(os.getcwd())
  os.chdir(sys.path[0])
  print(os.getcwd())

  if not os.path.exists("axsim.bat"):
    print("axsim.bat not yet created. Creating it now")
    start = time.time()
    subprocess.call("xvlog.bat -sv -L uvm -f vivadofiles.f")
    end = time.time()
    print(f"Read files for synthesis. Took {end-start} seconds")
    start = time.time()
    subprocess.call("xelab.bat top -a --incr -L uvm")
    end = time.time()
    print(f"Elaborated and created simulation executable. Took {end-start} seconds")

  print("Found simulation executable. Running tests")

  N = 50
  rnd = run_test("random_test", N)
  edge = run_test("edge_test", N)
  print(f"RANDOM test: Average: {np.mean(rnd)}, stdev: {np.std(rnd)}")
  print(f"EDGE test  : Average: {np.mean(edge)}, stdev: {np.std(edge)}")

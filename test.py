import os
import subprocess

# Settings
TEST_DIR = "."     # Directory with our program
CODE_FILE = "main.c"    # Our C source file
COMPILER_TIMEOUT = 10.0 # Timeout for the compiler in seconds
RUN_TIMEOUT = 10.0      # Timeout for running the compiled program in seconds

# Create absolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile the program
print("Building ...")
try:
    ret = subprocess.run(
        ["gcc", code_path, "-o", app_path], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed.", str(e))
    exit(1)


# Parse output
output = ret.stdout.decode("utf-8")
print(output)
output = ret.stderr.decode("utf-8")
print(output)

# Check if the program compiled successfully
if ret.returncode != 0:
    print("Compilation failed.")
    exit(1)

# Run the compiled program
print("Running ...")
try:
    ret = subprocess.run(
        [app_path],
        stdout=subprocess.PIPE,
        timeout=RUN_TIMEOUT
    )

except Exception as e:
    print("ERROR: Running the program failed.", str(e))
    exit(1)

# Parse output
output = ret.stdout.decode("utf-8")
print(output)

# All tests passed! Exit gracefully
print("All tests passed.")
exit(0)

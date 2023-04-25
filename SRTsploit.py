import subprocess
import json
import sys

if len(sys.argv) < 2:
    print("Please provide the Docker image name as an argument.")
    exit()

docker_image = sys.argv[1]


# To check if Docker Bench is successfully installed
try:
    subprocess.run(['docker-bench-security', '-h'], stdout=subprocess.DEVNULL)
except FileNotFoundError:
    print("Docker Bench Security is not installed. Installing now...")
    subprocess.run(['sh', './install_docker_bench.sh'])

# To check if Clair is sucessfully installed
try:
    subprocess.run(['clair-scanner', '--version'], stdout=subprocess.DEVNULL)
except FileNotFoundError:
    print("Clair is not installed. Installing now...")
    subprocess.run(['sh', './install_clair.sh'])

# To check if trivy is successfully installed
try:
    subprocess.run(['trivy', '--version'], stdout=subprocess.DEVNULL)
except FileNotFoundError:
    print("Trivy is not installed. Installing now...")
    subprocess.run(['sh', './install_trivy.sh'])

# To run Docker Bench 
print("Running Docker Bench Security...")
result = subprocess.run(['docker-bench-security', 'cis-docker-benchmark-4.0.0-level-1'], capture_output=True, text=True)
with open('docker_bench_results.json', 'w') as f:
    json.dump(result.stdout, f) #Output stored in JSON File

# To run Clair 
print("Running Clair...")
result = subprocess.run(['clair-scanner', '--json', 'clair_results.json', docker_image], capture_output=True, text=True)
with open('clair_results.json', 'w') as f:
    json.dump(result.stdout, f) #Output stored in JSON File

# To run Trivy 
print("Running Trivy...")
result = subprocess.run(['trivy', '--format', 'json', '-o', 'trivy_results.json', docker_image], capture_output=True, text=True)
with open('trivy_results.json', 'w') as f:
    json.dump(result.stdout, f) #Output stored in JSON File

print("Completed, check your findings")

print("Installing Docker Bench Security...")
subprocess.run(["curl", "-sSL", "https://raw.githubusercontent.com/docker/docker-bench-security/master/docker-bench-security.sh", "-o", "/usr/local/bin/docker-bench-security"])

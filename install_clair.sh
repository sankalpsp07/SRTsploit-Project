print("Installing Clair...")
subprocess.run(["curl", "-sSL", "https://github.com/quay/clair/", "-o", "/usr/local/bin/clair"])

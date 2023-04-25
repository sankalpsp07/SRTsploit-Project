print("Installing Trivy...")
subprocess.run(["curl", "-sSL", "https://github.com/aquasecurity/trivy", "-o", "/usr/local/bin/clair"])

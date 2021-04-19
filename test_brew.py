import subprocess

def test_brew():
    subprocess.run(["brew", "install", "git-annex"], check=True)

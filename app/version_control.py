import subprocess
import os


class VersionControl:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def run_git_command(self, command):
        """Runs a git command in the specified repository."""
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                text=True,
                capture_output=True,
                shell=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e.stderr}")
            return None

    def get_modified_files(self):
        """Returns a list of modified files in the repository."""
        output = self.run_git_command("git status --porcelain")
        if output:
            return [line[3:] for line in output.split("\n") if line]
        return []

    def get_file_diff(self, filename):
        """Returns the diff of a specific file."""
        return self.run_git_command(f"git diff {filename}")

    def stage_and_commit(self, message):
        """Stages all changes and commits them with a message."""
        self.run_git_command("git add .")
        self.run_git_command(f'git commit -m "{message}"')


# Example usage:
if __name__ == "__main__":
    repo_path = "/path/to/your/repo"
    vc = VersionControl(repo_path)

    modified_files = vc.get_modified_files()
    print("Modified Files:", modified_files)

    for file in modified_files:
        print(f"Diff for {file}:\n", vc.get_file_diff(file))

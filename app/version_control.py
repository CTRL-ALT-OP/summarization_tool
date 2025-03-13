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
        """Returns a list of modified files in the repository with correct path handling."""
        output = self.run_git_command("git status --porcelain")
        print("Git Status Output:", output)  # Debugging line

        modified_files = []

        if output:
            for line in output.split("\n"):
                if line.strip():  # Ensure it's not empty
                    status, filename = (
                        line[:2].strip(),
                        line[2:].strip(),
                    )  # Extract status & filename correctly
                    if status in {"M", "A", "D"}:  # Modified, Added, Deleted
                        modified_files.append(filename)

        print("Parsed Modified Files:", modified_files)  # Debugging line
        return modified_files

    def get_file_diff(self, filename):
        """Returns the diff of a specific file, ensuring correct Git path handling."""
        corrected_filename = filename.strip().replace(
            "\\", "/"
        )  # Normalize Windows paths
        diff_output = self.run_git_command(f'git diff -- "{corrected_filename}"')

        print(f"Diff for {corrected_filename}:", diff_output)  # Debugging line

        return diff_output if diff_output else "No differences detected."

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

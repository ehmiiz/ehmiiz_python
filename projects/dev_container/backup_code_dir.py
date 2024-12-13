import os
import subprocess
import datetime

def backup_code_directory(container_name, backup_location):
    try:
        # Get the current date for the backup folder or file name
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Define the container source path and backup destination
        source_path = f"{container_name}:/home/ehmiiz/code"
        backup_path = os.path.join(backup_location, f"code_backup_{date_str}.tar")
        
        # Command to create a tarball of the directory inside the container
        tar_command = [
            "docker", "exec", container_name, "tar", "-cvf", "/tmp/code_backup.tar", "-C", "/home/ehmiiz", "code"
        ]
        subprocess.run(tar_command, check=True)
        
        # Command to copy the tarball from the container to the host
        copy_command = ["docker", "cp", f"{container_name}:/tmp/code_backup.tar", backup_path]
        subprocess.run(copy_command, check=True)
        
        # Clean up the tarball inside the container
        cleanup_command = ["docker", "exec", container_name, "rm", "/tmp/code_backup.tar"]
        subprocess.run(cleanup_command, check=True)
        
        print(f"Backup completed successfully. File saved to {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e.stderr.strip()}")

if __name__ == "__main__":
    # Set the container name and backup location
    container_name = "python_dev"
    backup_location = "C:/Users/ehmiiz/OneDrive - Wirely AB/Backup"  # Replace with your desired backup directory
    
    # Ensure the backup directory exists
    if not os.path.exists(backup_location):
        os.makedirs(backup_location)
    
    # Perform the backup
    backup_code_directory(container_name, backup_location)

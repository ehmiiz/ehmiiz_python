import subprocess
import getpass

def create_python_dev_container():
    try:
        # Define the Docker command to create the container
        command = [
            "docker", "run", "-d", "--name", "python_dev", "--restart", "unless-stopped",
            "-v", "python_dev_data:/app/data", "fedora:latest", "tail", "-f", "/dev/null"
        ]
        
        # Run the command to create the container
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Get the container ID
        container_id = result.stdout.strip()
        print(f"Container created successfully. ID: {container_id}")
        
        # Add a user and configure the container
        setup_user_and_backup(container_id)
        
        return container_id
    except subprocess.CalledProcessError as e:
        print(f"Error creating container: {e.stderr.strip()}")
        return None


def setup_user_and_backup(container_id):
    try:
        # Define the commands to run inside the container
        username = "ehmiiz"
        pw = getpass.getpass("pw: ")
            
        commands = [
            # Add a new user '{username}' with home directory and password
            f"docker exec -i {container_id} bash -c \"useradd -m -d /home/{username} {username}\"",
            f"docker exec -i {container_id} bash -c \"echo 'ehmiiz:{pw}' | chpasswd\"",
            
            # Add '{username}' to the sudo group
            f"docker exec -i {container_id} bash -c \"usermod -aG wheel {username}\"",
            
            # Set /home/code as the automatic backup directory
            f"docker exec -i {container_id} bash -c \"mkdir -p /home/{username}/code && chown {username}:{username} /home/{username}/code\"",
        ]
        
        # Execute each command
        for command in commands:
            print(f"Executing: {command}")
            subprocess.run(command, check=True, shell=True)
        
        print("User added, granted sudo privileges, and backup directory set.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring container: {e.stderr.strip()}")


# Call the function
if __name__ == "__main__":
    container_id = create_python_dev_container()
    if container_id:
        print(f"Container ID: {container_id}")

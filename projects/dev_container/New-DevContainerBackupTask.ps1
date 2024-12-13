
# Define variables
$TaskName = "BackupCodeDirectory"
$ScriptPath = "C:\Users\ehmiiz\code\py\ehmiiz_python\projects\dev_container\backup_code_dir.py"
$StartTime = (Get-Date).AddMinutes(1) # Start one minute from now

# Define the task action
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -Command python `"$ScriptPath`""

# Define the scheduled task trigger
$Trigger = New-ScheduledTaskTrigger -Once -At $StartTime -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Days 3650)

# Register the task
Register-ScheduledTask -TaskName $TaskName -Trigger $Trigger -Action $Action -Description "Backup code directory every hour" -User "$env:USERNAME" -RunLevel Highest -Force

Write-Output "Scheduled task '$TaskName' created successfully to run the Python script every hour starting at $StartTime."

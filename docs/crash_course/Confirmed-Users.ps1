<#
unconfirmed_users = ['luppo', 'frello', 'ehmmo']

confirmed_users = []

while unconfirmed_users:
    
    current_user = unconfirmed_users.pop()
    
    print(f"Confirmed: {current_user.title()}")
    confirmed_users.append(current_user)

print("We have confirmed:")
for c in confirmed_users:
    print(c.title())

#>

[System.Collections.ArrayList]$ListaNummerEtt = "knackar-apan", "apan-med-vaniljsås", "arga-apan"

$ListaNummerTvå = @()

# Körs tills alla apor är slut i lista 1, lägger apor i lista 2
while ($ListaNummerEtt) {

    $SistaApan = $ListaNummerEtt | Select-Object -Last 1
    $ListaNummerEtt.Remove($SistaApan)

    Write-Output "Vi har apa: $SistaApan"
    $ListaNummerTvå += $SistaApan
}

$ListaNummerTvå
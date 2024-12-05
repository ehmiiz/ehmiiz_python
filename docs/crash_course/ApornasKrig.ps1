# Hehe

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
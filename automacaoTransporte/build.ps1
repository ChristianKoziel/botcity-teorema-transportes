$exclude = @("venv", "automacaoTransporte.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "automacaoTransporte.zip" -Force
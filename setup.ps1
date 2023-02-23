Write-Output "Install poetry dependencys."
python -m poetry install

Write-Output "Building executable"
python -m PyInstaller main.py --onefile --name "OMSCS-7210_Setup"

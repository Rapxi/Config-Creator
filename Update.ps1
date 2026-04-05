
param (
    [string]$RepoOwner = "Rapxi",       # e.g. "microsoft"
    [string]$RepoName  = "Config-Creator",  # e.g. "terminal"
    [string]$Branch    = "main"         # e.g. "main" or "master"
)


# Config

$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ZipUrl      = "https://github.com/$RepoOwner/$RepoName/archive/refs/heads/$Branch.zip"
$ZipPath     = Join-Path $env:TEMP "$RepoName-$Branch.zip"
$ExtractTemp = Join-Path $env:TEMP "$RepoName-extract-$(Get-Random)"


# Helper

function Write-Step { param([string]$Msg) Write-Host "`n>> $Msg" -ForegroundColor Cyan }
function Write-OK   { param([string]$Msg) Write-Host "   $Msg" -ForegroundColor Green }
function Write-Fail { param([string]$Msg) Write-Host "   ERROR: $Msg" -ForegroundColor Red }


# 1. Download ZIP

Write-Step "Downloading $ZipUrl "
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $ZipUrl -OutFile $ZipPath -UseBasicParsing -ErrorAction Stop
    Write-OK "Saved to $ZipPath"
} catch {
    Write-Fail "Download failed: $_"
    exit 1
}


#  Extract ZIP to a temp folder

Write-Step "Extracting ZIP "
try {
    New-Item -ItemType Directory -Path $ExtractTemp -Force | Out-Null
    Expand-Archive -Path $ZipPath -DestinationPath $ExtractTemp -Force -ErrorAction Stop
    Write-OK "Extracted to $ExtractTemp"
} catch {
    Write-Fail "Extraction failed: $_"
    Remove-Item $ZipPath -ErrorAction SilentlyContinue
    exit 1
}


#  GitHub puts everything inside a sub-folder: <RepoName>-<Branch>/
#    Move its contents into the script directory, overwriting existing files.

Write-Step "Copying files to $ScriptDir ..."

# Find the single top-level folder GitHub creates inside the ZIP
$TopLevel = Get-ChildItem -Path $ExtractTemp -Directory | Select-Object -First 1

if (-not $TopLevel) {
    Write-Fail "Could not find extracted repo folder inside $ExtractTemp"
    exit 1
}

$SourceRoot = $TopLevel.FullName
Write-OK "Source root: $SourceRoot"

$Files = Get-ChildItem -Path $SourceRoot -Recurse -File
$Total = $Files.Count
$i     = 0

foreach ($File in $Files) {
    $i++
    # Build the relative path from the source root
    $Relative   = $File.FullName.Substring($SourceRoot.Length).TrimStart('\','/')
    $Destination = Join-Path $ScriptDir $Relative

    # Ensure the target sub-directory exists
    $DestDir = Split-Path $Destination -Parent
    if (-not (Test-Path $DestDir)) {
        New-Item -ItemType Directory -Path $DestDir -Force | Out-Null
    }

    Copy-Item -Path $File.FullName -Destination $Destination -Force
    Write-Host "   [$i/$Total] $Relative" -ForegroundColor DarkGray
}

Write-OK "All $Total file(s) copied."


# Clean up temp files

Write-Step "Cleaning up ..."
Remove-Item $ZipPath     -Force -ErrorAction SilentlyContinue
Remove-Item $ExtractTemp -Recurse -Force -ErrorAction SilentlyContinue
Write-OK "Done."

Write-Host "`nUpdate complete!" -ForegroundColor Yellow
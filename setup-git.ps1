# Git Setup Script for SDR-Audit-Agent
# This script initializes git, adds files, commits, and sets up the remote

Write-Host "Setting up Git repository for SDR-Audit-Agent..." -ForegroundColor Green

# Try to find git
$gitPath = $null
$possiblePaths = @(
    "C:\Program Files\Git\bin\git.exe",
    "C:\Program Files (x86)\Git\bin\git.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\git.exe",
    "git"
)

foreach ($path in $possiblePaths) {
    if ($path -eq "git") {
        try {
            $null = Get-Command git -ErrorAction Stop
            $gitPath = "git"
            break
        } catch {
            continue
        }
    } else {
        if (Test-Path $path) {
            $gitPath = $path
            break
        }
    }
}

if (-not $gitPath) {
    Write-Host "ERROR: Git not found. Please install Git or add it to your PATH." -ForegroundColor Red
    Write-Host "Download Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

Write-Host "Found Git at: $gitPath" -ForegroundColor Green

# Initialize git if needed
if (-not (Test-Path .git)) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    & $gitPath init
}

# Add files
Write-Host "Adding files to git..." -ForegroundColor Yellow
& $gitPath add app.py requirements.txt templates/index.html Dockerfile

# Commit
Write-Host "Creating initial commit..." -ForegroundColor Yellow
& $gitPath commit -m "Initial commit: SDR-Audit-Agent with intentional vulnerabilities"

# Add remote
Write-Host "Setting up remote repository..." -ForegroundColor Yellow
& $gitPath remote remove origin 2>$null
& $gitPath remote add origin https://github.com/lukeman817/sdr-audit-agent.git

Write-Host "`nGit repository setup complete!" -ForegroundColor Green
Write-Host "`nTo push to GitHub, run:" -ForegroundColor Cyan
Write-Host "  git push -u origin main" -ForegroundColor White
Write-Host "`nOr if your default branch is 'master':" -ForegroundColor Cyan
Write-Host "  git push -u origin master" -ForegroundColor White
Write-Host "`nNote: You may need to authenticate with GitHub." -ForegroundColor Yellow

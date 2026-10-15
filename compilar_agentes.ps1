# =====================================================================
# PIPELINE DE SINCRONIZACIÓN: BÓVEDA -> AGENTES NATIVOS
# =====================================================================
# Este script escanea la Bóveda de Arquitectura y "compila" los documentos
# de diseño transformándolos en skills ejecutables nativas de Antigravity.

$vaultPath = $PSScriptRoot
# Apuntamos la carpeta nativa al directorio padre (el workspace raíz)
$targetPath = Join-Path (Split-Path $vaultPath -Parent) ".agents\skills"

Write-Host "🚀 Iniciando compilación de Bóveda a Agentes Nativos..." -ForegroundColor Cyan

# Crear el directorio base si no existe
if (-not (Test-Path $targetPath)) {
    New-Item -ItemType Directory -Force -Path $targetPath | Out-Null
}

# Buscar todos los archivos Markdown que empiecen con "Skill "
$skills = Get-ChildItem -Path $vaultPath -Recurse -Filter "Skill *.md"

$count = 0
foreach ($skill in $skills) {
    # Formatear el nombre de la carpeta (snake_case)
    # Ej: "Skill AAS UI UX Pro Max" -> "aas_ui_ux_pro_max"
    $rawName = $skill.BaseName.Replace("Skill ", "").Trim()
    $folderName = $rawName.ToLower() -replace '[^a-z0-9]', '_' -replace '_+', '_'
    
    $skillDestDir = Join-Path $targetPath $folderName
    
    if (-not (Test-Path $skillDestDir)) {
        New-Item -ItemType Directory -Force -Path $skillDestDir | Out-Null
    }
    
    # Copiar y renombrar estrictamente a SKILL.md
    $destFile = Join-Path $skillDestDir "SKILL.md"
    Copy-Item -Path $skill.FullName -Destination $destFile -Force
    
    Write-Host "  ✅ Enlazada nativamente: $folderName" -ForegroundColor Green
    $count++
}

# Skills globales: ya tienen formato nativo (<nombre>/SKILL.md), se copian completas
$globalPath = Join-Path $vaultPath "14-Skills-Globales"
foreach ($dir in Get-ChildItem -Path $globalPath -Directory) {
    $skillDestDir = Join-Path $targetPath $dir.Name
    robocopy $dir.FullName $skillDestDir /E /XD .venv __pycache__ /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy falló para $($dir.Name) (código $LASTEXITCODE)" }
    Write-Host "  ✅ Skill global: $($dir.Name)" -ForegroundColor Green
    $count++
}

Write-Host "🎉 Pipeline terminado. Se compilaron $count skills." -ForegroundColor Cyan
Write-Host "Antigravity ahora cargará estas skills nativamente en su memoria." -ForegroundColor Yellow

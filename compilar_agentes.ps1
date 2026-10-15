# =====================================================================
# PIPELINE DE SINCRONIZACION: BOVEDA -> AGENTES Y SKILLS NATIVAS
# =====================================================================
# Este script sincroniza la Boveda de Arquitectura con el motor de skills
# de Antigravity (y otros arneses compatibles como Claude Code / OpenCode).
# Soporta tanto ejecucion autocontenida como multi-workspace.

$vaultPath = $PSScriptRoot

# Definir destinos:
# 1. Dentro de la propia boveda (.agents/skills) para que sea 100% autocontenida
# 2. En la configuracion global de Antigravity (~/.gemini/config/skills) para disponibilidad universal
# 3. En la boveda de estudio si ya contiene carpeta .agents
$targetDirs = @(
    (Join-Path $vaultPath ".agents\skills")
)

$globalSkillsDir = Join-Path $env:USERPROFILE ".gemini\config\skills"
if (Test-Path (Split-Path $globalSkillsDir -Parent)) {
    $targetDirs += $globalSkillsDir
}

$studyVaultSkills = "C:\Users\NezerkC\OneDrive\Documentos\Obsidian Vault\.agents\skills"
if (Test-Path $studyVaultSkills) {
    $targetDirs += $studyVaultSkills
}

Write-Host "Iniciando compilacion de Boveda a Skills Nativas..." -ForegroundColor Cyan
Write-Host "Boveda origen: $vaultPath" -ForegroundColor Gray

foreach ($target in $targetDirs) {
    if (-not (Test-Path $target)) {
        New-Item -ItemType Directory -Force -Path $target | Out-Null
    }
}

# ---------------------------------------------------------------------
# 1. Sincronizar Skills Globales (14-Skills-Globales)
# ---------------------------------------------------------------------
$globalSkillsPath = Join-Path $vaultPath "14-Skills-Globales"
$globalCount = 0

if (Test-Path $globalSkillsPath) {
    $globalSkills = Get-ChildItem -Path $globalSkillsPath -Directory
    foreach ($skillDir in $globalSkills) {
        $skillName = $skillDir.Name
        foreach ($target in $targetDirs) {
            $destDir = Join-Path $target $skillName
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Force -Path $destDir | Out-Null
            }
            # Copiar recursivamente archivos y subdirectorios (scripts, evals, references)
            Copy-Item -Path (Join-Path $skillDir.FullName "*") -Destination $destDir -Recurse -Force
        }
        Write-Host "  Skill Global sincronizada: $skillName" -ForegroundColor Green
        $globalCount++
    }
}

# ---------------------------------------------------------------------
# 2. Sincronizar Skills AAS Especialistas (Skill *.md)
# ---------------------------------------------------------------------
$skillsAAS = Get-ChildItem -Path $vaultPath -Recurse -Filter "Skill *.md" | Where-Object {
    $_.FullName -notmatch "14-Skills-Globales"
}

# Diccionario de descripciones por omision para progressive disclosure
$descriptions = @{
    "aas_context_distiller"   = "Analista de Requerimientos y Destilador de Contexto. Transforma conversaciones informales en un plan de accion estructurado (DAG) con diagrama Mermaid."
    "aas_code_review"         = "Revision estricta de Pull Requests, validacion de invariantes de Clean Architecture, cumplimiento de contratos CDD y gates de merge contra ADRs."
    "aas_security_engineer"   = "Auditoria de seguridad integral, analisis de vulnerabilidades OWASP, SAST/SCA, sanitizacion de fronteras y hardening de infraestructura."
    "aas_devops_cloud"        = "Automatizacion de infraestructura cloud, pipelines CI/CD deterministas, monitoreo de metricas DORA y orquestacion de despliegues."
    "aas_rpa_windows"         = "Automatizacion robotica de procesos en Windows, scripts de PowerShell, inspeccion de UI y orquestacion de tareas desktop."
    "aas_frontend_design"     = "Diseno e implementacion de sistemas de diseno visual, componentes en React/Tailwind y tokens de diseno para interfaces modernas."
    "aas_ui_ux_pro_max"       = "Transformacion de requerimientos funcionales y Design Tokens en interfaces de usuario usables, accesibles y mantenibles con librerias homologadas."
}

$aasCount = 0
foreach ($skill in $skillsAAS) {
    $rawName = $skill.BaseName.Replace("Skill ", "").Trim()
    $folderName = ($rawName.ToLower() -replace "[^a-z0-9]", "_") -replace "_+", "_"
    
    $content = Get-Content -Path $skill.FullName -Raw -Encoding UTF8
    
    # Validar si ya tiene name y description en el frontmatter
    $desc = "Agente especialista: " + $rawName
    if ($descriptions.ContainsKey($folderName)) {
        $desc = $descriptions[$folderName]
    }
    
    if ($content -match "(?s)^---\s*\r?\n(.*?)\r?\n---") {
        $fm = $matches[1]
        $hasName = $fm -match "(?m)^name:"
        $hasDesc = $fm -match "(?m)^description:"
        
        $newFm = $fm
        if (-not $hasName) { 
            $newFm = "name: " + $folderName + "`n" + $newFm 
        }
        if (-not $hasDesc) { 
            $newFm = "description: `"" + $desc + "`"`n" + $newFm 
        }
        
        $body = $content -replace "(?s)^---\s*\r?\n.*?\r?\n---\r?\n?", ""
        $compiledContent = "---`n" + $newFm.Trim() + "`n---`n" + $body
    } else {
        $compiledContent = "---`nname: " + $folderName + "`ndescription: `"" + $desc + "`"`n---`n`n" + $content
    }

    foreach ($target in $targetDirs) {
        $destDir = Join-Path $target $folderName
        if (-not (Test-Path $destDir)) {
            New-Item -ItemType Directory -Force -Path $destDir | Out-Null
        }
        $destFile = Join-Path $destDir "SKILL.md"
        [System.IO.File]::WriteAllText($destFile, $compiledContent, [System.Text.Encoding]::UTF8)
    }
    
    Write-Host "  Skill AAS compilada: $folderName" -ForegroundColor Green
    $aasCount++
}

Write-Host "Sincronizacion completada exitosamente." -ForegroundColor Cyan
Write-Host "   - $globalCount Skills Globales vinculadas." -ForegroundColor White
Write-Host "   - $aasCount Skills AAS de Arquitectura compiladas." -ForegroundColor White
Write-Host "   - Total: $($globalCount + $aasCount) Skills nativas disponibles en Antigravity." -ForegroundColor Yellow

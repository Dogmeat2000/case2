# Case 2: Input Validation Testing

## 🛡️ Automated Security & Quality Telemetry

This project leverages automated continuous integration workflows to scan for code quality, architectural degradation, and supply chain security vulnerabilities on every push to the main branch.

### 📊 Static Application Security Testing (SAST)

| Analysis Engine | Quality Gate Status | Security Rating | Code Smells | Open Vulnerabilities |
| :--- | :---: | :---: | :---: | :---: |
| **SonarQube Cloud** | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Dogmeat2000_case2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Dogmeat2000_case2) | [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Dogmeat2000_case2&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Dogmeat2000_case2t) | [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Dogmeat2000_case2&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Dogmeat2000_case2) | [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Dogmeat2000_case2&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Dogmeat2000_case2) |

🔗 **Deep Dive Analysis Dashboard:** [Access Public SonarQube Overview Report](https://sonarcloud.io/project/overview?id=Dogmeat2000_case2)

---

### 📦 Software Supply Chain & Dependency Analysis (SCA)

| Vulnerability Vector | Current Active Count | Direct Dashboard Links |
| :--- | :---: | :--- |
| **Trivy Container/FS Scanner** | ![Trivy Alerts Count](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FDogmeat2000%2F866c8a4d1b81b16604e625af0368cd13%2Fraw%2Ftrivy-count_case2.json&cacheBust=1) | [View Trivy Code Scanning Alerts](https://github.com/Dogmeat2000/case2/security/code-scanning) |
| **GitHub Dependabot** | ![Dependabot Alerts Count](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FDogmeat2000%2F866c8a4d1b81b16604e625af0368cd13%2Fraw%2Fdependabot-count_case2.json&cacheBust=1) | [Review Active Dependabot Alerts](https://github.com/Dogmeat2000/case2/security/dependabot) |
| **Supply Chain Malware** | ![Malware Protection Enabled](https://img.shields.io/badge/Malware--Scan-Active-success?style=flat&logo=github) | [Review Repository Malware Status](https://github.com/Dogmeat2000/case2/security/malware) |

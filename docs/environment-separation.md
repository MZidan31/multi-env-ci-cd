# 🧩 Environment Separation Strategy

## 📌 Tujuan
Dokumen ini menjelaskan strategi pemisahan environment antara *Development* (`dev`) dan *Production* (`prod`) dalam proyek final ini. Tujuan utama dari pemisahan ini adalah untuk menjaga stabilitas, keamanan, dan fleksibilitas proses deployment serta monitoring.

Dengan memisahkan environment, setiap perubahan atau pengembangan aplikasi dapat diuji terlebih dahulu di Dev sebelum di-deploy secara resmi ke Prod. Ini mengurangi risiko kesalahan yang langsung berdampak pada pengguna akhir.

---

## 🗂️ Struktur Namespace Kubernetes

Aplikasi akan berjalan di dua namespace berbeda:

| Environment | Namespace | Tujuan |
|-------------|-----------|--------|
| Development | `dev`     | Tempat testing, eksperimen, pengembangan |
| Production  | `prod`    | Versi final yang stabil untuk pengguna akhir |

Namespace memisahkan resource, configmap, secret, dan monitoring sehingga isolasi environment menjadi maksimal.

---

## ⚙️ Perbedaan Konfigurasi Dev & Prod

| Aspek              | Dev                                         | Prod                                          |
|--------------------|---------------------------------------------|-----------------------------------------------|
| **Namespace**      | `dev`                                       | `prod`                                        |
| **Replicas**       | `1` (cukup satu pod)                        | `2` atau lebih (high availability)            |
| **Image Tag**      | `$BUILD_NUMBER` (latest build)              | `v1.x.x` (tagged & approved version)          |
| **ConfigMap**      | `BASE_URL=http://dev.example.com`           | `BASE_URL=http://prod.example.com`           |
| **Secrets**        | API_KEY=dummy atau dev key                  | API_KEY=real production key                   |
| **Monitoring**     | Dashboard: Dev Metrics                      | Dashboard: Prod Metrics                       |
| **Alerting**       | Non-kritis, alert lokal                     | Alert kritis via Discord/email ops team       |

---

## 🔁 Alur CI/CD Dev → Prod

Alur deployment aplikasi dari Dev ke Prod melalui pipeline Jenkins:

1. **Push ke Branch `main`**  
   Developer push perubahan ke branch `main`, Jenkins akan:
   - Build Docker image
   - Push ke DockerHub dengan tag berdasarkan `$BUILD_NUMBER`
   - Deploy ke namespace `dev`

2. **Testing di Environment Dev**  
   - Tim QA atau dev melakukan validasi secara fungsional
   - Dashboard monitoring digunakan untuk mengecek performa awal

3. **Tagging untuk Release**  
   Setelah lolos testing, developer membuat tag Git (contoh: `v1.0.0`). Jenkins akan:
   - Build ulang image dengan tag `v1.0.0` *(jika diperlukan)*
   - Menjalankan input manual di Jenkins untuk approval deploy
   - Jika di-approve, Jenkins deploy ke namespace `prod`

4. **Monitoring Pasca Deploy Prod**  
   - Dashboard Prod aktif
   - Jika terjadi error, rollback bisa dilakukan dengan re-tag versi sebelumnya

---

## 🧱 Struktur Folder yang Mewakili Pemisahan Environment


# 📘 Branch & Tag Strategy untuk CI/CD Multi-Environment

Dokumen ini menjelaskan strategi penggunaan branch dan tag untuk mendukung alur Continuous Integration & Continuous Deployment (CI/CD) pada aplikasi yang memiliki dua environment: **Development (Dev)** dan **Production (Prod)**.

---

## 🧠 Tujuan

- Menstandarisasi pengelolaan branch di Git agar mudah dikelola dan dipantau
- Menentukan alur deployment otomatis berdasarkan branch/tag
- Menghindari kesalahan deploy ke lingkungan Production

---

## 📁 Struktur Branch

| Branch         | Fungsi                                                                 |
|----------------|------------------------------------------------------------------------|
| `main`         | Branch utama untuk integrasi dan deployment otomatis ke namespace `dev` |
| `feature/*`    | Branch untuk pengembangan fitur baru                                    |
| `hotfix/*`     | Branch untuk perbaikan cepat pada `main`                                |
| `release/*` *(opsional)* | Digunakan untuk testing rilis sebelum tagging ke Production         |

> **Catatan:** Semua perubahan ke `main` harus melalui proses *merge* (via pull request atau manual merge), disarankan setelah review tim.

---

## 🏷️ Penamaan Tag Versi

Tag digunakan untuk menandai rilis yang siap deploy ke Production. Format tag disarankan mengikuti [SemVer](https://semver.org/):

- `v<MAJOR>.<MINOR>.<PATCH>`

| Contoh Tag     | Keterangan                            |
|----------------|----------------------------------------|
| `v1.0.0`       | Rilis awal stabil                      |
| `v1.1.0`       | Penambahan fitur besar                 |
| `v1.1.1`       | Perbaikan bug ringan                   |
| `v2.0.0-beta`  | (Opsional) Rilis beta sebelum final    |

---

## 🔁 Alur CI/CD Berdasarkan Branch & Tag

| Aksi Git                      | Jenkins Stage                       | Target Namespace | Approval |
|------------------------------|-------------------------------------|------------------|----------|
| Push ke `main`               | Build → Push Docker → Deploy Dev    | `dev`            | ❌       |
| Tag versi (ex: `v1.0.0`)     | Build → Push Docker → **Approval** → Deploy Prod | `prod`           | ✅       |

---

## 🛡️ Aturan & Kebijakan

- ⛔ Jangan push langsung ke `main`, gunakan pull request dari `feature/*` atau `hotfix/*`
- ✅ Tag hanya boleh dibuat setelah aplikasi sudah **lulus uji coba** di environment Dev
- ✅ Tag versi harus disepakati minimal oleh 2 anggota tim (termasuk PL)
- ⛔ Jangan hapus atau timpa tag yang sudah digunakan deploy ke Production

---

## 🛠️ Cara Membuat Tag

### Via Git CLI:
```bash
git checkout main
git pull origin main
git tag v1.0.0
git push origin v1.0.0

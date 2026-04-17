# =========================================
# DNS SETUP - sevengate.store
# PREMIUM j - Action Required
# =========================================

## 🚨 30 MINUTES - FOLLOW THESE STEPS

### Step 1: Go to your domain registrar
```
URL: https://www.namecheap.com/account/domains/
OR: https://www.godaddy.com
OR: wherever you bought sevengate.store
```

### Step 2: Go to DNS Settings
```
Find "sevengate.store" → Click "Manage" → "DNS"
```

### Step 3: Add these records

```
TYPE     HOST        VALUE                               TTL
─────────────────────────────────────────────────────────
A        @           185.199.108.153                   3600
A        @           185.199.109.153                   3600
A        @           185.199.110.153                   3600
A        @           185.199.111.153                   3600
CNAME    www         gadboisjean1000-arch.github.io    3600
```

### Step 4: Enable HTTPS (after 24h)
```
1. Go to: https://github.com/gadboisjean1000-arch/sevengate-store/settings/pages
2. Enable "Enforce HTTPS"
3. Wait for SSL certificate (automatic)
```

### Step 5: Verify
```
Open: https://sevengate.store
Should show: OMEGAHUB website
```

---

## ⚠️ IMPORTANT

- DNS propagation takes 24-48h
- Use ALL 4 A records (failover)
- www CNAME is required
- HTTPS auto-enabled after propagation

---

## 📞 If issues

Check propagation:
```
https://dnschecker.org/#A/sevengate.store
```

---

**PREMIUM j - DO THIS NOW**

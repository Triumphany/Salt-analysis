# 🔬 Inorganic Qualitative Salt Analysis Assistant (Python CLI Tool)

This is a command-line Python tool for simulating qualitative inorganic salt analysis using classic wet-lab procedures. It guides users through preliminary tests, anion detection, and cation group analysis — mimicking a real lab experience through interactive prompts.

---

## ⚙️ Features

- ✅ Preliminary salt analysis (color and crystalline nature)
- ✅ Anion detection based on residue and filtrate tests
- ✅ Cation group identification from Group I to VI
- ✅ Final summarized lab report
- ✅ Educational and interactive interface with emojis

---

## 📦 Technologies Used

- **Python 3.10+**
- Standard Library only (no external packages required)

---

## 🎮 Sample Execution

```bash
🔬 Inorganic Qualitative Salt Analysis
======================================

1️⃣ What is the colour of the salt? white
→ Al, Zn, Ca, Sr, Ba, Mg, Na, K, NH₄⁺ salts.

2️⃣ What is the nature of the compound? 'Crystalline: C' or 'Amorphous: A' C
→ All water-soluble salts.

3️⃣ Begin Anion Analysis...
Is there any residue? If yes, enter R; if not, enter N: N
→ No residue. Anion is likely halide, sulphate, nitrate or nitrite.

4️⃣ Continue Anion Analysis on filtrate...
2 drops of W.S + AgNO₃ → Any precipitate? (P/N): P
What is the colour of the precipitate? white
→ Halide detected with color: white

5️⃣ Begin Cation Group Analysis...
Add dil HCl → Any precipitate? (Y/N): Y
→ Group I cations may be present (Ag⁺, Pb²⁺, Hg₂²⁺).

📋 FINAL REPORT
===================
Colour of salt     : White
Nature of salt     : Crystalline
Anion identified   : Halide may be present: white ppt
Cation group found : Group I
===================

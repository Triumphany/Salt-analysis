def colour():
    col = input("\n1️⃣ What is the colour of the salt? ").lower()
    if col == "blue":
        print("→ Hydrated Copper salts and anhydrous Cobalt salts.")
        return "Blue"
    elif col == "green":
        print("→ Chromium, Nickel, Copper and Ferrous salts.")
        return "Green"
    elif col == "yellow":
        print("→ Chromates or salts like PbO, HgO, Bi₂O₃, FePO₄, CdS, As₂O₃, etc.")
        return "Yellow"
    elif col in ["orange", "pink"]:
        print("→ Dichromates and Sb₂S₃")
        return col.capitalize()
    elif col == "black":
        print("→ Oxides of Cu²⁺, Mn²⁺, sulphides of Fe²⁺, Sb³⁺, Ni²⁺.")
        return "Black"
    elif col == "white":
        print("→ Al, Zn, Ca, Sr, Ba, Mg, Na, K, NH₄⁺ salts.")
        return "White"
    else:
        print("→ No data found.")
        return "No data"

def nature():
    nat = input("\n2️⃣ What is the nature of the compound? 'Crystalline: C' or 'Amorphous: A' ").upper()
    if nat == "C":
        print("→ All water-soluble salts.")
        return "Crystalline"
    elif nat == "A":
        print("→ Likely insoluble salts.")
        return "Amorphous"
    else:
        print("→ Invalid input.")
        return "Unknown"

def anion():
    print("\n3️⃣ Begin Anion Analysis...")
    Residue = input("Is there any residue? If yes, enter R; if not, enter N: ").upper()
    if Residue == "R":
        print("→ Residue may contain carbonate or sulphide. Add dil. HCl.")
        obs = input("What do you observe?\n1: Effervescence (CO₂) turning lime water milky\n2: H₂S gas (blackening lead acetate)\nEnter 1 or 2: ")
        if obs == "1":
            print("→ Carbonate is present.")
            return "Carbonate is present"
        elif obs == "2":
            print("→ Sulphide is present.")
            return "Sulphide is present"
        else:
            print("→ Invalid observation.")
            return "Unknown anion (invalid input)"
    elif Residue == "N":
        print("→ No residue. Anion is likely halide, sulphate, nitrate or nitrite.")
        return "Proceed to solution analysis"
    else:
        print("→ Invalid input.")
        return "Invalid residue input"

def anion_test():
    print("\n4️⃣ Continue Anion Analysis on filtrate...")
    halide = input("2 drops of W.S + AgNO₃ → Any precipitate? (P/N): ").upper()
    if halide == "P":
        color = input("What is the colour of the precipitate? (white/yellow/cream): ")
        print(f"→ Halide detected with color: {color}")
        return f"Halide may be present: {color} ppt"
    elif halide == "N":
        sulphate = input("2 drops of W.S + Ba(NO₃)₂ → Any ppt? (P/N): ").upper()
        if sulphate == "P":
            print("→ Add dil. HNO₃. If ppt does not dissolve → Sulphate is present.")
            return "Sulphate is present"
        elif sulphate == "N":
            nitrite = input("W.S + acetic acid + FeSO₄ → Any colour change? (Y/N): ").upper()
            if nitrite == "Y":
                print("→ Nitrite is present.")
                return "Nitrite is present"
            elif nitrite == "N":
                nitrate = input("W.S + conc. H₂SO₄ (cool) + FeSO₄ along wall → Brown ring? (Y/N): ").upper()
                if nitrate == "Y":
                    print("→ Nitrate is present.")
                    return "Nitrate is present"
                else:
                    return "No nitrate or nitrite detected"
    print("→ Invalid input.")
    return "Unknown anion"

def group_analysis():
    print("\n5️⃣ Begin Cation Group Analysis...")
    Group_1 = input("Add dil HCl → Any precipitate? (Y/N): ").upper()
    if Group_1 == "Y":
        print("→ Group I cations may be present (Ag⁺, Pb²⁺, Hg₂²⁺).")
        return "Group I"
    else:
        Group_2 = input("Add more HCl, heat, pass H₂S gas → Any ppt? (Y/N): ").upper()
        if Group_2 == "Y":
            input("→ Group II detected. What is the colour of the precipitate? ")
            return "Group II"
        else:
            Group_3A = input("Add NH₄Cl (excess) + NH₄OH (alkaline) → Any ppt? (Y/N): ").upper()
            if Group_3A == "Y":
                input("→ Group IIIA detected. What is the colour of the precipitate? ")
                return "Group IIIA"
            else:
                Group_3B = input("Add NH₄Cl + NH₄OH + H₂S gas → Any ppt? (Y/N): ").upper()
                if Group_3B == "Y":
                    input("→ Group IIIB detected. What is the colour of the precipitate? ")
                    return "Group IIIB"
                else:
                    Group_4 = input("Add (NH₄)₂CO₃ → Any ppt? (Y/N): ").upper()
                    if Group_4 == "Y":
                        return "Group IV"
                    else:
                        Group_5 = input("Add NH₄HPO₄ → Any ppt? (Y/N): ").upper()
                        if Group_5 == "Y":
                            return "Group V"
                        else:
                            return "Group VI (Na⁺, K⁺, NH₄⁺)"

def main():
    print("🔬 Inorganic Qualitative Salt Analysis")
    print("======================================")
    
    # Preliminary
    final_colour = colour()
    final_nature = nature()
    
    # Anion Test
    anion_result = anion()
    if anion_result == "Proceed to solution analysis":
        final_anion = anion_test()
    else:
        final_anion = anion_result

    # Cation Test
    final_cation = group_analysis()

    # Final Report
    print("\n📋 FINAL REPORT")
    print("===================")
    print(f"Colour of salt     : {final_colour}")
    print(f"Nature of salt     : {final_nature}")
    print(f"Anion identified   : {final_anion}")
    print(f"Cation group found : {final_cation}")
    print("===================")


main()


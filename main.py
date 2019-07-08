from pathlib import Path
import sys

STEAM = Path("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Kerbal Space Program\\GameData")
STEAM_64 = Path("C:\\Program Files\\Steam\\steamapps\\common\\Kerbal Space Program\\GameData")

def get_folder():
    """
    Determines KSP installation location. Defaults to Steam install, otherwise
    prompts for a location.
    """
    loc = None
    if STEAM.is_dir():
        loc = STEAM
    elif STEAM_64.is_dir():
        loc = STEAM_64
    
    if loc:
        if input(f"Found KSP GameData at {loc}, install? [y]/n: ") in ("y", "Y", ""):
            return loc
    
    return Path(input("Enter KSP GameData Location:\n"))

def find_gamedata(mod):
    """
    Determines GameData location in mod folder
    """
    datas = list(mod.glob("**/GameData/"))
    if len(datas) == 0:
        if input(f"Couldn't find GameData, use folder root? [y]/n: ") in ("y", "Y", ""):
            return mod
    if len(datas) == 1:
        if input(f"Found GameData at {datas[0]}, use? [y]/n: ") in ("y", "Y", ""):
            return datas[0]
    else:
        print("Found multiple GameDatas, choose one:")
        for i, gd in enumerate(datas):
            print(f"{i}, {gd}")
        i = int(input(": "))
        if input(f"Use GameData at {datas[i]}? [y]/n: ") in ("y", "Y", ""):
            return datas[i]
    
    return mod / input("Enter GameData location in mod folder:\n")

def main():
    loc = get_folder()
    print(f"installing to {loc}...\n")
    if len(sys.argv) > 1:
        mod_folder = Path(sys.argv[1])
    else:
        mod_folder = Path(input("Choose mod folder: "))
        print()
    data = find_gamedata(mod_folder)
    print(f"installing from {data}...")

if __name__ == "__main__":
    main()
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
    Determines GameData location in mod directory
    """
    datas = list(mod.rglob("GameData/"))
    if len(datas) == 0:
        if input(f"Couldn't find GameData, use directory root? [y]/n: ") in ("y", "Y", ""):
            return [mod]
    elif len(datas) == 1:
        if input(f"Found GameData at {datas[0]}, use? [y]/n: ") in ("y", "Y", ""):
            return [datas[0]]
    else:
        print("Found multiple GameDatas, choose one, or 'a' to use all:")
        for i, gd in enumerate(datas):
            print(f"[{i}]: {gd}")
        i = input()
        if i in ("a", "A"):
            return datas
        elif i:
            return [datas[int(i)]]
    
    return [mod / input("Enter GameData location in mod directory:\n")]

def install(src, dest):
    for f in src.iterdir():
        print(f"{f} => {dest / f.name}")
        f.rename(dest / f.name)

def main():
    ksp = get_folder()
    print(f"installing to {ksp}...\n")
    if len(sys.argv) > 1:
        mod_folder = Path(sys.argv[1])
    else:
        mod_folder = Path(input("Choose mod directory: "))
        print()
    if not mod_folder.is_dir():
        print(f"Directory {mod_folder} not found!")
        quit()
    datas = find_gamedata(mod_folder)
    for d in datas:
        print(f"Installing from {d} ...")
        install(d, ksp)
    print("Done!")

if __name__ == "__main__":
    main()
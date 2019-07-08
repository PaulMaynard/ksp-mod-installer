import sys
from pathlib import Path
from zipfile import ZipFile
from tempfile import TemporaryDirectory

STEAM = Path("C:/Program Files (x86)/Steam/steamapps/common/Kerbal Space Program/GameData")
STEAM_64 = Path("C:/Program Files/Steam/steamapps/common/Kerbal Space Program/GameData")

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

def get_dir(loc):
    """
    Gives a Path object representing the mod folder, and a temporary directory
    to be cleaned up if the mod comes from a zip or is downoaded.
    """
    ploc = Path(loc)
    if ploc.is_dir():
        return (ploc, None)
    elif ploc.suffix == ".zip":
        print("Unzipping...")
        temp = TemporaryDirectory()
        with ZipFile(loc) as zfil:
            zfil.extractall(temp.name)
        return Path(temp.name), temp
    else:
        print(f"Directory {loc} not found!")
        quit()

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
        mod_loc = sys.argv[1]
    else:
        mod_loc = input("Choose mod location: ")
        print()
    (mod_dir, temp) = get_dir(mod_loc)
    datas = find_gamedata(mod_dir)
    for d in datas:
        print(f"Installing from {d} ...")
        install(d, ksp)
    if temp:
        temp.cleanup()
        
    print("Done!")

if __name__ == "__main__":
    main()
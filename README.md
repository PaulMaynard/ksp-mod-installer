# KSP Mod Installer

Are you tired of installing mods manually by downloading endless zips from 
spacedock, hunding for their GameData folders, and dragging them into your
KSP install? Do you also want to avoind the minefield that is CKAN, or you want
to use a custom or dev version of a mod? Then this tool is for you!

## Usage

```bash
python main.py [PATH]
```

`[PATH]` can be:
- A path to a folder, from which the mod files will be *moved*, not copied.
- A path to a zip file
- `sd:<id>`, where `id` is the numeric id of the mod on spacedock.
- ~~`sds:<name>`, where `name` is the name of the mod to search on spacedock.~~
- `gh:<user>/<repo>[/<branch>]`, to download off of github. ~~Uses latest
  release if no branch given~~, or downloads branch head if given. 

## Features

- Can install mods from folders or zip files.
- Automatically finds Steam KSP install.
- Finds GameData in mod folder, can handle if there are multiple ones.

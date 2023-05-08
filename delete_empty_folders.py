# Moves a complex folder-file-structure from a privately owned drive into a shared drive while maintaining the structure
# and accounting for missing ownership rights that effectively hinder the moving of any files.

import errno, os, stat, shutil

'''
Files cannot be moved into shared drives if they are not owned by the account used in google sync. Ownership-rights must be manually transferred to the current account or
the owners' accounts must be used in google sync instead (note, file-paths could change if new log-in takes place).

Unfortunately, ownership cannot be figured out on the local google sync version - it is necessary to browse the drive online. To make it easier / faster to find the remaining files
for which ownership-rights are lacking, we want to be left only with the folder-structure in which files remain.

So next step is folder-removal: we delete all folders that are empty after the last round of moving files.
'''

# handleRemoveReadonly helps to avoid "read-only" challenges when trying to delete all empty (sub-)folders in the src-path
# based on: https://stackoverflow.com/a/1214935

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

# step 2: actual folder removal in source location
def remove_empty_folders(paths):
    if type(paths) is str:
        paths = [paths]
    for path in paths:
        walk = list(os.walk(path))
        for subpath, _, _ in walk[::-1]:
            if len(os.listdir(subpath)) == 0:
                shutil.rmtree(subpath, ignore_errors=False, onerror=handleRemoveReadonly)
                print(f"Removed empty folder {subpath}.")
    return ''

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    remove_empty_folders(src)
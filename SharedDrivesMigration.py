'''

This program moves a complex folder-file-structure from a (personal) drive into a shared drive while maintaining the structure
and accounting for missing ownership rights that effectively hinder the moving of any files.

Prerequirements: local Google Drive for Desktop installation, identified locations from where to where files and sub-folders should be moved, python libraries installed.not

'''

### Program set-up #####
# enter path that holds the files/sub-folders that are supposed to be moved here:
src = "ENTER PATH HERE LIKE H:/My Drive/operationalstuff"

# enter exact path where files and sub-folders should be moved to here:
dst = "ENTER PATH HERE LIKE H:/Shared drives/Operations/german_chapter"

# specify if (sub-)folders at source-location which have been moved with all content should be deleted afterwards
# RECOMMEND LEAVING THIS TRUE - helps identifying locations from which files couldn't be moved (due to missing ownership rights)
deleteemptyfolders = True

## PARAMETER-DOUBLECHECK: Are you sure you have correctly specified all parameters? -> If yes, set this to True
parameter_check = False





##############################


### program code below - edit only if you know what you are doing

import os, shutil, delete_empty_folders

def moving_contents(src, dst):
    error_list = []
    for root, directories, files in os.walk(src, topdown=True):
        for name in directories:
            sub_dir = os.path.join(root, name).replace(src, dst)

            # create copied folder in destination-structure
            if not os.path.exists(sub_dir):
                os.mkdir(sub_dir)

        for name in files:
            # move file to destination
            src_file = os.path.join(root, name)
            dst_file = os.path.join(root, name).replace(src, dst)

            # since some files can only be moved with copy paste and others only with cut paste, we will try both methods
            # cut-paste (ctrl + x) is much faster since it doesnt require downloading the files in the back - so it's tried first

            try:
                # method equals ctrl + x
                os.rename(src_file, dst_file)
                print(f"Successfully moved {name} to {dst_file}!")

            except:
                try:
                    # recursively use copy-function (this will help copying all the non-google-format files with other owners, e.g. PDFs and so on...
                    shutil.move(src_file, dst_file)
                    print(f"Successfully copied {name} to {dst_file}!")
                    os.remove(src_file)

                    # files that cannot be moved (other owners AND gooogle-format-files) simply stay in their original place - there is no file loss here
                except:
                    error_list.append(src_file)

    if error_list:
        print(f"{len(error_list)} files could not be moved.")

    print("Finished moving all files with owner-rights from {src} to {dst}.")

    return ""


if parameter_check:
    if __name__ == '__main__':
        moving_contents(src, dst)
        if deleteemptyfolders:
            delete_empty_folders.remove_empty_folders([src, dst])
else:
    print("Parameter-Doublecheck isn't set to True, please set your parameters, set doublecheck to True and run again!")


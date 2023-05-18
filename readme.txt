# SharedDrivesMigration

Helps moving a nested folder-file-structure on Google Drive from the (personal) drive area into a shared drive while maintaining the structure
and accounting for missing ownership rights that effectively hinder the moving of any files due to Google settings.


Prerequirements:
- local Google Drive for Desktop installation
- identified locations from where to where files and sub-folders should be moved
- python libraries installed etc

This is not a fully functional binary file and parameter-specification should be moved to the argsparser - at the moment users have to open it and specify parameters there. Currently, there doesnt seem to be a need to further finalize this into a publishable / more user-friendly version.

Next steps:
-consider using Drive API
- add type definitions
- use Docstrings in Code

Code
-> add gute Dokumentation
-> in GO übersetzen und dann in executable verpacken, GO - lässt sich direkt native umsetzen
oder in Python und PyInstaller inkludieren?
- Größe checken
- GitHub Actions nutzen: baut executables für verschiedene OS simultan



Motivation: having an existing NGO with history of using Google Drive without Shared Drives wanting to migrate files to org-owned shared drives newly installed - very bothersome and lengthy effort without automation. It's really poorly made by Google atm.

Background (to be shortened):
Small NGOs oftentimes use Google Drive for file-management. Until they get registered as NGO and thus obtain access to GSuite for Non-Profits, they have usually already grown a large system of personally owned ("My Drive") files and folders shared between the initial members of the group. Using personally owned files in Gdrive comes with big problems, e.g. files cannot be moved by anyone who isn't the file owner within larger structures, people dropping out of the organization oftentimes leave many files in suboptimal and not modifiable locations, new members of the orgs must get access to the files by individual file / folder-sharing instead of their addition to a user-group that has general access to shared drives (TLDR: NGOs should use Shared Drives but usually start building large structures in personal drives). However, once orgs obtain access to the functionality of free shared drives, they will stumble upon this REALLY BAD GOOGLE-Problem that folders cannot be copied from personal drives into shared-drives. The usual work-around is downloading the entire personal drive and uploading it to the shared drive - but in my concreat
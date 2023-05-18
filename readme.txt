# SharedDrivesMigration

Helps moving a nested folder-file-structure on Google Drive from the (personal) drive area into a shared drive while maintaining the structure
and accounting for missing ownership rights that effectively hinder the moving of any files due to Google settings.

Motivation: having an existing NGO with history of using Google Drive without Shared Drives wanting to migrate files to org-owned shared drives newly installed - very bothersome and lengthy effort without automation. It's really poorly made by Google atm.

Prerequirements:
- local Google Drive for Desktop installation
- identified locations from where to where files and sub-folders should be moved
- python libraries installed etc

This is not a fully functional binary file and parameter-specification should be moved to the argsparser - at the moment you will have to open
it and specify parameters there. Currently, there doesnt seem to be a need to further finalize this into a publishable / more user-friendly version.

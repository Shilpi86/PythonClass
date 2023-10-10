import filecmp

dir1 = "/Users/shona/Desktop/bun1"
dir2 = "/Users/shona/Desktop/bun2"

comp = filecmp.dircmp(dir1, dir2)

# Print the differences between the directories
print("Common files:", comp.common_files)


#print("Files only in", dir1 + ":", comp.left_only)
#print("Files only in", dir2 + ":", comp.right_only)
#print("Common subdirectories:", comp.common_dirs)
#print("Subdirectories only in", dir1 + ":", comp.left_only)
#print("Subdirectories only in", dir2 + ":", comp.right_only)
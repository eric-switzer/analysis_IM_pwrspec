import fnmatch
import os
import filecmp
import subprocess

cmp_path = "../analysis_IM/"

matches = []
for root, dirnames, filenames in os.walk('.'):
  for filename in fnmatch.filter(filenames, '*.py'):
      matches.append(os.path.join(root, filename))

for filename in matches:
    local_file = filename[2:]
    remote_file = cmp_path + local_file
    try:
        if not filecmp.cmp(local_file, remote_file):
            print remote_file, local_file
            subprocess.call(["vimdiff", local_file, remote_file])
    except OSError:
        print "remote does not have %s" % local_file

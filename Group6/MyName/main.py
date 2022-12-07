import sys
import pkg_resources

f = open("my_version.txt", 'w')
f.write(sys.version)
for d in pkg_resources.working_set:
    line = d.project_name + ' = ' + str(d.version) + "\n"
    f.write(line)
f.close()

print("Done")
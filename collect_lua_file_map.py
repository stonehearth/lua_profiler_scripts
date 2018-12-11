#!/usr/bin/env python
import os
import sys

def collect_lua_file_map():
  string_escape_table = {
    "\\" : "&#92;",   # escape escape
    "\"" : "&quot;",  # escape quotes
    "\n" : "\\n",     # new lines to \n
  }

  subdir = 'source/stonehearth_data/mods/'
  lua_file_map_path = 'scripts/lua_profiler/lua_file_map.js'

  if len(sys.argv) == 3:
    _, subdir, lua_file_map_path = sys.argv

  print 'Path to mods directory: %s' % subdir
  print 'Path to lua_file_map.js: %s' % lua_file_map_path

  luafiles = {}
  for root, dirs, files in os.walk(subdir):
    for f in files:
      if f.endswith('.lua'):
        filename = os.path.join(root, f)
        source = '@' + filename[len(subdir):].replace('\\', '/')
        contents = file(filename).read()
        for src, dst in string_escape_table.iteritems():
          contents = contents.replace(src, dst)
        luafiles[source] = contents

  f = file(lua_file_map_path, 'w')
  f.write('var luaFileMap = {')
  for source in luafiles:
    f.write("  \"%s\": \"%s\",\n" % (source, luafiles[source]))
  f.write('   "@" : undefined\n};\n')
  f.close()

if __name__ == "__main__":
  collect_lua_file_map()
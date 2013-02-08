import json, glob

for fn in glob.glob("*.json"):
  print "testing %s"%fn
  f=open(fn)
  try:
    json.load(f)
    print "OK"
  except:
    print "Fail"
  f.close()

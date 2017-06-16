def is_it_python(s):
   if s is not str or len(s.strip())==0:
     return False
   try:
        compile(s.strip(),'','eval')
        return True
   except:
       return False
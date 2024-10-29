Test:
- on_message(message), call HelloWorld(message)  
  Expected: Call HelloWorld(message) succesfully    
  Result: HelloWorld(message) failed  
  Fix: await HelloWorld(message)
- on_message(message), await HelloWorld(message)  
  Expected: HelloWorld won't fail  
  Result: HelloWorld didn't fail
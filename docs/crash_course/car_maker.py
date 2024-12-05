# import makecar # 
# from makecar import make_car # Nice if you know you'll only be using 1 function.
# from makecar import make_car as mc # <- Minimalistic way
import makecar as mc # <- Perfered way, easiest to read and gives away module name.
# from makecar import * # <- Might be the simplest way, drawback is that it might import 2 much. 

mc.make_car('Subaru', 'Outback')
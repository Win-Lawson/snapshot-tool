--
-- Created by IntelliJ IDEA.
-- User: nwlla
-- Date: 4/13/2021
-- Time: 2:45 PM
-- To change this template use File | Settings | File Templates.
--

os.loadAPI("shape.lua")

print("But first I need to know what to build with")
print("If you want to use oak planks, enter oak_planks (minecraft id)")
print("Enter Base Material")
mat1 = read()
print("Enter Wall Material")
mat2 = read()
print("Enter Roof Material")
mat3 == read()

shape.prism(13,9,2,mat1)
shape.prism(13,9,2,mat2)
turtle.turnLeft()
turtle.forward()
turtle.turnRight()
shape.prism(13,11,4,mat2)
turtle.turnRight()
turtle.turnRight()
turtle.forward()
turtle.turnRight()
turtle.forward()
turtle.turnRight()
turtle.down()
shape.roof(15,7,mat3)
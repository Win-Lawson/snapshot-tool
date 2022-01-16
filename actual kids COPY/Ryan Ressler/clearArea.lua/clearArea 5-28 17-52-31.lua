length =16
width = 49
shouldTurnLeft = false
turtle.select(16)
turtle.equipLeft()
for i = 1, width do 
for i = 1, length do  
    if turtle.detectDown() == false  then   
        turtle.select(1)
        turtle.placeDown()
    end
    if turtle.inspect() == "oak_log" then
    end
    if turtle.detect() == true then
        if equipPickaxe == false then
            turtle.select()
            turtle.equipLeft()
            equipPickaxe = true
        end
        turtle.dig()     
    end
    turtle.up()
    turtle.digDown()
    turtle.select(2)
    turtle.placeDown()
    turtle.forward()
    turtle.down()
end
if shouldTurnLeft == false then 
turtle.turnRight()
turtle.forward()
turtle.turnRight()
shouldTurnLeft = true
else 
turtle.turnLeft()
turtle.forward()
turtle.turnLeft()
shouldTurnLeft = false
end
end


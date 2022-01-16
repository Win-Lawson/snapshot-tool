length =15
width = 49
equipPickaxe = false
for i = 1, width do 
for i = 1, length do  
    if turtle.detectDown() == false  then   
        turtle.select(3)
        turtle.placeDown()
    end
    if turtle.inspect() == "oak_log" then
    end
    if turtle.detect() == true then
        if equipPickaxe == false then
            turtle.equipRight()
            equipPickaxe = true
        end
        turtle.dig()     
    end
        if equipPickaxe == true then
            turtle.equipRight()
            equipPickaxe = false
        end
    turtle.up()
    turtle.digDown()
    turtle.select(4)
    turtle.placeDown()
    turtle.forward()
    turtle.down()
end
turtle.turnRight()
turtle.forward()
turtle.turnRight()
end

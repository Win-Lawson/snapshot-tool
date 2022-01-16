inventorySlot=1
turtle.up()
for i=1,8 do
    for i=1,4 do
        for i=1, 8, 1 do
            turtle.select(math.random(1,16))
            turtle.placeDown()
            turtle.forward()
            end
        turtle.turnRight()
        end
    turtle.up()    
    end

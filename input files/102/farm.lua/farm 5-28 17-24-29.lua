inventorySlot= 1
turtle.select(inventorySlot)
function PotatoPlace()
    while turtle.getItemCount()==0 do
        inventorySlot= inventorySlot+1
        turtle.select(inventorySlot)
    end
    turtle.placeDown()

end

size=16
if 
     
        for i=1, size do
            for i=1, size do
        turtle.digDown()
        turtle.placeDown()
        turtle.forward()
        end
        turtle.turnRight()
        turtle.forward()
        turtle.turnRight()
            for i=1, size do
            turtle.digDown()
            turtle.placeDown()
            turtle.forward()
        end
        turtle.turnLeft()
        turtle.forward()
        turtle.turnLeft()
    end
        for i=1, size do
            turtle.digDown()
            turtle.placeDown()
            turtle.forward()
    end    

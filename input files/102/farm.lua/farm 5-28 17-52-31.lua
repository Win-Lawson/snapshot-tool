inventorySlot= 1
turtle.select(inventorySlot)
function PotatoPlace()
    while turtle.getItemCount()==0 do
        inventorySlot= inventorySlot+1
        turtle.select(inventorySlot)
        if inventorySlot == 17 then
            os.shutdown()
        end
    end
    turtle.placeDown()

end

turnRight= true
size=16
for i =1,4 do
    for i=1, size do
        turtle.digDown()
        PotatoPlace()
        turtle.forward()
    end
    if turnRight then
        turtle.turnRight()
        turtle.forward()
        turtle.turnRight()
    else
        turtle.turnLeft()
        turtle.forward()
        turtle.turnLeft()
    end
    turnRight= not turnRight
end
    

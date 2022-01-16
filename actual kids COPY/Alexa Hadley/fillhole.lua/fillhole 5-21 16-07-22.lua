inventoryslot=1
 for i=1, 10,  1 do
    turtle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
        inventoryslot= inventoryslot+1
        turtle.select(inventoryslot)
    end
        turtle.placeUp()
end

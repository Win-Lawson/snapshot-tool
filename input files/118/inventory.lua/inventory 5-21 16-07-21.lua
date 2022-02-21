InventorySlot=1
for i=1, 23, do
    tutle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
        inventorySlot= inventorySlot+1
        turtle.select(inventorySlot)
    end
    turtle.placeUp()
end

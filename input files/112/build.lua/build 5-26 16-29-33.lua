innventorySlots = 1

for i=1, 10 do
    turtle.forward()
    if not turtle.detectDown() then
        turtle.placeDown()
        inventorySlots = inventorySlots + 1
        turtle.select(inventorySlot)
    else
        turtle.placeUp()
        inventorySlots = inventorySlots + 1
    end
end

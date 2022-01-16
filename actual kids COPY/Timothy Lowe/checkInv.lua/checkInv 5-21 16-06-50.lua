function sortInv() 
    turtle.getItemCount(1)
    while turtle.getItemCount(1) < 30 do 
        for slot = 3, 16 do
            turtle.select(slot)
            if turtle.compareTo(1) == true then
                turtle.transferTo(1)
                turtle.select(1)
                break
            end
            if slot == 16 then
                print("Low on Blocks, need more!")
                break
            end
        end
    end
end

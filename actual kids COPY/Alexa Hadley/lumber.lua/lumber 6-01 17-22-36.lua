saplingI= 9
boneMealI= 13

function cutDown()
    turtle.select(1)
    if turtle.compare() then
        turtle.dig()
        turtle.forward()
        while turtle.compareUp() do
            turtle.digUp()
            turtle.up()
        end
        while not turtle.detectDown() do
            turtle.down()
    
        end
        turtle.back()
    end
end

function plant()
    turtle.select(9)
    sapling()
    turtle.place()
    turtle.select(1)
    while not turtle.compare() do 
        turtle.select(13)
        boneMeal()    
        turtle.place()
        turtle.select(1)
    end
end
function sapling()
    saplingI=9
    while turtle.getItemCount()==0 do
    saplingI= saplingI+1
        if saplingI == 13 then
            os.shutdown()
        end
    turtle.select(saplingI)
    end
end
function boneMeal()
        boneMealI= 13
    while turtle.getItemCount() == 0 do 
    boneMealI = boneMealI+1 
    if boneMealI== 17 then 
    os.shutdown()
    end
        turtle.select(boneMealI)
    end
            
end

while true do
cutDown()
plant()
end




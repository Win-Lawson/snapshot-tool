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
    turtle.place()
    turtle.select(1)
    while not turtle.compare() do 
        turtle.select(13)
            
        turtle.place()
        turtle.select(1)
    end
end
function sapling
while turtle.get
end
function boneMeal
end

while true do
cutDown()
plant()
end




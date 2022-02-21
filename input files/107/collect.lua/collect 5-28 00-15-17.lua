function up()
    while not turtle.up() do
        turtle.digUp()
    end
end

function cutTree()
    while turtle.compare() do
        turtle.dig()
        up()
    end
    while not turtle.detectDown() do 
        turtle.down()
    end
end 

fuction = search(dist)
    while dist > 0 do
        if turtle.compare() then
            cutTree()
        elseif not turtle.forward() then
            up()
        else
            dist = dist - 1
            while not turtle.detectDown() do
                turtle.down()
             end
         end
     end
 end 
    

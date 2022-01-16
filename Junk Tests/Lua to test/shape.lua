--
-- STEM+C
-- Authors: Brian Guerrero, Win Lawson
--
-- API allows for the creation of shapes with a given material
--
-- supply material with material without the "minecraft:" prefix

function line(size,material)
    material = "minecraft:"..material
    i = 1
    while i<=size do
        for j = 1, 16 do
            detail = turtle.getItemDetail(j)
            if detail~=nil then
                if detail.name == material then
                    turtle.select(j)
                    a=1
                    while a<=detail.count and i<=size+1 do
                        turtle.placeDown()
                        if i<size then
                            turtle.forward()
                        end
                        a=a+1
                        i=i+1
                    end
                end
            end
        end
    end
end

function square(size,material)
    for i=1, 4 do
        line(size, material)
        turtle.turnRight()
    end
end

function cube(size, material)
    for i=1, size do
        square(size,material)
        turtle.up()
    end
end

function pyramid(size,material)
    if size <= 0 then return end
    square(size,material)
    turtle.up()
    turtle.forward()
    turtle.turnRight()
    turtle.forward()
    turtle.turnLeft()
    pyramid(size-2,material)
end

function rectangle(width, length,material)
    for i=1, 2 do
        line(width,material)
        turtle.turnRight()
        line(length,material)
        turtle.turnRight()
    end

end
function prism(width, length, height,material)
    for i=1, height do
        rectangle(width, length,material)
        turtle.up()
    end
end

function roof(length,height, material)
    for i = 1, height do
        line(length,material)
        turtle.turnRight()
        turtle.turnRight()
        for x = 1, length-1 do
            turtle.forward()
        end
        turtle.turnLeft()
        turtle.up()
        turtle.forward()
        turtle.turnLeft()
    end
    turtle.down()
    turtle.down()
    for i = 1, height-1 do
        line(length,material)
        turtle.turnRight()
        turtle.turnRight()
        for x = 1, length-1 do
            turtle.forward()
        end
        turtle.turnLeft()
        turtle.forward()
        turtle.down()
        turtle.turnLeft()
    end
end
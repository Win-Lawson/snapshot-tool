--
-- STEM+C
-- Authors: Brian Guerrero, Win Lawson
--
-- API allows for the creation of shapes with a given material
--
-- supply material with material without the "minecraft:" prefix
-- material = 'all' --> turtle will use all materials starting with slot 1
-- material = 'random' --> turtle will choose a random slot until all are empty
function line_unspecified_material(size)
    slot= turtle.getSelectedSlot()
    turtle.select(slot)
    for i=1, size-1, 1 do
        while turtle.getItemCount(slot)==0 do
            slot= slot+1
            if slot == 17 then
                print("Out of Materials") return
            end
            turtle.select(slot)
        end
        turtle.placeDown()
        turtle.forward()
    end
    turtle.placeDown()
end

function line_random_material(size)
    for i = 1, size-1, 1 do
        turtle.select(math.random(1,16))
        while turtle.getItemCount()==0 do
            turtle.select(math.random(1,16))
        end
        turtle.placeDown()
        turtle.forward()
    end
    turtle.placeDown()
end

function line(size,material)
    if material == 'all' then
        line_unspecified_material(size)
    elseif material == 'random' then
        line_random_material(size)
    else
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
                    elseif j == 16 then
                        print('out of materials')
                    end
                elseif j==16 then
                    print('out of materials')
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

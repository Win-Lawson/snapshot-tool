-- look for logs automatically and collect them
-- be able to traverse hills
-- be able to replant trees
os.loadAPI("HelpfulAPI")

function hills()
    if not turtle.detectDown() then
        turtle.down()
    end
end

function replant()
    turtle.place("birch_sapling")
end

-- be able to know when the tree ends
-- but how
function mine()
i=1
for i<10 do
    while isWood()
        if result == true then
            turtle.dig()
                turtle.up()
        else
            print("false")
        end   
    end
end
end

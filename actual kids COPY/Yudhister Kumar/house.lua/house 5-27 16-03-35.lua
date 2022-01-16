os.loadAPI("shape.lua")

for i=1, 5 do
    turtle.up()
    shape.square(5, "all")
end
shape.pyramid(8, "all")

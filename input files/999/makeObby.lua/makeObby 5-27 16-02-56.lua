os.loadAPI("obstacles.lua")
os.loadAPI("checkInv.lua")
randNum=1
for f=1, 10 do
    randNum = math.random(7)
    if randNum==1 then
        obstacles.basicFor()
    elseif randNum==2 then
        obstacles.basicUp()
    elseif randNum==3 then
        obstacles.basicDown()
    elseif randNum==4 then
        obstacles.basicAround()
    elseif randNum==5 then
        obstacles.ladderClimb()
    elseif randNum==6 then
        obstacles.basicBar()
    elseif randNum==7 then
        obstacles.barWalk()
    end
    turtle.forward()
    turtle.select(3)
    turtle.placeDown()
    turtle.select(1)
    checkInv.sortInv()
end
turtle.forward()
shell.run("dance")

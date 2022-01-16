-- look for logs automatically and collect them
-- be able to traverse hills
-- be able to replant trees

function detectLogs()
    while turtle.detect("birch_log") do
        result = true
    end
end

function hills()
    if not turtle.detect() then
        turtle.down()
    end
end

function replant()
    turtle.place("birch_sapling")
end

-- be able to know when the tree ends
function mine()
    detectLogs()
end
    
    




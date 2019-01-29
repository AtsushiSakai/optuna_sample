"

 Himmelblau function

 author: Atsushi Sakai
"

function himmelblau_function(x, y)
    return (x^2 + y - 11)^2 + (x + y^2 - 7)^2
end

x = parse(Float64,ARGS[1])
y = parse(Float64,ARGS[2])
println(himmelblau_function(x, y))


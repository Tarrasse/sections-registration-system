function reg(s){
    var url = "/sections/register?id=" + s;
    $.ajax({
        type: "GET",
        url:url,
    });
}

function logout(){
    var url = "/sections/logout";
    $.ajax({
        type: "GET",
        url:url
    });
}
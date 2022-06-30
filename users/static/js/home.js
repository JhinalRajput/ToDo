$("#btn-signup").click(function(){
    event.preventDefault();
    const uname = document.querySelector("#username").value;
    const email_id = document.querySelector("#email_id").value;
    const pass1 = document.querySelector("#password").value;
    const pass2 = document.querySelector("#conpassword").value;

    //alert(uname+" "+email_id+ " " +pass1+" "+pass2);

    if(email_id.indexOf("@")==-1 || email_id.lastIndexOf(".")==-1){
        $("[rel=email_id]").popover({
            trigger: 'hover',
            html: true,
        }).popover('toggle');
    }
    else if(pass1 !== pass2){
        $("[rel=pass2]").popover({
            trigger: 'hover',
            html: true,
        }).popover('toggle');
    }
    else{
        $.ajax({

        })
    }

});
<!-- sign up page -->
<?php
    if(isset($_POST["name"]) && isset($_POST["email"]) && isset($_POST["password"])){
        $name=$_POST["name"];
        $email=$_POST["email"];
        $password=$_POST["password"];

        $conn=new mysqli("localhost","root","","users");
        //checking
        $sql="select * from user_registered where name='$name' and email='$email'";
        $result=$conn->query($sql);
        if($result->num_rows>0){
            die("This name and email is already registered.");
        }else{
            $sql="insert into user_registered (email,password,name) values ('$email','$password','$name');";
            if($conn->query($sql)){
                header("Location:login.html");
            }else{
                die("Error occured");
            }
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign up</title>
</head>
<body>
    <div class="signupbox">
        <form method="post" action="index.php">
            <span>Name</span>
            <input type="text" name="name" placeholder="Enter Your Name..">
            <br><br>
            <span>Email</span>
            <input type="text" name="email" placeholder="Enter Your Email..">
            <br><br>
            <span>Password</span>
            <input type="password" name="password" placeholder="Set Your Password..">
            <br><br>
            <button type="submit">Submit</button>
            <button type="reset">Reset</button>
        </form>
    </div>
    <br>
    <a href="login.html">Login instead</a>
</body>
</html>
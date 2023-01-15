<?php
    $username="root";
    $password="";
    $servername="localhost";
    $db="users";
    $connection= new mysqli($servername,$username,$password,$db);
    if($connection->error){
        echo "Error Occured";
    }
    if(isset($_POST["email"])){
        $email=$_POST["email"];
        $pw=$_POST["password"];
        // echo "<br>$email<br>$pw";
        
        $sql="select * from user_registered where email='$email' and password='$pw';" ;
        // echo "<br>$sql";
        $result=$connection->query($sql);
        if($result->num_rows!=1){
            die ("You are not registered");
        }
    }



    $connection2= new mysqli("localhost","root","","to_do_list");
    $email=$_POST["email"];
    $pw=$_POST["password"];
    //inputbox handling
    if(isset($_POST["inputbox"]) && $_POST["inputbox"]!=""){
        $task=$_POST["inputbox"];
        $sql="insert into tasks values ('$email','$task',CURRENT_TIMESTAMP);";
        $connection2->query($sql);
    }
?>


<html>
    <head>
        <title>To-do list</title>
        <style>
            body{
                display:flex;
                flex-direction:row;
                gap:3rem;
            }
            .task{
                box-sizing:border-box;
                padding:10px;
                border:1px solid black;
                margin-bottom:5px;
                width:fit-content;
            }
            .task p{
                margin-bottom:0px;
            }
            .hidden{
                display:none;
            }
        </style>
    </head>
    <body>
        <div class="box1">
            <h1>To Do list</h1>
            <form action="file.php" method="post">
                <?php
                    // echo $_POST["email"];
                    echo "<input type='text' value=$email name='email' id='email' style='display:none;'>";
                    echo "<input type='text' value=$pw name='password' id='password' style='display:none;'>";
                ?>
                <input type="text" id="inputbox" name="inputbox">
                <button type="submit" id="submit">Submit</button>
            </form>
            
            
        <div class="tasks">
            <?php
                //delete handling
                if(isset($_POST["task-delete"])){
                    $dtask=$_POST["task-delete"];
                    $dentry=$_POST["entry-delete"];
                    $sql="delete from tasks where user='$email' and task='$dtask' and entrytime='$dentry'";
                    $connection2->query($sql);
                }
            ?>
            <?php
                //edit handling
                if(isset($_POST["task-edit"]) && isset($_POST["change"]) && $_POST["change"]!="" ){
                    $newtask=$_POST["change"];
                    $prevtask=$_POST["task-edit"];
                    $editentry=$_POST["entry-edit"];
                    $sql="update tasks set task='$newtask' where task='$prevtask' and user='$email' and entrytime='$editentry'";
                    $connection2->query($sql);
                }
            ?>
            <?php
                $result=$connection2->query("select task, entrytime from tasks where user='$email';");
                if($result->num_rows>0){
                    $counter=1;
                    while($row=$result->fetch_assoc()){
                        $task=$row["task"]; //this task is different from the task in Form handle. aru kunai variable name sochna na sakera ho
                        $entry=$row["entrytime"];
                        echo "
                        <div id='$counter' class='task'>
                            <p>
                            Task=><span id='task-$counter'>$task</span>
                            <br>
                            Entry=><span id='entry-$counter'>$entry</span>
                            <br><br>
                            </p>
                            <button class='delete' id='delete-$counter'>Delete</button>
                            <button class='edit' id='edit-$counter'>Edit</button>
                            </div>
                            ";
                            $counter++;
                        }
                    }else{
                        echo "<br>No tasks are entried.";
                    }
                ?>
            </div>
        </div>
        <div class="box2">
            <div id="query" class="hidden">
                <div class="confirmation-box"></div>
                <button class="cancel">Cancel</button>
            </div>
        </div>
        <script src="./app2.js"></script>
    </body>
</html>